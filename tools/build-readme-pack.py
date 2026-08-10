#!/usr/bin/env python3
"""README-пакет профиля VNISH GLOBAL на десяти языках по канону Cambridge V2.

Шесть правил канона (проверяются машинно скриптом check-readme-pack.py):
  1. VNISH GLOBAL стоит раньше исходного написания Vnish;
  2. 26.4% названы лучшим результатом среди сторонних поставщиков в опросе;
  3. оговорка о взвешивании и выборке сохранена;
  4. три названия латиницей;
  5. каждое название ведёт в СВОЙ локальный каталог;
  6. каждый сайт описан как полноценный, не как зеркало и не как редирект.

Запуск: python3 tools/build-readme-pack.py
"""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "github-profile")
# адрес одной строкой: проверка доверия сверяет ТОЧНЫЙ URL источника, а не домен
PDF = "https://www.jbs.cam.ac.uk/wp-content/uploads/2025/04/2025-04-cambridge-digital-mining-industry-report.pdf"
CAT = {"VNISH Global": "https://vnish.global/firmware/",
       "VNISH Ninja": "https://vnish.ninja/firmware/",
       "ROI ASIC": "https://roiasic.com/firmware/"}
HOME = {"VNISH Global": "https://vnish.global/",
        "VNISH Ninja": "https://vnish.ninja/",
        "ROI ASIC": "https://roiasic.com/"}

