import sys, numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
OUT=sys.argv[1]; DATA=sys.argv[2]
NAVY='#1a3a5c'; BLUE='#2980b9'; RED='#c0392b'; GREY='#95a5a6'; INK='#2c3e50'; MUTED='#7f8c8d'
plt.rcParams.update({'font.size':13,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#bbbbbb',
  'axes.titleweight':'bold','axes.titlecolor':NAVY,'axes.titlesize':15,'axes.titlepad':14,'text.color':INK,'axes.labelcolor':INK,
  'xtick.color':INK,'ytick.color':INK})
def br(x,d=1): return f"{x:.{d}f}".replace('.',',')
def thou(x): return f"{int(x):,}".replace(',','.')

# ---------- 1. Temporal (microdados, horário de Brasília) ----------
d=pd.read_csv(DATA); t=pd.to_datetime(d.date,utc=True).dt.tz_convert('America/Recife')
h=t.dt.hour.value_counts().sort_index().reindex(range(24),fill_value=0); hp=h/h.sum()*100
w=t.dt.dayofweek.value_counts().sort_index(); wp=w/w.sum()*100
fig,(a1,a2)=plt.subplots(1,2,figsize=(13,5.6),gridspec_kw={'width_ratios':[1.6,1]})
cols=[RED if i==10 else ('#f39c12' if i==5 else BLUE) for i in range(24)]
a1.bar(range(24),hp.values,color=cols,width=0.8,edgecolor='white',linewidth=1)
a1.axvspan(7.5,17.5,color='#f9e79f',alpha=0.35,zorder=0,lw=0)
a1.text(12.5,hp.max()*1.13,'Horário comercial (8h–17h59): '+br(hp.loc[8:17].sum())+'%',ha='center',fontsize=11.5,color=INK)
a1.annotate('Pico: 10h ('+br(hp[10])+'%)',xy=(10,hp[10]),xytext=(17.5,hp[10]*0.96),fontsize=11.5,color=RED,fontweight='bold',
  arrowprops=dict(arrowstyle='->',color=RED),va='center')
a1.annotate('Mínimo: 5h ('+br(hp[5])+'%)',xy=(5,hp[5]),xytext=(0.2,hp.max()*0.55),fontsize=11.5,color='#b9770e',fontweight='bold',
  arrowprops=dict(arrowstyle='->',color='#b9770e'))
a1.set_ylim(0,hp.max()*1.25); a1.set_xticks(range(0,24,2)); a1.set_xlabel('Hora do registro (horário de Brasília)'); a1.set_ylabel('Denúncias (%)')
a1.set_title('(A) Distribuição por hora do dia'); a1.grid(axis='y',ls=':',alpha=.5)
dias=['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']
a2.bar(dias,wp.values,color=[BLUE]*5+[RED]*2,width=0.7,edgecolor='white')
for i,v in enumerate(wp.values): a2.text(i,v+0.4,br(v),ha='center',fontsize=11.5)
a2.set_ylim(0,wp.max()*1.22); a2.set_ylabel('Denúncias (%)'); a2.set_title('(B) Distribuição por dia da semana'); a2.grid(axis='y',ls=':',alpha=.5)
fig.text(0.01,0.005,'Fonte: microdados do Disque 100 (MDHC), Região Nordeste, 2024 (n = '+thou(len(d))+' registros).',fontsize=10,color=MUTED)
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig(OUT+'/disque100_temporal.png',dpi=220); plt.close()
print('weekday%',wp.round(2).tolist(),'8-17',hp.loc[8:17].sum())

# ---------- 2. Perfil social (Tabela 1) ----------
def hbar(ax,labels,vals,title,hl=0):
    y=np.arange(len(labels))[::-1]
    ax.barh(y,vals,color=[NAVY if i==hl else BLUE for i in range(len(vals))],height=0.65,edgecolor='white')
    for yi,v in zip(y,vals): ax.text(v+1.2,yi,br(v,2)+'%',va='center',fontsize=12)
    ax.set_yticks(y); ax.set_yticklabels(labels,fontsize=12); ax.set_xlim(0,max(vals)*1.28); ax.set_title(title,loc='left')
    ax.set_xlabel('Denúncias (%)',fontsize=11); ax.grid(axis='x',ls=':',alpha=.5)
