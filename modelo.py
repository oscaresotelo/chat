from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
the_model = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
tokenizer= AutoTokenizer.from_pretrained(the_model, do_lower_case= False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)
contexto = "En 1533 llegó el conquistador español del Perú Diego de Almagro para explorar las actuales regiones de la Quebrada de Humahuaca y los Valles Calchaquíes. En 1543 otro español: Diego de Rojas recorrió el territorio. La región dependía administrativamente de Chile pero estaba casi en el límite con el territorio dependiente de Charcas, lo que motivó disputas jurisdiccionales que originaron los traslados poblacionales Desde la creación del Virreinato del Perú por Real Cédula del 1 de marzo de 1543, la región del Tucumán quedó integrada en él.El primer asentamiento español en la región fue El Barco, fundada en 1550 por Juan Núñez de Prado, proveniente del Perú. La población fue luego trasladada dos veces (El Barco II y El Barco III), hasta establecerse definitivamente a orillas del Río del Estero en 1553, con el nombre de Santiago del Estero fuera de los límites de la jurisdicción chilena. El núcleo humano que conformaron los primeros vecinos de Santiago del Estero fue el primero con el que la corona de Castilla logró un asiento definitivo en lo que actualmente constituye territorio de la República Argentina. En 1560 el español Juan Pérez de Zurita fundó la ciudad de Cañete.		La provincia fue creada en 1564, con el nombre de Provincia de Tucumán, Juríes y Diaguitas, su primer gobernador fue Francisco de Aguirre con sede en Santiago del Estero. Con la creación de la Gobernación del Tucumán en 1566 y del Obispado en 1570, esta región empezó a cobrar importancia. Por orden de Aguirre, Diego de Villarroel fundó San Miguel de Tucumán el 31 de mayo de 1565 en un sitio llamado Ibatín por los nativos de etnia lule.En pleno momento fundacional de la ciudad de San Miguel del Tucumán arreciaba la Guerra Calchaquí, una de las más denodadas resistencias habidas a la ocupación española, al punto que en octubre de 1578 los diaguitas calchaquíes estuvieron casi a punto de destruir la ciudad de origen español, en efecto los principales protagonistas de tal resistencia fueron los diaguitas quienes tras prácticamente un siglo de enconada lucha fueron debelados pueblo por pueblo y ciudad por ciudad, siendo en muchas ocasiones desarraigados y casi todas sus pequeñas ciudades arrasadas.		La ciudad de San Miguel de Tucumán fue trasladada a su actual emplazamiento el 27 de septiembre de 1685 por el teniente gobernador Miguel de Salas y Valdez cumpliendo órdenes del gobernador Fernando de Mendoza y Mate de Luna.		En la época anterior a la creación del Virreinato del Río de La Plata, la palabra Tucumán o región del Tucumán era dada por los españoles a un extenso territorio de 700.000 km² que abarcaba de norte a sur los territorios y actuales provincias de Tarija, Jujuy, Salta, Catamarca, Tucumán, Santiago del Estero, La Rioja, San Juan, Córdoba, San Luis y Mendoza.		En 1776 la Gobernación del Tucumán pasó a formar parte del recién creado Virreinato del Río de la Plata, con capital en la ciudad de Santiago del Estero		Al subdividirse administrativamente el Virreinato del Río de la Plata, conforme a la Real Ordenanza de Intendentes del 28 de enero de 1782, la actual provincia de Tucumán quedó ubicada dentro de la Gobernación Intendencia del Tucumán, de efímera duración . La Real Cédula del 5 de agosto de 1783, suprimió la Gobernación Intendencia del Tucumán, con lo cual Tucumán junto con Catamarca, Santiago del Estero, Jujuy, Salta, Tarija y la Puna de Atacama, pasaron a integrar la nueva Gobernación Intendencia de Salta del Tucumán, con sede gubernativa en la ciudad de Salta.			Mientras el resto del territorio formó la de Gobernación Intendencia de Córdoba del Tucumán que incluía a Córdoba, San Luis, Mendoza, San Juan, La Rioja y pequeños sectores occidentales de la actual provincia de Santa Fe, siendo la ciudad de Córdoba su capital y metrópoli."
pregunta = "cuando llego el conquistador español?"
nlp = pipeline("question-answering",model = model,tokenizer=tokenizer)
salida = nlp({"question":pregunta, "context": contexto })
# print(salida)
from textwrap import wrap 
def pregunta_respuesta(model, contexto,nlp):
	print("contexto")
	print("----------")
	print("\n".join(wrap(contexto)))

	continuar = True
	while continuar:
		print("\nPregunta")
		print("------")
		pregunta = str(input())

		continuar = pregunta!=""

		if continuar:
			salida = nlp({"question":pregunta, "context": contexto})
			print("\nRespuesta:")
			print("--------------")
			print(salida["answer"])

pregunta_respuesta(model,contexto, nlp)