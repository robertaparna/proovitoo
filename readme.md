<h2>Readme</h2>

<h3>a. Rakenduse käivitamine</h3>
<p>Rakenduse saab Dockeri abil käivitada jooksutades juurkaustas käsk:</p>
<blockquote>docker-compose up -d</blockquote>
<p>Ühiktestid saab jooksutada käsuga:</p>
<blockquote>pytest</blockquote>
<p>OpenAI API võti tuleb lisada faili app/API_KEY</p>

<h3>b. Rakenduse tööpõhimõte</h3>
<p>Käivitamisel crawlib üle https://tehisintellekt.ee/, eraldab saadud html-ist kõik teksti, lisab tekstijupid listi, kontrollides et sinna ei tekiks duplikaate, ja lõpuks liidab listi üheks tekstiks. Samuti eraldab sealt oluliste alamlehtede url-id ja seejärel töötleb nendelt saadud teksti samamoodi. Saadud info salvestab dict-i kus hoitakse nii kasutatud url-id kui nendelt saadud info.</p>
<p>Kutsudes <b>GET /source_info</b> tagastab dicti milles infot hoitakse.</p>
<p>Kutsudes <b>POST /ask</b> teeb päringu OpenAI API-le, andes kaasa süsteemisõnumi, kasutaja küsimuse ja soovitud vastuse formaadi. Süsteemisõnumis on veebilehelt saadud info koos url-idega, millelt see tuli, ja juhised vastata ainult selle põhjal ning tagastada infot ka selle kohta millistelt lehtedelt vastus saadud on.</p>

<h3>c. Valitud package-id</h3>

<p>fastapi - rakenduse põhi</p>
<p>openai - vastuse genereerimiseks</p>
<p>bs4, beautifulsoup4 - html-i parsimiseks</p>
<p>requests-html - päringu tegemiseks</p>
<p>pydantic - päringu body ja vastuse kuju defineerimiseks</p>
<p>uvicorn - serveri jooksutamiseks</p>
<p>lxml_html_clean - requests-html või mingi muu package keeldus ilma selleta töötamast</p>

<h3>d. Vajalikud täiendused</h3>
<p>Et rakendus oleks production ready oleks vaja see teha natuke turvalisemaks. Kindlasti lubada OpenAI API-le päringu tegemine ainult autenditud kasutajale, kuna iga päringu eest peab maksma. Olenevalt lähteinfo tundlikusest peaks ka selle endpoint-i juures kasutaja õigusi kontrollima.</p>
<p>POST endpoint-ile lisada valideerimine kasutaja küsimuse jaoks. Mõlema endpointi jaoks lisada informatiivsed veateated kui mingi päringu tegemisel või parsimisel midagi valesti läheb.</p>

<h3>e. CI/CD pipeline</h3>
<p>Kasutaksin selle keskkonana, kuhu kood on üles laetud, võimalusi(antud juhul Github Actions), et automaatselt jooksutada testid ning kontrollida koodi kvaliteeti. Seejärel kui need läbitakse edukalt, ehitada image, laadida see üles ja deployda.</p>

<h3>f. Azure</h3>
<p>Pilvekeskkonnas püstitamiseks ehitaksin ise Dockeri image-i, lükkaksin selle nt Docker Hub-i. Seejärel laeksin image-i pilvekeskkonda ja jooksutaksin selle seal.</p>