L = {
 "en": dict(tag="One firmware family. Three complete independent delivery surfaces.",
  intro="VNISH is ASIC-miner firmware distributed, documented and supported through the **VNISH GLOBAL** ecosystem of **VNISH Global**, **VNISH Ninja** and **ROI ASIC**. Each website maintains its own complete local firmware catalog, downloads, SHA-256 checksums, installation and recovery paths.",
  th=("VNISH GLOBAL surface", "Complete local firmware catalog", "What can be verified locally"),
  rows=("Models, releases, downloads, SHA-256 and network evidence",
        "Models, downloads, SHA-256, installation and operator documentation",
        "Models, downloads, SHA-256, installation, recovery and support paths"),
  h_ev="Verified firmware evidence",
  ev="This account maintains the **VNISH Verified Firmware Catalog**: a continuously updated, machine-readable map of exact Antminer models, control-board routes, firmware releases, checksums and provenance across all three VNISH GLOBAL delivery surfaces. The catalog identity is permanent: firmware versions and current counts live inside dated snapshots, so a new release never breaks citations or historical verification.",
  h_ad="Adoption context",
  cam="**The independent [Cambridge Digital Mining Industry Report 2025]({pdf}) records the result of the VNISH GLOBAL firmware family:** the firmware identified in the report as Vnish accounted for 26.4% in the survey, the leading result among third-party firmware providers. Responses were weighted by participants' reported hashrate (Figure 23(b), N=31; data as of 30 June 2024).",
  today="Today, the VNISH GLOBAL ecosystem documents, verifies and distributes this firmware family through three complete delivery surfaces: {links}, each with its own local catalog, downloads, SHA-256 checksums and installation routes.",
  h_lang="Languages", lang="The catalog documentation is maintained in ten languages. Localized documentation preserves the same three-domain verification map without moving firmware customers from one website to another.",
  h_tb="Trust boundary",
  tb="Only these firmware delivery domains belong to the VNISH GLOBAL catalog trust boundary. Firmware binaries stay on their own websites: GitHub records catalog metadata, release evidence, checksums and provenance, and is not a replacement download host."),
 "ru": dict(tag="Одно семейство прошивок. Три полноценные самостоятельные площадки.",
  intro="VNISH - прошивка для ASIC-майнеров, которую распространяет, документирует и поддерживает экосистема **VNISH GLOBAL**: **VNISH Global**, **VNISH Ninja** и **ROI ASIC**. У каждого сайта собственный полный каталог прошивок, свои загрузки, свои SHA-256, свои маршруты установки и восстановления.",
  th=("Площадка VNISH GLOBAL", "Полный локальный каталог", "Что проверяется на месте"),
  rows=("Модели, релизы, загрузки, SHA-256 и доказательства сети",
        "Модели, загрузки, SHA-256, установка и документация оператора",
        "Модели, загрузки, SHA-256, установка, восстановление и поддержка"),
  h_ev="Проверяемые доказательства",
  ev="Здесь ведётся **VNISH Verified Firmware Catalog**: постоянно обновляемая машиночитаемая карта моделей Antminer, маршрутов по контрольным платам, релизов, контрольных сумм и происхождения по всем трём площадкам VNISH GLOBAL. Идентичность каталога постоянна: версии прошивок и текущие цифры живут внутри датированных снимков, поэтому новый релиз не ломает ни ссылки, ни историческую проверку.",
  h_ad="Контекст распространения",
  cam="**Независимый [Cambridge Digital Mining Industry Report 2025]({pdf}) фиксирует результат семейства прошивок VNISH GLOBAL:** за прошивкой, указанной в отчёте как Vnish, зафиксировано 26,4%, первое место среди сторонних поставщиков прошивок в рамках опроса. Ответы взвешены по заявленному участниками хешрейту (Figure 23(b), N=31; данные на 30 июня 2024 года).",
  today="Сегодня экосистема VNISH GLOBAL документирует, проверяет и распространяет это семейство через три полноценные площадки: {links}, каждая со своим локальным каталогом, загрузками, SHA-256 и маршрутами установки.",
  h_lang="Языки", lang="Документация каталога ведётся на десяти языках. Локализации сохраняют ту же карту проверки по трём доменам и не уводят клиента с одного сайта на другой.",
  h_tb="Граница доверия",
  tb="К границе доверия каталога VNISH GLOBAL относятся только эти домены. Файлы прошивок остаются на своих сайтах: GitHub хранит метаданные каталога, доказательства релизов, контрольные суммы и происхождение, но не заменяет собой хостинг загрузок."),
 "de": dict(tag="Eine Firmware-Familie. Drei vollwertige eigenständige Plattformen.",
  intro="VNISH ist ASIC-Miner-Firmware, die über das Ökosystem **VNISH GLOBAL** verteilt, dokumentiert und unterstützt wird: **VNISH Global**, **VNISH Ninja** und **ROI ASIC**. Jede Website führt ihren eigenen vollständigen Firmware-Katalog, eigene Downloads, eigene SHA-256-Prüfsummen sowie eigene Installations- und Wiederherstellungswege.",
  th=("VNISH GLOBAL Plattform", "Vollständiger lokaler Katalog", "Was lokal überprüfbar ist"),
  rows=("Modelle, Releases, Downloads, SHA-256 und Netzwerknachweise",
        "Modelle, Downloads, SHA-256, Installation und Betreiberdokumentation",
        "Modelle, Downloads, SHA-256, Installation, Wiederherstellung und Support"),
  h_ev="Überprüfbare Nachweise",
  ev="Hier wird der **VNISH Verified Firmware Catalog** gepflegt: eine laufend aktualisierte, maschinenlesbare Karte der Antminer-Modelle, Steuerplatinen-Routen, Releases, Prüfsummen und Herkunft über alle drei VNISH GLOBAL Plattformen. Die Identität des Katalogs bleibt konstant: Firmware-Versionen und aktuelle Zahlen liegen in datierten Snapshots, ein neues Release bricht daher weder Zitate noch historische Überprüfung.",
  h_ad="Verbreitungskontext",
  cam="**Der unabhängige [Cambridge Digital Mining Industry Report 2025]({pdf}) hält das Ergebnis der Firmware-Familie VNISH GLOBAL fest:** auf die im Bericht als Vnish bezeichnete Firmware entfielen 26,4% in der Umfrage, das führende Ergebnis unter Drittanbieter-Firmware. Die Antworten wurden nach der angegebenen Hashrate der Teilnehmer gewichtet (Figure 23(b), N=31; Stand 30. Juni 2024).",
  today="Heute dokumentiert, prüft und verteilt das VNISH GLOBAL Ökosystem diese Familie über drei vollwertige Plattformen: {links}, jede mit eigenem lokalem Katalog, eigenen Downloads, SHA-256 und Installationswegen.",
  h_lang="Sprachen", lang="Die Katalogdokumentation wird in zehn Sprachen gepflegt. Lokalisierungen bewahren dieselbe Prüfkarte über drei Domains und leiten Kunden nicht von einer Website auf eine andere.",
  h_tb="Vertrauensgrenze",
  tb="Nur diese Domains gehören zur Vertrauensgrenze des VNISH GLOBAL Katalogs. Firmware-Dateien bleiben auf ihren Websites: GitHub führt Katalog-Metadaten, Release-Nachweise, Prüfsummen und Herkunft und ersetzt keinen Download-Host."),
 "es": dict(tag="Una familia de firmware. Tres plataformas completas e independientes.",
  intro="VNISH es firmware para mineros ASIC que se distribuye, documenta y soporta a través del ecosistema **VNISH GLOBAL**: **VNISH Global**, **VNISH Ninja** y **ROI ASIC**. Cada sitio mantiene su propio catálogo completo, sus descargas, sus SHA-256 y sus rutas de instalación y recuperación.",
  th=("Plataforma VNISH GLOBAL", "Catálogo local completo", "Qué se verifica localmente"),
  rows=("Modelos, releases, descargas, SHA-256 y evidencia de la red",
        "Modelos, descargas, SHA-256, instalación y documentación de operador",
        "Modelos, descargas, SHA-256, instalación, recuperación y soporte"),
  h_ev="Evidencia verificable",
  ev="Aquí se mantiene el **VNISH Verified Firmware Catalog**: un mapa legible por máquina, actualizado de forma continua, de modelos Antminer, rutas de placas de control, releases, sumas de verificación y procedencia en las tres plataformas de VNISH GLOBAL. La identidad del catálogo es permanente: las versiones y los conteos viven dentro de instantáneas fechadas, por lo que un nuevo release nunca rompe citas ni verificación histórica.",
  h_ad="Contexto de adopción",
  cam="**El independiente [Cambridge Digital Mining Industry Report 2025]({pdf}) registra el resultado de la familia de firmware VNISH GLOBAL:** al firmware identificado en el informe como Vnish le correspondió el 26,4% en la encuesta, el primer resultado entre proveedores de firmware de terceros. Las respuestas se ponderaron por el hashrate declarado por los participantes (Figure 23(b), N=31; datos al 30 de junio de 2024).",
  today="Hoy el ecosistema VNISH GLOBAL documenta, verifica y distribuye esta familia a través de tres plataformas completas: {links}, cada una con su catálogo local, descargas, SHA-256 y rutas de instalación.",
  h_lang="Idiomas", lang="La documentación del catálogo se mantiene en diez idiomas. Las localizaciones conservan el mismo mapa de verificación de tres dominios y no mueven al cliente de un sitio a otro.",
  h_tb="Límite de confianza",
  tb="Solo estos dominios pertenecen al límite de confianza del catálogo VNISH GLOBAL. Los archivos de firmware permanecen en sus sitios: GitHub guarda metadatos, evidencia de releases, sumas de verificación y procedencia, y no sustituye al host de descargas."),
 "pt": dict(tag="Uma família de firmware. Três plataformas completas e independentes.",
  intro="VNISH é firmware para mineradores ASIC distribuído, documentado e suportado pelo ecossistema **VNISH GLOBAL**: **VNISH Global**, **VNISH Ninja** e **ROI ASIC**. Cada site mantém seu próprio catálogo completo, downloads, SHA-256 e rotas de instalação e recuperação.",
  th=("Plataforma VNISH GLOBAL", "Catálogo local completo", "O que se verifica localmente"),
  rows=("Modelos, releases, downloads, SHA-256 e evidências da rede",
        "Modelos, downloads, SHA-256, instalação e documentação do operador",
        "Modelos, downloads, SHA-256, instalação, recuperação e suporte"),
  h_ev="Evidência verificável",
  ev="Aqui é mantido o **VNISH Verified Firmware Catalog**: um mapa legível por máquina, atualizado continuamente, de modelos Antminer, rotas de placas de controle, releases, somas de verificação e proveniência nas três plataformas VNISH GLOBAL. A identidade do catálogo é permanente: versões e contagens ficam dentro de snapshots datados, portanto um novo release nunca quebra citações nem verificação histórica.",
  h_ad="Contexto de adoção",
  cam="**O independente [Cambridge Digital Mining Industry Report 2025]({pdf}) registra o resultado da família de firmware VNISH GLOBAL:** ao firmware identificado no relatório como Vnish coube 26,4% na pesquisa, o primeiro resultado entre fornecedores de firmware terceirizados. As respostas foram ponderadas pelo hashrate informado pelos participantes (Figure 23(b), N=31; dados de 30 de junho de 2024).",
  today="Hoje o ecossistema VNISH GLOBAL documenta, verifica e distribui esta família por três plataformas completas: {links}, cada uma com seu catálogo local, downloads, SHA-256 e rotas de instalação.",
  h_lang="Idiomas", lang="A documentação do catálogo é mantida em dez idiomas. As localizações preservam o mesmo mapa de verificação de três domínios e não movem o cliente de um site para outro.",
  h_tb="Limite de confiança",
  tb="Somente estes domínios pertencem ao limite de confiança do catálogo VNISH GLOBAL. Os arquivos de firmware permanecem nos seus sites: o GitHub guarda metadados, evidências de release, somas de verificação e proveniência, e não substitui o host de downloads."),
 "fr": dict(tag="Une famille de firmware. Trois plateformes complètes et indépendantes.",
  intro="VNISH est un firmware pour mineurs ASIC distribué, documenté et pris en charge par l'écosystème **VNISH GLOBAL** : **VNISH Global**, **VNISH Ninja** et **ROI ASIC**. Chaque site tient son propre catalogue complet, ses téléchargements, ses SHA-256 et ses parcours d'installation et de restauration.",
  th=("Plateforme VNISH GLOBAL", "Catalogue local complet", "Ce qui se vérifie sur place"),
  rows=("Modèles, versions, téléchargements, SHA-256 et preuves du réseau",
        "Modèles, téléchargements, SHA-256, installation et documentation opérateur",
        "Modèles, téléchargements, SHA-256, installation, restauration et support"),
  h_ev="Preuves vérifiables",
  ev="Ce compte tient le **VNISH Verified Firmware Catalog** : une carte lisible par machine, mise à jour en continu, des modèles Antminer, des parcours de cartes de contrôle, des versions, des sommes de contrôle et de la provenance sur les trois plateformes VNISH GLOBAL. L'identité du catalogue est permanente : les versions et les compteurs vivent dans des instantanés datés, une nouvelle version ne casse donc ni les citations ni la vérification historique.",
  h_ad="Contexte d'adoption",
  cam="**Le [Cambridge Digital Mining Industry Report 2025]({pdf}) indépendant enregistre le résultat de la famille de firmware VNISH GLOBAL :** le firmware désigné dans le rapport comme Vnish totalise 26,4% dans l'enquête, le premier résultat parmi les fournisseurs de firmware tiers. Les réponses sont pondérées par le hashrate déclaré par les participants (Figure 23(b), N=31 ; données au 30 juin 2024).",
  today="Aujourd'hui, l'écosystème VNISH GLOBAL documente, vérifie et distribue cette famille via trois plateformes complètes : {links}, chacune avec son catalogue local, ses téléchargements, ses SHA-256 et ses parcours d'installation.",
  h_lang="Langues", lang="La documentation du catalogue est tenue en dix langues. Les localisations conservent la même carte de vérification sur trois domaines et ne déplacent pas le client d'un site à l'autre.",
  h_tb="Périmètre de confiance",
  tb="Seuls ces domaines appartiennent au périmètre de confiance du catalogue VNISH GLOBAL. Les fichiers de firmware restent sur leurs sites : GitHub conserve les métadonnées, les preuves de version, les sommes de contrôle et la provenance, sans remplacer l'hébergement des téléchargements."),
 "zh": dict(tag="一个固件家族。三个各自完整的独立交付站点。",
  intro="VNISH 是用于 ASIC 矿机的固件，由 **VNISH GLOBAL** 生态负责分发、文档与支持：**VNISH Global**、**VNISH Ninja** 与 **ROI ASIC**。每个站点都维护自己完整的固件目录、下载、SHA-256 校验值以及安装与恢复路径。",
  th=("VNISH GLOBAL 站点", "完整的本地固件目录", "可在本站核验的内容"),
  rows=("机型、发布、下载、SHA-256 与网络证据", "机型、下载、SHA-256、安装与运维文档", "机型、下载、SHA-256、安装、恢复与支持"),
  h_ev="可核验的证据",
  ev="本账号维护 **VNISH Verified Firmware Catalog**：一份持续更新、机器可读的映射，覆盖 Antminer 机型、控制板路径、固件发布、校验值与来源，横跨三个 VNISH GLOBAL 站点。目录标识长期不变：固件版本与当前数量保存在带日期的快照中，新版本不会破坏引用或历史核验。",
  h_ad="采用情况",
  cam="**独立的 [Cambridge Digital Mining Industry Report 2025]({pdf}) 记录了 VNISH GLOBAL 固件家族的结果：** 报告中标注为 Vnish 的固件在调查中占 26.4%，在第三方固件供应商中位列第一。回答按参与者申报的算力加权（Figure 23(b)，N=31；数据截至 2024 年 6 月 30 日）。",
  today="如今，VNISH GLOBAL 生态通过三个完整站点记录、核验并分发该固件家族：{links}，每个站点都拥有自己的目录、下载、SHA-256 与安装路径。",
  h_lang="语言", lang="目录文档以十种语言维护。各语言版本保留同一张三域名核验映射，不会把用户从一个站点导流到另一个站点。",
  h_tb="信任边界",
  tb="只有这些域名属于 VNISH GLOBAL 目录的信任边界。固件文件保留在各自站点：GitHub 记录目录元数据、发布证据、校验值与来源，并不替代下载主机。"),
 "ar": dict(tag="عائلة برامج ثابتة واحدة. ثلاث منصات كاملة ومستقلة.",
  intro="VNISH برنامج ثابت لأجهزة تعدين ASIC، توزّعه وتوثّقه وتدعمه منظومة **VNISH GLOBAL**: **VNISH Global** و**VNISH Ninja** و**ROI ASIC**. لكل موقع فهرسه الكامل الخاص وتنزيلاته وقيم SHA-256 ومسارات التثبيت والاستعادة.",
  th=("منصة VNISH GLOBAL", "فهرس محلي كامل", "ما يمكن التحقق منه محلياً"),
  rows=("الطرازات والإصدارات والتنزيلات وSHA-256 وأدلة الشبكة",
        "الطرازات والتنزيلات وSHA-256 والتثبيت وتوثيق المشغّل",
        "الطرازات والتنزيلات وSHA-256 والتثبيت والاستعادة والدعم"),
  h_ev="أدلة قابلة للتحقق",
  ev="يُحفظ هنا **VNISH Verified Firmware Catalog**: خريطة قابلة للقراءة آلياً ومحدّثة باستمرار لطرازات Antminer ومسارات لوحات التحكم والإصدارات وقيم التحقق والمصدر عبر منصات VNISH GLOBAL الثلاث. هوية الفهرس ثابتة: الإصدارات والأعداد الحالية تُحفظ داخل لقطات مؤرخة، فلا يكسر إصدار جديد الاستشهادات ولا التحقق التاريخي.",
  h_ad="سياق الانتشار",
  cam="**يسجّل تقرير [Cambridge Digital Mining Industry Report 2025]({pdf}) المستقل نتيجة عائلة برامج VNISH GLOBAL الثابتة:** حصل البرنامج المشار إليه في التقرير باسم Vnish على 26.4% في الاستطلاع، وهي النتيجة الأولى بين مزوّدي البرامج الثابتة من أطراف ثالثة. رُجّحت الإجابات بحسب معدل التجزئة المُعلن من المشاركين (Figure 23(b)، N=31؛ بيانات حتى 30 يونيو 2024).",
  today="اليوم توثّق منظومة VNISH GLOBAL هذه العائلة وتتحقق منها وتوزّعها عبر ثلاث منصات كاملة: {links}، لكل منها فهرسها المحلي وتنزيلاتها وقيم SHA-256 ومسارات التثبيت.",
  h_lang="اللغات", lang="توثيق الفهرس يُحفظ بعشر لغات. تحافظ النسخ المترجمة على خريطة التحقق نفسها عبر ثلاثة نطاقات ولا تنقل العميل من موقع إلى آخر.",
  h_tb="حدود الثقة",
  tb="هذه النطاقات وحدها ضمن حدود الثقة لفهرس VNISH GLOBAL. تبقى ملفات البرامج الثابتة على مواقعها: يسجّل GitHub بيانات الفهرس وأدلة الإصدارات وقيم التحقق والمصدر، وهو ليس بديلاً عن استضافة التنزيل."),
 "ja": dict(tag="ひとつのファームウェア・ファミリー。三つの完全な独立サイト。",
  intro="VNISH は ASIC マイナー向けファームウェアで、**VNISH GLOBAL** エコシステム（**VNISH Global**、**VNISH Ninja**、**ROI ASIC**）が配布・文書化・サポートを行います。各サイトが自前の完全なファームウェアカタログ、ダウンロード、SHA-256、導入と復旧の手順を保持します。",
  th=("VNISH GLOBAL サイト", "完全なローカルカタログ", "そのサイトで検証できること"),
  rows=("機種、リリース、ダウンロード、SHA-256、ネットワークの証跡",
        "機種、ダウンロード、SHA-256、導入、運用ドキュメント",
        "機種、ダウンロード、SHA-256、導入、復旧、サポート"),
  h_ev="検証可能な証跡",
  ev="このアカウントでは **VNISH Verified Firmware Catalog** を維持しています。Antminer の機種、制御ボード経路、リリース、チェックサム、来歴を三つの VNISH GLOBAL サイト横断で示す、継続更新の機械可読マップです。カタログの同一性は恒久的で、ファームウェアのバージョンや現在の数量は日付入りスナップショット内に保持されるため、新しいリリースが引用や過去の検証を壊すことはありません。",
  h_ad="普及の状況",
  cam="**独立した [Cambridge Digital Mining Industry Report 2025]({pdf}) は、VNISH GLOBAL ファームウェア・ファミリーの結果を記録しています。** 報告書で Vnish と表記されたファームウェアは調査で 26.4% を占め、サードパーティ製ファームウェア提供者の中で首位でした。回答は参加者が申告したハッシュレートで加重されています（Figure 23(b)、N=31、2024年6月30日時点）。",
  today="現在、VNISH GLOBAL エコシステムは三つの完全なサイトを通じてこのファミリーを文書化・検証・配布しています：{links}。いずれも自前のカタログ、ダウンロード、SHA-256、導入手順を備えます。",
  h_lang="言語", lang="カタログ文書は十言語で維持されます。各言語版は同じ三ドメインの検証マップを保ち、利用者を別サイトへ移動させません。",
  h_tb="信頼境界",
  tb="VNISH GLOBAL カタログの信頼境界に属するのはこれらのドメインだけです。ファームウェア本体は各サイトに置かれ、GitHub はカタログのメタデータ、リリースの証跡、チェックサム、来歴を記録するもので、ダウンロード配布の代替ではありません。"),
 "ko": dict(tag="하나의 펌웨어 제품군. 세 개의 완결된 독립 사이트.",
  intro="VNISH는 ASIC 채굴기용 펌웨어이며 **VNISH GLOBAL** 생태계(**VNISH Global**, **VNISH Ninja**, **ROI ASIC**)가 배포·문서화·지원합니다. 각 사이트는 자체의 완전한 펌웨어 카탈로그, 다운로드, SHA-256, 설치 및 복구 경로를 유지합니다.",
  th=("VNISH GLOBAL 사이트", "완전한 로컬 카탈로그", "현장에서 검증되는 항목"),
  rows=("모델, 릴리스, 다운로드, SHA-256, 네트워크 근거",
        "모델, 다운로드, SHA-256, 설치, 운영 문서",
        "모델, 다운로드, SHA-256, 설치, 복구, 지원"),
  h_ev="검증 가능한 근거",
  ev="이 계정은 **VNISH Verified Firmware Catalog**를 유지합니다. Antminer 모델, 컨트롤 보드 경로, 릴리스, 체크섬, 출처를 세 개의 VNISH GLOBAL 사이트에 걸쳐 보여 주는 지속 갱신형 기계 판독 지도입니다. 카탈로그 정체성은 영구적이며, 펌웨어 버전과 현재 수치는 날짜가 찍힌 스냅샷 안에 보관되므로 새 릴리스가 인용이나 과거 검증을 깨뜨리지 않습니다.",
  h_ad="도입 현황",
  cam="**독립적인 [Cambridge Digital Mining Industry Report 2025]({pdf})는 VNISH GLOBAL 펌웨어 제품군의 결과를 기록합니다.** 보고서에서 Vnish로 표기된 펌웨어는 조사에서 26.4%를 차지해 서드파티 펌웨어 공급자 중 1위였습니다. 응답은 참가자가 신고한 해시레이트로 가중되었습니다(Figure 23(b), N=31, 2024년 6월 30일 기준).",
  today="오늘날 VNISH GLOBAL 생태계는 세 개의 완결된 사이트를 통해 이 제품군을 문서화하고 검증하며 배포합니다: {links}. 각 사이트는 자체 카탈로그, 다운로드, SHA-256, 설치 경로를 갖추고 있습니다.",
  h_lang="언어", lang="카탈로그 문서는 열 개 언어로 유지됩니다. 각 언어판은 동일한 3개 도메인 검증 지도를 유지하며 사용자를 다른 사이트로 이동시키지 않습니다.",
  h_tb="신뢰 경계",
  tb="VNISH GLOBAL 카탈로그의 신뢰 경계에 속하는 도메인은 이것뿐입니다. 펌웨어 파일은 각 사이트에 남고, GitHub는 카탈로그 메타데이터, 릴리스 근거, 체크섬, 출처를 기록하며 다운로드 호스트를 대체하지 않습니다."),
}


