from string import Template
import json


websiteData = json.loads(open("website-settings.json").read())


# "application" | "unit" | "topic" -> HTML (for the sidebar)
def build_sidebar(titleHref, titleName, overviewHref, overviewName, overviewIcon, buttonsContent, smallWidth):
	sidebarButtons = """ <div class="sidebar\""""
	#unit view must have smaller width
	if(smallWidth):
		sidebarButtons+= """id="unit">"""
	sidebarButtons+="""<div class="logo-details"><div class="logo_name">
	<i class='bx bx-home-smile'></i> </div> """


	sidebarButtons += """ <a href=""" + titleHref +""" class="logo_name">""" + titleName + """</a> <!--NAME-->
			<i class='bx bx-chevron-right' id="btn" ></i>
			</div>
			
			<ul class="nav-list">
			
			<li>
				<a href=""" + overviewHref + """ aria-label="Go to""" + overviewName + """\">
					<i class=""" + overviewIcon + """></i>
					<span class="links_name">""" + overviewName + """</span>
				</a>
				<span class="tooltip">""" + overviewName + """</span>
			</li>"""

		

	sidebarButtons += buttonsContent

    #end div tags and script for sidebar
	sidebarButtons += """</ul> </div> 
	        <script>
		    let sidebar = document.querySelector(".sidebar");
		    let closeBtn = document.querySelector("#btn");
		
		    closeBtn.addEventListener("click", ()=>{
			    sidebar.classList.toggle("open");
			    menuBtnChange();//calling the function(optional)
		    });
		
		    searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
			    sidebar.classList.toggle("open");
			    menuBtnChange(); //calling the function(optional)
		    });
		
		    // following are the code to change sidebar button(optional)
		    function menuBtnChange() {
			    if(sidebar.classList.contains("open")){
				    closeBtn.classList.replace("bx-chevron-right", "bx-chevron-left");//replacing the iocns class
			    }
			    else {
				    closeBtn.classList.replace("bx-chevron-left","bx-chevron-right");//replacing the iocns class
			    }
		    }
	        </script>"""
	
	return sidebarButtons



def build_mobile_sidebar(titleHref, titleName, overviewHref, overviewName, mobileButtonsContent):
	mobileSidebarButtons = """ <div id="mySidebar" class="collapsedSidebar">
			<a href=""" + titleHref + """ class="homeMobile"> """ + titleName +"""</a> <!--NAME-->
		  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×&nbsp;</a>
			<a href=""" + overviewHref + """>""" + overviewName + """</a>"""
	
	mobileSidebarButtons += mobileButtonsContent
		

	mobileSidebarButtons += """ </div>

		<div class="openbutton">
			<button class="openbtn"  onclick="openNav()">☰ Open Sidebar</button> 
		</div> 
		  
		<script>
		  function openNav() {
			document.getElementById("mySidebar").style.width = "100%";
			document.getElementById("content").style.marginLeft = "100%";
		  }
		  
		  function closeNav() {
			document.getElementById("mySidebar").style.width = "0";
			document.getElementById("content").style.marginLeft= "0";
		  }
		</script>
		"""

	return mobileSidebarButtons

def build_head_html(title):
	headHtml = """<head>
	<!-- logo on tab-->
	
	<meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- import font -->
	<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200&display=swap" rel="stylesheet">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>	
	
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="description" content="Discrete Math for Computer Science">
	<meta name="author" content="Mia Minnes">

	<title>""" + title + """</title>

	<!-- Bootstrap Core CSS -->
	<link rel="stylesheet" href="css/bootstrap.min.css">

	<!---Collapsible Menu-->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

	<link rel="stylesheet" href="css/sidebarStyle.css">
	<link rel="stylesheet" href="css/style.css">


	<!-- icons for side menu -->
	<link rel='stylesheet' href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' >

	<link rel="shortcut icon" href="../resources/images/musicalChairs.png">
</head>
	"""
	return headHtml


# Application
appData = json.loads(open("applications.json").read())
appButtonsContent = ""
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	appButtonsContent += "<li>"
	appButtonsContent += """<a href= \"""" + file + """\" aria-label="Go to """ + i + """ ">"""
	appButtonsContent += """<i><p class="icons">&nbsp;&nbsp;""" + appData[i]['Icon'] + """</p></i>"""
	appButtonsContent += """<span class="links_name"> """ + i + """</span>"""
	appButtonsContent += "</a>"
	appButtonsContent += """<span class="tooltip"> """ + i + """</span>"""
	appButtonsContent += "</li>\n"

