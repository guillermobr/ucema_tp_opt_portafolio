import sys

def simular(data, tickers, q, n_stocks=5, w_min=0.05, w_max=0.50):
    datos = []
    with tqdm.tqdm(total=q, file=sys.stdout) as pbar:
        for i in range(q):
            pbar.update()

            muestra = data[random.sample(tickers, n_stocks)]

            ponds = np.random.dirichlet(np.ones(n_stocks), 100)
            pond = np.array([w for w in ponds if (w.min() > w_min) & (w.max() < w_max)][0])

            if len(retornos):
                r = {}
                r['activos'] = list(muestra.columns)
                r['weights'] = pond.round(5)
                r['retorno'] = np.sum((muestra.mean() * pond * 252))
                r['volatilidad'] = np.sqrt(np.dot(pond, np.dot(muestra.cov() * 252, pond)))
                r['Sharpe Simple'] = round(r['retorno'] / r['volatilidad'], 5)
                datos.append(r)

    df = pd.DataFrame(datos).sort_values('Sharpe Simple', ascending=False)

    return df