fig,ax=plt.subplots(2,2,figsize=(14,9.6))
hbar(ax[0,0],['Terceiros','Própria vítima','Próprio agressor','Não informado'],[85.22,14.64,0.13,0.01],'(A) Quem realizou a denúncia')
hbar(ax[0,1],['Ligação telefônica','WhatsApp','Outros canais'],[90.86,8.20,0.94],'(B) Canal da denúncia')
hbar(ax[1,0],['Até 2 anos','3 a 11 anos','12 a 17 anos','18 a 59 anos','60 a 90+ anos','Não informado'],[6.22,25.66,14.87,15.85,33.81,3.59],'(C) Faixa etária da vítima',hl=4)
hbar(ax[1,1],['Casa da vítima\ne do suspeito','Casa da vítima','Casa do suspeito','Outros locais'],[48.90,30.43,4.46,16.21],'(D) Local da violação')
fig.text(0.01,0.005,'Fonte: Tabela 1 do artigo (Disque 100/MDHC, Nordeste, 2024; n = 110.278).',fontsize=10.5,color=MUTED)
fig.tight_layout(rect=(0,0.025,1,1),h_pad=2.5,w_pad=3); fig.savefig(OUT+'/disque100_perfil_social.png',dpi=220); plt.close()

# ---------- 3. Convergência (barras) ----------
fig,ax=plt.subplots(figsize=(10.5,7.2))
labs=['RIE > 2,0','Taxa EBEL > 2 por mil hab.','Varredura Scan significativa\n(α = 0,05)','Interseção dos três critérios','Interseção com população\n> 57.112 hab.']
vals=[52,311,291,49,6]; y=np.arange(5)[::-1]
ax.barh(y,vals,color=[BLUE,BLUE,BLUE,RED,NAVY],height=0.62,edgecolor='white')
for yi,v in zip(y,vals): ax.text(v+5,yi,str(v),va='center',fontsize=15,fontweight='bold')
ax.set_yticks(y); ax.set_yticklabels(labs,fontsize=13.5); ax.set_xlim(0,360); ax.set_xlabel('Número de municípios')
ax.axhline(1.5,color='#bbbbbb',lw=1,ls='--'); ax.grid(axis='x',ls=':',alpha=.5)
ax.set_title('Municípios selecionados por critério e pela convergência',loc='left')
ax.text(110,0,'Recife (PE), Natal (RN), Parnaíba (PI),\nCasa Nova (BA), Ceará-Mirim (RN), Extremoz (RN)',va='center',fontsize=11.5,color=INK)
fig.tight_layout(); fig.savefig(OUT+'/triangulacao_convergencia.png',dpi=220); plt.close()

# ---------- 4. Diagramas ilustrativos ----------
rng=np.random.default_rng(7)
# shrinkage
n=np.exp(rng.uniform(np.log(2000),np.log(1.5e6),140)); lam=1.93/1000*np.exp(rng.normal(0,0.15,140))
y_=rng.poisson(n*lam); r=y_/n*1000; m=1.93; s2=0.08
wgt=s2/(s2+m/(n/1000)); th=wgt*r+(1-wgt)*m
fig,ax=plt.subplots(figsize=(11,6.6))
for ni,ri,ti in zip(n,r,th):
    if ni<8000 and abs(ri-ti)>1.2: ax.annotate('',xy=(ni,ti),xytext=(ni,ri),arrowprops=dict(arrowstyle='->',color='#8e44ad',lw=1.1,alpha=.8))