appMobileButtonsContent = ""
for i in appData:
	file = i.replace(" ", "-").lower()+".html"
	appMobileButtonsContent += """<a href= \"""" + file + """\">""" + i + """</a>\n"""



# Outcome
outcomeData = json.loads(open("outcomes.json").read())
outcomeButtonsContent = ""
for big in outcomeData:
	for med in outcomeData[big]['Children']:
		#only put icon in sidebar of 2nd tier topics that have children 
		if(bool(outcomeData[big]['Children'][med]['Children'])):
			outcomeButtonsContent += "<li>"
			outcomeButtonsContent += """<a href= \"""" +outcomeData[big]['Children'][med]['file'] + """\" aria-label="Go to """ + med + """ ">"""
			outcomeButtonsContent += """<i><p class="icons">&nbsp;&nbsp;""" + outcomeData[big]['Children'][med]['Icon'] + """</p></i>"""
			outcomeButtonsContent += """<span class="links_name"> """ + med + """</span>"""
			outcomeButtonsContent += "</a>"
			outcomeButtonsContent += """<span class="tooltip"> """ + med + """</span>"""
			outcomeButtonsContent += "</li>"

outcomeMobileButtonsContent = ""
for big in outcomeData:
	for med in outcomeData[big]['Children']:
		#only put icon in sidebar of 2nd tier topics that have children 
		if(bool(outcomeData[big]['Children'][med]['Children'])):
			outcomeMobileButtonsContent += """<a href= \"""" + outcomeData[big]['Children'][med]['file'] + """\"">""" + med + """</a>"""


# Unit
unitData = json.loads(open("unit-settings.json").read())
#unit buttons will have an additional assignments button
unitButtonsContent = """<li>
			<a href=\"assignments.html\" aria-label="Go to Assignments\">
			<i class='bx bxs-detail'></i>
			<span class="links_name"> Assignments </span>
			</a>
			<span class="tooltip">Assignments</span>
			</li>"""

for i in range(0,len(unitData)):
	unitButtonsContent += "<li>"
	unitButtonsContent += """<a href= " """ + 'unit'+str(i+1) + """.html" aria-label="Go to """ + unitData[i]['header'] + """ ">"""
	unitButtonsContent += """<i><p class="icons">&nbsp;&nbsp;&nbsp;&nbsp;""" + str(i+1) + """</p></i>"""
	unitButtonsContent += """<span class="links_name"> """ + unitData[i]['header'] + """</span>"""
	unitButtonsContent += "</a>"
	unitButtonsContent += """<span class="tooltip"> """ + unitData[i]['header'] + """</span>"""
	unitButtonsContent += "</li>"

unitMobileButtonsContent = ""
for i in range(0,len(unitData)):
	unitMobileButtonsContent += """<a href= \"""" + 'unit'+str(i+1) + """.html\"">""" + unitData[i]['header'] + """</a>"""




sidebars = {
	'application': build_sidebar("index.html", websiteData['Global Class Name'], "overviewApplication.html", "Overview", "'bx bxs-shapes'", appButtonsContent,bool(False)),
	'topic': build_sidebar("index.html", websiteData['Global Class Name'], "overviewTopic.html", "Overview", "'bx bxs-shapes'", outcomeButtonsContent, bool(False)),
	'unit': build_sidebar("courseInfo.html", websiteData['Course Offering Title'], "overviewCalendar.html", "Calendar", "'bx bx-calendar'", unitButtonsContent, bool(True)),
}

mobile_sidebars = {
	'application': build_mobile_sidebar("index.html", websiteData['Global Class Name'], "overviewApplication.html", "Overview", appMobileButtonsContent),
	'topic': build_mobile_sidebar("index.html", websiteData['Global Class Name'], "overviewTopic.html", "Overview", outcomeMobileButtonsContent),
	'unit': build_mobile_sidebar("courseInfo.html", websiteData['Course Offering Title'], "overviewCalendar.html", "Calendar", unitMobileButtonsContent),
}

head_html = {
	'application': build_head_html(websiteData['Global Class Name']),
	'topic': build_head_html(websiteData['Global Class Name']),
	'unit': build_head_html(websiteData['Course Offering Title']),
	'others': build_head_html(websiteData['Global Class Name'])
}

