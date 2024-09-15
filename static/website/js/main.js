(function($) {

	"use strict";


  // Form
	var contactForm = function() {
		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					name: "required",
					subject: "required",
					email: {
						required: true,
						email: true
					},
					message: {
						required: true,
						minlength: 5
					}
				},
				messages: {
					name: "Please enter your name",
					subject: "Please enter your subject",
					email: "Please enter a valid email address",
					message: "Please enter a message"
				},
				/* submit via ajax */
				
				submitHandler: function(form) {		
					var $submit = $('.submitting'),
						waitText = 'Submitting...';

					$.ajax({   	
				      type: "POST",
				      url: "php/sendEmail.php",
				      data: $(form).serialize(),

				      beforeSend: function() { 
				      	$submit.css('display', 'block').text(waitText);
				      },
				      success: function(msg) {
		               if (msg == 'OK') {
		               	$('#form-message-warning').hide();
				            setTimeout(function(){
		               		$('#contactForm').fadeIn();
		               	}, 1000);
				            setTimeout(function(){
				               $('#form-message-success').fadeIn();   
		               	}, 1400);

		               	setTimeout(function(){
				               $('#form-message-success').fadeOut();   
		               	}, 8000);

		               	setTimeout(function(){
				               $submit.css('display', 'none').text(waitText);  
		               	}, 1400);

		               	setTimeout(function(){
		               		$( '#contactForm' ).each(function(){
											    this.reset();
											});
		               	}, 1400);
			               
			            } else {
			               $('#form-message-warning').html(msg);
				            $('#form-message-warning').fadeIn();
				            $submit.css('display', 'none');
			            }
				      },
				      error: function() {
				      	$('#form-message-warning').html("Something went wrong. Please try again.");
				         $('#form-message-warning').fadeIn();
				         $submit.css('display', 'none');
				      }
			      });    		
		  		} // end submitHandler

			});
		}
	};
	contactForm();

})(jQuery);

document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.getElementById('dropdown');
    const sections = document.querySelectorAll('.form-section');
    const imageBox = document.getElementById('imageBox');
    const infoText = document.getElementById('infoText');

    const images = {
        Afforestion: staticUrl + 'website/images/afforestation.jpg',
        Aviation: staticUrl + 'website/images/aviation.jpg',
        Bio: staticUrl + 'website/images/biomethane.jpg',
        EVchar: staticUrl + 'website/images/evchar.jpg',
        solar: staticUrl + 'website/images/solar.jpg'
    };

    const infoTexts = {
        none:' <h5>Ready to Get Started?</h5><strong>Register for free </strong> and start using our Beta carbon calculator today! <br>For companies seeking a <strong>customized carbon management solution, contact us</strong> to discuss your specific needs and explore how our expertise can help you achieve your sustainability goals. <br><br><strong>Together, lets build a more sustainable future, one footprint at a time!</strong>',
        Afforestion: '<strong>Project Type:</strong> Creates new forests on degraded land. Trees absorb and store carbon dioxide as they grow.<br><strong>Data Points for Calculating Credits:</strong><br><li>Number of trees planted successfully and their survival rate over a specific period (usually 5-30 years)</li><li>Species of trees planted - Faster-growing trees may generate credits quicker, but slower-growing natives might store more carbon long-term.</li><li>Soil quality and local climate - These factors influence how much carbon a tree can store.</li>',
        Aviation: '<strong>Challenges:</strong> Aviation is a significant contributor to greenhouse gas emissions, particularly through CO2 and Nitrous Oxide (N2O) emissions at high altitudes. Current technology limitations make direct on-board emission reduction difficult.<br><strong>Potential Solutions:</strong><br><strong><li>Sustainable Aviation Fuel (SAF):</strong> SAF is a biofuel derived from renewable sources like plant oils or waste biomass. Using SAF can significantly reduce lifecycle emissions compared to traditional jet fuel.</li><li><strong>Carbon Offsetting Projects:</strong> Airlines can invest in projects like afforestation or renewable energy to offset their emissions. However, the effectiveness of offsets for aviation is debated due to the complex nature of its impact.</li><strong>Data Points for Calculating Credits (SAF):</strong><br>Volume of SAF used compared to traditional jet fuel.Lifecycle emission reduction factor of the specific SAF blend used. (Verified by relevant bodies)',
        Bio: '<strong>Process:</strong> Bio-methanization breaks down organic waste (like agricultural waste, food scraps, or sewage sludge) through anaerobic digestion, producing biogas rich in methane (CH4). This biogas can be upgraded to biomethane, a renewable energy source similar to natural gas but with lower greenhouse gas emissions.<br><strong>Potential for Credits:</strong> Biomethane displaces fossil-based natural gas, reducing CO2 emissions. Additionally, capturing and utilizing methane from waste decomposition avoids its release into the atmosphere, which has a much higher warming potential than CO2.</br><strong>Data Points for Calculating Credits:</strong><li>Volume of biomethane produced from waste compared to the volume of fossil fuel natural gas displaced.</li><li>Methane capture efficiency of the bio-methanization plant.</li>',
        EVchar: '<strong>Project Type:</strong> Installs EV charging stations powered by renewable energy sources (solar panels on-site or purchase of renewable energy certificates - RECs).<br><strong>Data Points for Calculating Credits:</strong><li>Electricity consumption per charging session</li> <li>Number of charging sessions per year</li> <li>Emission factor of the avoided grid electricity (kg CO2/kWh)</li>',
        solar: '<strong>Project Type:</strong> Installs solar panels that generate clean electricity, displacing electricity generation from fossil fuels.<br><strong>Data Points for Calculating Credits:</strong><li>Capacity of the solar power plant (in Megawatts - MW)</li><li>Local electricity grid mix (percentage of electricity generated from fossil fuels)</li><li>Lifetime of the solar panels (usually 20-25 years)</li>'
    };
    infoText.innerHTML = infoTexts.none;
    dropdown.addEventListener('change', () => {
        const selectedValue = dropdown.value;

        sections.forEach(section => {
            const inputs = section.querySelectorAll('input');
            inputs.forEach(input => input.value = '');
        });

        if (images[selectedValue]) {
            imageBox.style.backgroundImage = `url(${images[selectedValue]})`;
        }
        if (infoTexts[selectedValue]) {
            infoText.innerHTML = infoTexts[selectedValue];
        }

        sections.forEach(section => {
            if (section.id === selectedValue) {
                section.classList.remove('hidden');
            } else {
                section.classList.add('hidden');
            }
        });

        if (selectedValue !== "none") {
            document.getElementById("calculateBtnWrapper").classList.remove("hidden");
        } else {
            document.getElementById("calculateBtnWrapper").classList.add("hidden");
        }
    });
});

