from html import escape

html_body = f"""
     <!DOCTYPE html>
     <html>
     <head>
         <style>
             pre {{
                 background-color: #f4f4f4;
                 border: 1px solid #ddd;
                 border-radius: 4px;
                 padding: 10px;
                 overflow: auto;
             }}
             code {{
                 color: #d63384;
                 font-family: monospace;
             }}
         </style>
     </head>
     <body>
         <h1>Alert!</h1>
         <p><strong>Error Message:</strong></p>
         <p><code>{escape(errors[0]["error_message"])}</code></p>
         <hr>
         <p><strong>Context:</strong></p>
         <pre><code>{escape(errors[0]["context"])}</code></pre>
     </body>
     </html>
     """