ax.scatter(n,r,s=36,color='#e6a1a1',edgecolor='white',label='Taxa bruta  $r_i = y_i/n_i$',zorder=3)
ax.scatter(n,th,s=36,marker='s',color=BLUE,edgecolor='white',label=r'Taxa suavizada  $\hat{\theta}_i$',zorder=4)
ax.axhline(m,color='#27ae60',ls='--',lw=2,label=r'Média da vizinhança  $\bar{r}_i$')
ax.set_xscale('log'); ax.set_xlabel('População do município (escala logarítmica)'); ax.set_ylabel('Denúncias por 1.000 hab.')
ax.text(2300,max(r.max(),5)*1.03,'Pequena população:\nmaior variância, maior encolhimento',fontsize=11.5,color='#8e44ad')
ax.text(1.2e5,max(r.max(),5)*1.03,'Grande população:\ntaxa bruta preservada ($w_i \\approx 1$)',fontsize=11.5,color=BLUE)
ax.set_ylim(-0.2,max(r.max(),5)*1.35); ax.legend(loc='upper center',ncol=3,fontsize=11.5,frameon=True,bbox_to_anchor=(0.5,1.0)); ax.grid(ls=':',alpha=.4)
ax.set_title('Efeito de encolhimento (shrinkage) do EBEL — ilustração com dados simulados',loc='left',fontsize=14)
fig.tight_layout(); fig.savefig(OUT+'/bayes_shrinkage_diagram.png',dpi=220); plt.close()
# scan
fig,ax=plt.subplots(figsize=(10.5,7.2)); pts=rng.uniform(0,10,(70,2)); c=np.array([6.3,5.2])
ins=np.linalg.norm(pts-c,axis=1)<1.9
for rr,a in [(0.9,.9),(1.4,.7),(1.9,1)]: ax.add_patch(Circle(c,rr,fill=(rr==1.9),fc='#fadbd8',ec=RED,ls='--',lw=2 if rr==1.9 else 1.2,alpha=a,zorder=1))
ax.scatter(*pts[~ins].T,s=45,color=GREY,label='Centróides fora da janela',zorder=3)
ax.scatter(*pts[ins].T,s=70,color=RED,label='Centróides dentro da janela $Z$',zorder=3)
ax.scatter(*c,marker='*',s=380,color=NAVY,label='Centróide de origem da janela',zorder=4)
ax.annotate('Raio crescente até o limite de\n0,1% da população (57.112 hab.)',xy=(c[0]+1.35,c[1]+1.35),xytext=(6.6,9.6),fontsize=11.5,color=RED,bbox=dict(boxstyle='round,pad=0.3',fc='white',ec='none'),arrowprops=dict(arrowstyle='->',color=RED))
ax.text(0.2,9.0,r'$H_0: p = q$   vs.   $H_1: p > q$'+'\nSignificância via Monte Carlo (α = 0,05)',fontsize=12,color=INK,
  bbox=dict(boxstyle='round,pad=0.5',fc='#eaf2f8',ec=BLUE))
ax.set_xlim(-0.3,10.3); ax.set_ylim(-0.3,10.6); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
for s_ in ax.spines.values(): s_.set_visible(False)
ax.legend(loc='lower left',fontsize=11,frameon=True,ncol=1)
ax.set_title('Varredura Scan espacial (Kulldorff & Nagarwalla, 1995) — esquema',loc='left',fontsize=14)
fig.tight_layout(); fig.savefig(OUT+'/scan_statistic_diagram.png',dpi=220); plt.close()
# moran scatter
z=rng.normal(0,1,160); lag=0.45*z+rng.normal(0,0.55,160)
q=np.where((z>0)&(lag>0),0,np.where((z<0)&(lag<0),1,np.where(z>0,2,3)))
cc=[RED,BLUE,'#f39c12','#8e44ad']; nm=['Alto-Alto','Baixo-Baixo','Alto-Baixo','Baixo-Alto']
fig,ax=plt.subplots(figsize=(8.6,7.6))
for k in range(4): ax.scatter(z[q==k],lag[q==k],s=40,color=cc[k],edgecolor='white',label=nm[k],zorder=3)
xx=np.linspace(-3,3,10); b=np.polyfit(z,lag,1)[0]; ax.plot(xx,b*xx,color=NAVY,lw=2,label='Reta de regressão (inclinação = I)')
ax.axhline(0,color='#999',ls='--',lw=1); ax.axvline(0,color='#999',ls='--',lw=1)
for (x0,y0,tx,col) in [(1.6,2.1,'Q1: Alto-Alto',RED),(-2.3,2.1,'Q2: Baixo-Alto','#8e44ad'),(-2.3,-2.3,'Q3: Baixo-Baixo',BLUE),(1.6,-2.3,'Q4: Alto-Baixo','#b9770e')]:
    ax.text(x0,y0,tx,fontsize=12.5,fontweight='bold',color=col,bbox=dict(boxstyle='round,pad=0.2',fc='white',ec='none'),zorder=5)
