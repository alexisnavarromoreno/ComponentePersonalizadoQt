from setuptools import setup
 
setup(
    name='Componente Personalizado',
    packages=['Componente Personalizado'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='GNU GENERAL PUBLIC LICENSE', # La licencia que tenga tu paquete
    description='Componente personalizado para formulario Qt',
    author='Alexis Navarro Moreno',
    author_email='alexisnm.1990@gmail.com',
    url='https://github.com/alexisnavarromoreno/ComponentePersonalizadoQt/tree/main', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/alexisnavarromoreno/ComponentePersonalizadoQt/archive/refs/tags/0.1.tar.gz', # Te lo explico a continuación
    keywords='formulario Qt animado', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)