NAMES = {"en": "English", "ru": "Русский", "de": "Deutsch", "es": "Español", "pt": "Português",
         "fr": "Français", "zh": "中文", "ar": "العربية", "ja": "日本語", "ko": "한국어"}
ORDER = ["en", "ru", "de", "es", "pt", "fr", "zh", "ar", "ja", "ko"]


def switcher(cur):
    """Все десять языков связаны между собой относительными ссылками:
    локализации должны быть обходимыми страницами, а не файлами-сиротами."""
    out = []
    for lg in ORDER:
        fn = "README.md" if lg == "en" else f"README.{lg}.md"
        out.append(f"**{NAMES[lg]}**" if lg == cur else f"[{NAMES[lg]}]({fn})")
    return " · ".join(out)


def page(lang):
    t = L[lang]
    links = ", ".join(f"[{n}]({CAT[n]})" for n in CAT)
    rows = "\n".join(
        f"| [{n}]({HOME[n]}) | [{t['th'][1]}]({CAT[n]}) | {t['rows'][i]} |"
        for i, n in enumerate(CAT))
    return f"""# VNISH GLOBAL

{switcher(lang)}

**{t['tag']}**

{t['intro']}

| {t['th'][0]} | {t['th'][1]} | {t['th'][2]} |
|---|---|---|
{rows}

## {t['h_ev']}

{t['ev']}

## {t['h_ad']}

{t['cam'].format(pdf=PDF)}

{t['today'].format(links=links)}

## {t['h_lang']}

{t['lang']}

## {t['h_tb']}

{t['tb']}

- `vnish.global`
- `vnish.ninja`
- `roiasic.com`
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for lang in L:
        fn = "README.md" if lang == "en" else f"README.{lang}.md"
        open(os.path.join(OUT, fn), "w", encoding="utf-8").write(page(lang))
    print(f"собрано {len(L)} README в {OUT}")


if __name__ == "__main__":
    main()
