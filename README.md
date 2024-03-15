<H2>Task Manager</H2>
<H3>Interface function description</H3>
<p style="color:blue"> <font size="3">During the development process, it's crucial to consider the user's perspective. Functions should be extensively used to modularize the code and improve readability. Incorporating data verification functions helps ensure the reliability of input. Testing should be repeated multiple times to identify and rectify any issues. Additionally, adding colors enhances the user experience, making the operation screen more friendly and intuitive.</font></p>  

### Admin Function Diagram


```mermaid
flowchart TD
    A[Welcome Page] -->B{Menu Selection function};
    B-- r --> C[Registering a user];
    B-- a --> D[Adding a Task];
    B-- va --> E[View All Tasks];
    B-- vm --> F[View My Tasks];
    B-- gr --> G[Generate Report];
    B-- ds --> H[Display Statistics];
    B-- c --> I[Change Password];
    B -- e --> J[Exit];
    C -- f --> C2(reg_user);
    D -- f --> D2(add_task);
    E -- f --> E2(view_all);
    F -- f --> F2(view_mine);
    G -- f --> G2(generate_task_overview);
    G2 -- f --> G3(generate_user_overview)
    G3 -- f --> G4(display_report_file_time)
    H -- f--> H2(display_statistics);
    I -- f --> I2(change_password)

  ```




<img width="500" alt="tm_1" src="https://github.com/Yami3366/finalCapstone/assets/159643271/24454b9c-cdd8-48ef-a8cc-9dcbf2246010">  

<p style="color:blue"> <font size="3">User Admin logon</font></p>
<img width="500" alt="tm_2" src="https://github.com/Yami3366/finalCapstone/assets/159643271/17b80f8c-db85-4df5-a4f4-b9bd9702631b">
<p style="color:blue"> <font size="3">choice r- registering a user</font></p>
<img width="500" alt="tm_3" src="https://github.com/Yami3366/finalCapstone/assets/159643271/81e02ff4-7222-471b-9a63-b878c5dd6081">
<p style="color:blue"> <font size="3">choice a- Adding a task</font></p>
<img width="500" alt="tm_4" src="https://github.com/Yami3366/finalCapstone/assets/159643271/d0f1bac5-6197-41e1-8524-00c4f80bc2ba">
<p style="color:blue"> <font size="3">choice va- View Add Tasks </font></p>
<img width="500" alt="tm_5" src="https://github.com/Yami3366/finalCapstone/assets/159643271/cccae6fc-bf9c-4d31-956d-5ca02b275893">
<p style="color:blue"> <font size="3">choice vm- View My Tasks </font></p>
<img width="500" alt="tm_6" src="https://github.com/Yami3366/finalCapstone/assets/159643271/6ea1a6ab-4e8e-4ecc-9159-9534a0d78fec">
<p style="color:blue"> <font size="3">choice gr- Generate Report </font></p>
<img width="500" alt="tm_7" src="https://github.com/Yami3366/finalCapstone/assets/159643271/f6d582b4-be62-4b2a-8c1d-fa65d8132caa">
<p style="color:blue"> <font size="3">choice ds- Display Statistics Report </font></p>
<img width="500" alt="tm_8" src="https://github.com/Yami3366/finalCapstone/assets/159643271/e685674d-5bad-430a-9734-1cef3e8da8e9">
<p style="color:blue"> <font size="3">Task Statistics Report</font></p>

<img width="500" alt="tm_10" src="https://github.com/Yami3366/finalCapstone/assets/159643271/eeb8b1ee-0452-4054-88c3-5b8e095eee99">


<p style="color:blue"> <font size="3">choice c- Chagne Password </font></p>
<img width="500" alt="tm_12" src="https://github.com/Yami3366/finalCapstone/assets/159643271/a080825c-1bb6-4d55-9bc4-a1250c88c850">
<p style="color:blue"> <font size="3">Passord vaild function </font></p>
<img width="500" alt="tm_11" src="https://github.com/Yami3366/finalCapstone/assets/159643271/34de7cbb-e948-48c5-b8e4-8fd713ce0a4d">
### Normal User Function Diagram  

```mermaid
flowchart TD
    A[Welcome Page] -->B{Menu Selection function};
    B-- va --> C[View All Tasks];
    B-- vm --> D[View My Tasks];
    B-- cp --> E[Change Password];
    B-- e --> F[Exit];
    C -- f --> G(view_all);
    D -- f --> H(view_mine)
    E -- f --> I(change_password)
  ```

<p style="color:blue"> <font size="3">User Kiki logon ,display user limited function</font></p>
<img width="500" alt="tm_13" src="https://github.com/Yami3366/finalCapstone/assets/159643271/ea601118-431b-4c31-8d5d-82eafd2d8d69">
<p style="color:blue"> <font size="3">Choic va -  Views All Tasks </font></p>
<img width="500" alt="tm_14" src="https://github.com/Yami3366/finalCapstone/assets/159643271/3a8fcf72-28bc-4ca3-9ef3-bf34347c2dd2">
<p style="color:blue"> <font size="3">Choic vm -  Views My Tasks and reassign Task to BoBo </font></p>
<img width="500" alt="tm_15" src="https://github.com/Yami3366/finalCapstone/assets/159643271/93dff33f-15fc-4d3a-a35f-c2ba911228ce">
<p style="color:blue"> <font size="3">Choic vm -  Views My Tasks again ,display no task. </font></p>
<img width="500" alt="tm_16" src="https://github.com/Yami3366/finalCapstone/assets/159643271/2b9d9b34-c932-4ea5-b8e1-464298003e90">
<p style="color:blue"> <font size="3">Choic vm -  Views All Tasks again ,display no task. </font></p>





  