document.getElementById("calculateBtn").addEventListener("click", function () {
    var selectedValue = document.getElementById("dropdown").value;
    var calculation = 0;

    switch (selectedValue) {
        case "Afforestion":
            var treesnumber = parseFloat(document.getElementById("treesnumber").value) || 0;
            var avglife = parseFloat(document.getElementById("avglife").value) || 0;
            var susrate = parseFloat(document.getElementById("susrate").value) || 0;
            calculation = ((treesnumber * susrate/100)*50)/1000;
            break;
        case "Aviation":
            var avivol = parseFloat(document.getElementById("avivol").value) || 0;
            calculation = (avivol * 0.7*3)/1000;
            break;
        case "Bio":
            var biocap = parseFloat(document.getElementById("biocap").value) || 0;
            var biolif = parseFloat(document.getElementById("biolif").value) || 0;
            var biometh = parseFloat(document.getElementById("biometh").value) || 0;
            calculation = biocap *(56-25)+biocap*0.9*25;
            break;
        case "EVchar":
            var elecon = parseFloat(document.getElementById("elecon").value) || 0;
            var numchar = parseFloat(document.getElementById("numchar").value) || 0;
            var emission = parseFloat(document.getElementById("Emission").value) || 0;
            calculation = ((elecon * numchar)/1000) * 365;
            break;
        case "solar":
            var solcap = parseFloat(document.getElementById("solcap").value) || 0;
            var solloc = parseFloat(document.getElementById("solloc").value) || 0;
            var sollif = parseFloat(document.getElementById("sollif").value) || 0;
            calculation = solcap * 1000 * sollif;
            break;
    }

    document.getElementById("ans").value = "Calculated Value: " + calculation.toFixed(2)+" Tons of carbon credits that may be sold out";
    document.getElementById("ans").style.display = "block";
});






const modal = document.getElementById('modal');
const modalBody = document.getElementById('modal-body');

const contentMap = {
    'challenges': `
        <h2>The Challenges of the Existing VCM</h2>
        <p>The paper outlines the current limitations of the VCM, including issues like double counting, limited accessibility, and high transaction costs.</p>
    `,
    'solution': `
        <h2>Introducing Sustainogram's Three-Pronged Solution</h2>
        <p>We detail our innovative platform that offers:</p>
        <ul>
            <li>A decentralized exchange for efficient and transparent carbon credit trading.</li>
            <li>A secure and verifiable meta registry for carbon offset validation.</li>
            <li>A comprehensive ecosystem connecting stakeholders and regulators.</li>
        </ul>
    `,
    'benefits': `
        <h2>Benefits for All Stakeholders</h2>
        <p>The paper explores the advantages of Sustainogram for various players in the carbon market, including businesses, project developers, buyers, consumers, and regulatory bodies.</p>
    `,
    'advantage': `
        <h2>A Competitive Advantage</h2>
        <p>We compare Sustainogram to existing solutions, highlighting how our blockchain-based platform offers a distinct advantage.</p>
    `,
    'opportunity': `
        <h2>Market Opportunity</h2>
        <p>The paper analyzes the promising market potential for a decentralized carbon credit trading platform.</p>
    `,
    'future': `
        <h2>Building a Sustainable Future</h2>
        <p>We conclude by outlining our business model, development timeline, and the expertise of our team behind Sustainogram, showcasing our vision for a more sustainable future.</p>
    `
};

function showModal(contentKey) {
    modalBody.innerHTML = contentMap[contentKey];
    modal.style.display = 'flex';
}

function closeModal() {
    modal.style.display = 'none';
}

document.querySelectorAll('.cta-button').forEach(button => {
    button.addEventListener('click', () => {
        window.location.href = 'https://www.linkedin.com';
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.content-section').forEach(section => {
    observer.observe(section);
});

document.querySelectorAll('.card').forEach(card => {
    observer.observe(card);
});