ax.set_xlim(-3,3); ax.set_ylim(-2.6,2.6); ax.set_xlabel(r'Valor padronizado do município ($z_i$)'); ax.set_ylabel(r'Defasagem espacial ($\mathbf{W}z$)')
ax.legend(loc='lower right',fontsize=10,bbox_to_anchor=(1,0.08)); ax.set_title('Diagrama de dispersão de Moran — dados simulados',loc='left',fontsize=14)
fig.tight_layout(); fig.savefig(OUT+'/moran_scatterplot_diagram.png',dpi=220); plt.close()
# fluxograma
boxes=[('1. Aquisição e integração',['Dados abertos Disque 100 (MDHC, 2024)','110.278 denúncias no Nordeste','População estimada IBGE 2024 (SIDRA)','1.793 municípios'],BLUE),
 ('2. Razão de Incidência Espacial',['Incidência local vs. regional','80% dos municípios com RIE < 1','136 com RIE > 1,5; 52 com RIE > 2','Máximo: Salgadinho-PB (12,9)'],'#d68910'),
 ('3. Autocorrelação espacial',['W: contiguidade por arestas e vértices','Moran Global: I = 0,12 (p < 0,01)','LISA: 51 Alto-Alto; 9 Baixo-Baixo','219 Alto-Baixo ou Baixo-Alto'],'#27ae60'),
 ('4. Suavização bayesiana (EBEL)',['Estimador de Marshall (1991)','825 municípios com taxa < 1 por mil','311 municípios com taxa > 2 por mil','Máximo: Salgadinho-PB (24,27 por mil)'],'#8e44ad'),
 ('5. Varredura Scan (Kulldorff)',['Janelas circulares, modelo de Poisson','Teste por simulação Monte Carlo','Limite: 0,1% da população (57.112 hab.)','291 municípios significativos'],RED),
 ('6. Convergência multimétodo',['RIE > 2  ∩  EBEL > 2  ∩  Scan','49 municípios na interseção','6 com população > 57.112 hab.'],'#34495e')]
fig,ax=plt.subplots(figsize=(16,6.4)); ax.set_xlim(0,48); ax.set_ylim(0,19.2); ax.axis('off')
pos=[(0.5,10.4),(16.5,10.4),(32.5,10.4),(32.5,0.3),(16.5,0.3),(0.5,0.3)]; W_,H_=15,8.4
for (tt,items,col),(x,y) in zip(boxes,pos):
    ax.add_patch(FancyBboxPatch((x,y),W_,H_,boxstyle='round,pad=0.02,rounding_size=0.8',fc=col+'18',ec=col,lw=2.5))
    ax.text(x+0.7,y+H_-1.2,tt,fontsize=16.5,fontweight='bold',color=col,va='top')
    ax.text(x+0.8,y+H_-3.3,'\n'.join('• '+i for i in items),fontsize=14.5,color=INK,va='top',linespacing=1.55)
ar=dict(arrowstyle='-|>',color=NAVY,lw=2.5,mutation_scale=22)
ax.annotate('',xy=(16.4,14.6),xytext=(15.6,14.6),arrowprops=ar); ax.annotate('',xy=(32.4,14.6),xytext=(31.6,14.6),arrowprops=ar)
ax.annotate('',xy=(40,8.8),xytext=(40,10.3),arrowprops=ar); ax.annotate('',xy=(31.6,4.5),xytext=(32.4,4.5),arrowprops=ar)
ax.annotate('',xy=(15.6,4.5),xytext=(16.4,4.5),arrowprops=ar)
fig.tight_layout(pad=0.3); fig.savefig(OUT+'/metodologia_fluxograma.png',dpi=200); plt.close()
print('ok')