def create_unit_boxes():
	for i in range (1, len(unitData)+1):
		index = i-1

    	#set appropriate variables for top calendar information section and title 
		weekNumber = i
		info=""
		if('CalendarInfo' in unitData[index]):
			info=unitData[index]['CalendarInfo']
		
		boxString =""
		#box heading and subheading/description
		boxString += """<div class="box"> \n"""
		boxString += "<h2> Week " + str(weekNumber) + "</h2>"
		boxString += "<p> " + info + "</p>"
		boxString += "<hr>"
		
		#list begins
		boxString += """<div class="column"> <dl> \n"""
		
		#Learning Materials (link to contents on weekly page)
		boxString += """<dt><i class='bx bxs-right-arrow'></i>Learning Materials</dt> \n"""
		
		#pdfs
		if('pdfs' in unitData[index]):
			for pdf in unitData[index]['pdfs']:
				pdfjsID = pdf['name'].replace(" ", "-")
				boxString += "<dd> <a href=\"unit""" +str(i)+ """.html#"""+ pdfjsID+"""\" >""" + pdf['name'] + """</a></dd>\n"""
				
		#embeds
		if('embed' in unitData[index]):
			for embed in unitData[index]['embed']: 
				embedID = embed['name'].replace(" ", "-")
				boxString += "<dd> <a href=\"unit""" +str(i)+ """.html#"""+ embedID+"""\" >""" + embed['name'] + """</a></dd>\n"""

    	#Assignments
		boxString += """<dt><i class='bx bxs-right-arrow'></i>Assignments</dt> \n"""
		if ('Assignments' in unitData[index]):
			for assignment in unitData[index]['Assignments']:
				#if link is provided use that link
				link = ""
				if('link' in assignment):
					link=assignment['link']
            	#else refer to the assignments page (default)
				else:
					cardID = assignment['name'].replace(" ", "").lower()
					link="""assignments.html#collapse"""+cardID
				
				boxString += "<dd> <a href=\"""" +link+ """\">"""+assignment['name']+"""</a></dd>\n"""  
		
		boxString += "</dl>"
		
		boxString += "</div>"
		
		boxString += "</div><br><br>"
	
	return boxString




def create_outcome_boxes():
	boxString = ""
	#big for loop begin
	for i in outcomeData:

		boxString += """<div class="box"> \n"""

		boxString += "<h2>" + outcomeData[i]['Icon'] + i + "</h2>"
		boxString += "<p> Description: " + outcomeData[i]['Description'] + "</p>"
		boxString += "<hr>"

		boxString += """<div class="column"> <dl> \n"""

		
		for j in outcomeData[i]['Children']:

			#add link to page of 2nd tier children with subtopics (only link to pages of 2nd tier children with content)
			if(bool(outcomeData[i]['Children'][j]['Children'])):
				boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href=\"""" + outcomeData[i]['Children'][j]['file'] + """\" >""" + j + """</a></dt> \n"""
				
			else:
				boxString += """<dt><i class='bx bx-subdirectory-right' ></i><a href="javascript:void(0)" >""" + j + """</a></dt> \n"""
			

			#list children of 2nd tier children (subtopics under outcomes, these will be included on the webpage for the outcomes as PDFs and menu options)
			if(bool(outcomeData[i]['Children'][j]['Children'])):
				for k in outcomeData[i]['Children'][j]['Children']:
					boxString += "<dd>" + k + "</dd>\n"
				
				boxString += "</dl>"

		boxString += "</div>"

		boxString += "</div><br><br>"
	return boxString

def create_application_boxes():
	boxString = """<div class="box"> \n"""
	#big for loop begin
	for i in appData:
		file = i.replace(" ", "-").lower()+".html"
		boxString += """<h2> <i style= "font-size: 75%;" class='bx bxs-chevron-right-square'></i> <a href= \"""" + file + """\" style="color: #182B49; text-decoration: none; font-size: 75%; font-weight: normal;" >""" + i + """</a></h2>"""
	boxString += "</div><br><br>"
	return boxString






def create_site_variables():
	return {
		'applicationSidebar': sidebars['application'],
		'outcomeSidebar': sidebars['topic'],
		'unitSidebar': sidebars['unit'],

		'applicationMobileSidebar': mobile_sidebars['application'],
		'outcomeMobileSidebar': mobile_sidebars['topic'],
		'unitMobileSidebar': mobile_sidebars['unit'],

		'applicationHead': head_html['application'],
		'outcomeHead': head_html['topic'],
		'unitHead': head_html['unit'],
		'othersHead': head_html['others'],

		'unitBoxes': create_unit_boxes(),
		'outcomeBoxes': create_outcome_boxes(),
		'applicationBoxes': create_application_boxes()
		# and many more to come ...
	}

site_variables = create_site_variables()