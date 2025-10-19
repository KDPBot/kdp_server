# Railway Documentation

This file contains the complete Railway documentation structure and content for LLM consumption.

# Overview
Source: https://docs.railway.com/overview

# About Railway
Source: https://docs.railway.com/overview/about-railway

Railway is a modern cloud deployment platform designed to help developers deploy instantly and scale apps effortlessly. Learn about our platform.



## Deploying on Railway

Point Railway to your deployment source and let the platform handle the rest.

#### Flexible Deployment Sources

- **Code Repositories**: With or without Dockerfiles. Railway will build an OCI compliant image based on what you provide.
- **Docker Images**: Directly from Docker Hub, GitHub Container Registry, GitLab Container Registry, Microsoft Container Registry, or Quay.io. We support public and private image registries.

#### Hassle-Free Setup

- **Sane Defaults**: Out of the box, your project is deployed with sane defaults to get you up and running as fast as possible.
- **Configuration Tuning**: When you're ready, there are plenty of knobs and switches to optimize as needed.

## Development Lifecycle

Software development extends far beyond code deployment. Railway's feature set is tailor-made, and continuously evolving, to provide the best developer experience we can imagine.

#### Configuration Management

- **Variables & Secrets**: Easily manage configuration values and sensitive data with variable management tools.

#### Environment and Workflow

- **Environment Management**: Create both static and ephemeral environments to create workflows that complement your processes.
- **Orchestration & Tooling**: Build Railway into any workflow using our CLI or API.

#### Deployment Monitoring

- **Observability**: Keep a pulse on your deployments with Railway's built-in observability tools.

## Operational Model

Railway operates with an emphasis on reliability and transparency. We utilize a combination of alerting tools, internal systems, and operational procedures to maintain high uptime. Read more about product philosophy and maturity here.

## Book a Demo

Looking to adopt Railway for your business? We'd love to chat! Click here to book some time with us.


# The Basics
Source: https://docs.railway.com/overview/the-basics

Learn about the core concepts of Railway.



## In a Nutshell

- **Dashboard** - Main entrypoint for all projects under your account.
- **Project** - A collection of services under the same network.
  - **Project Settings** - Contains all project-level settings.
- **Service** - A target for a deployment source (e.g. Web Application).
  - **Service Variables** - A collection of configurations and secrets.
  - **Backups** - A collection of backups for a service.
  - **Service Metrics** - Rundown of metrics for a service.
  - **Service Settings** - Contains all service-level settings.
- **Deployment** - Built and deliverable unit of a service.
- **Volumes** - Persistent storage solution for services.
  - **Volume Metrics** - Rundown of metrics for volumes (e.g. disk usage over time).
  - **Volume Settings** - Contains all volume-level settings.

## Dashboard / Projects

Your main entrypoint to Railway where all your projects are shown in the order they where last opened.

Projects contain your services and environments.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785111/docs/the-basics/dashboard_ycmxnk.png"
alt="Screenshot of the Railway dashboard"
layout="responsive"
width={1305} height={735} quality={100} />

## Project / Project Canvas

A project represents a capsule for composing infrastructure in Railway. You can think of a project as an application stack, a service group, or even a collection of service groups.

Services within a project are automatically joined to a private network scoped to that project.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785173/docs/the-basics/project_canvas_dxpzxe.png"
alt="Screenshot of the project canvas"
layout="responsive"
width={1365} height={765} quality={100} />

### Project Settings

This page contains all the project level settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785164/docs/the-basics/project_settings_ghwzih.png"
alt="Screenshot of the project settings page"
layout="responsive"
width={1365} height={765} quality={100} />

Some of the most commonly used project settings are -

- Transfer Project - Transfer your project between workspaces.

- Environments - Manage various settings regarding environments.

- Members - Add or remove members to collaborate on your project.

- Danger - Remove individual services or delete the entire project.

## Services

A Railway service is a deployment target for your deployment source. Deployment sources can be code repositories or Docker Images. Once you create a service and choose a source, Railway will analyze the source, build a Docker image (if the source is a code repository), and deploy it to the service.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785212/docs/the-basics/services_zuyl56.png"
alt="Screenshot of the project canvas with services highlighted"
layout="responsive"
width={1365} height={765} quality={100} />

Out of the box, your service is deployed with a set of default configurations which can be overridden as needed.

### Service Variables

Service Variables provide a powerful way to manage configuration and secrets across services in Railway.

You can configure variables scoped to services. These variables are specific to each service and are not shared across the project by default.

If you want to access variables from this service in another service within the same project, you need to utilize a Reference Variable.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785219/docs/the-basics/service_variables_galkry.png"
alt="Screenshot of the service variables tab"
layout="responsive"
width={1365} height={765} quality={100} />

### Backups

If your service has a volume attached, this is where you can manage backups.

Backups are incremental and Copy-on-Write, we only charge for the data exclusive to them, that aren't from other snapshots or the volume itself.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785142/docs/the-basics/backups_fdx09o.png"
alt="Screenshot of the service backups tab"
layout="responsive"
width={1365} height={765} quality={100} />

From here you can perform the following actions -

- Create a backup - Manually create a backup of the volume with a press of a button.

- Delete a backup - Remove a backup from the list via the backup's 3-dot menu.

- Lock a backup - Prevent a backup from being deleted via the backup's 3-dot menu.

- Restore a backup - Click the Restore button on the backup.

- Modify the backup schedule - Click the Edit schedule button on the header to make changes to the schedule.

### Service Metrics

Service Metrics provide an essential overview of CPU, memory, and network usage for a given service.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785153/docs/the-basics/service_metrics_dcbfms.png"
alt="Screenshot of the service metrics tab"
layout="responsive"
width={1365} height={770} quality={100} />

### Service Settings

This tab contains all the service level settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785132/docs/the-basics/service_settings_lnyql0.png"
alt="Screenshot of the service settings tab"
layout="responsive"
width={1365} height={765} quality={100} />

Some of the most commonly used service settings are -

- Source - Here you can configure the deployment source, which can be either a GitHub repository with a specific branch or an image with optional credentials.

- Networking - Generate a Railway-provided domain or add your own custom one.

- Custom Build Command - Here you can configure a custom build command if you need to overwrite the default.

- Custom Start Command - Here, you can configure a custom start command if you need to overwrite the default.

## Deployments

Deployments involve building and delivering your Service.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785123/docs/the-basics/deployment_l0trj8.png"
alt="Screenshot of a service open with a deployment highlighted"
layout="responsive"
width={1365} height={790} quality={100} />

## Volumes

Volumes are a feature that allows services on Railway to maintain persistent data.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785187/docs/the-basics/volumes_yom2km.png"
alt="Screenshot of the project canvas with a volume highlighted"
layout="responsive"
width={1365} height={765} quality={100} />

### Volume Metrics

Volume Metrics show the amount of data stored in the volume and its maximum capacity.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785205/docs/the-basics/volume_metrics_thv60n.png"
alt="Screenshot of the volume metrics tab"
layout="responsive"
width={1365} height={826} quality={100} />

### Volume Settings

This tab contains all the volume centric settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785195/docs/the-basics/volume_settings_kirpdn.png"
alt="Screenshot of the volume settings tab"
layout="responsive"
width={1365} height={826} quality={100} />

Some of the most commonly used volume settings are -

- Mount path - The absolute path where the volume will be mounted within the deployed service.

- Volume Size - Displays the current volume capacity and offers the option to expand it if your plan permits.

- Wipe Volume - This action wipes all data in the volume and then redeploys the connected service.

## What Next?

If you've read enough for now and are ready to get started, we suggest checking out either of these two resources next -

- Quick Start guide to deploy a To Do app from a template.

- Guides section to dive into how things work.

If you want to go deeper, click the Next button below to head to the next section - Advanced Concepts.


# Best Practices
Source: https://docs.railway.com/overview/best-practices

Learn the best practices to maximize performance, efficiency, and scalability of your apps on Railway.

To keep consistency we want each topic to follow the same convention -

- What?
- When?
- Do X.
- Why?
- Image.
*/}

Railway is a highly versatile platform, offering various ways to use it, though some may be less optimal than others for most use cases. These topics aim to help you maximize both your potential and the platform's capabilities.

## Use Private Networking When Possible

Private networking allows services within a project to communicate internally without the need to expose them publicly, while also providing faster communication and increased throughput.

When configuring environment variables in your service to reference domains or URLs of other services, ensure you use the private versions of these variables, such as RAILWAY_PRIVATE_DOMAIN or DATABASE_URL.

Using the private network enables communication between services within the same project without incurring service-to-service egress costs, which is particularly beneficial when interacting with databases or other internal services.

<Image src="https://res.cloudinary.com/railway/image/upload/v1725659271/docs/best-practices/use_private_networking_son2xp.png"
alt="screenshot of a service showing the use of private networking via reference variables"
layout="intrinsic"
width={1048} height={818} quality={100} />

<span style={{'font-size': "0.9em"}}>Screenshot showing the use of the RAILWAY_PRIVATE_DOMAIN variable being used via referencing.</span>

## Deploying Related Services Into the Same Project

In Railway, a project serves as a container for organizing infrastructure. It can encompass an application stack, a group of services, or even multiple service groups.

If you're about to head back to the dashboard to deploy another service like a database, there's a quicker way - look for the Create button at the top right of the Project canvas. This shortcut allows you to add new services directly to your current project.

There are a few key advantages of keeping related services within the same project -

- **Private networking** - The private network is scoped to a single environment within a project, having all related services within a single project will allow you to use private networking for faster networking along with no egress fees for service-to-service communication.

- **Project clutter** - Deploying a new service or database as an entire project will quickly become overwhelming and clutter your dashboard.

- **Variable management** - Variables can be referenced between services within a project, reducing redundancy and making it easier to manage instead of having to manually copy variables between services.

<Image src="https://res.cloudinary.com/railway/image/upload/v1725659271/docs/best-practices/related_services_in_a_project_mtxuis.png"
alt="screenshot of the project canvas showing multiple linked services"
layout="intrinsic"
width={1048} height={818} quality={100} />

<span style={{'font-size': "0.9em"}}>Screenshot showing related services within a project and their connection links.</span>

## Use Reference Variables Where Applicable

Reference variables allow you to dynamically reference another variable, either from a variable set on the current service or from another service in the same project.

Rather than manually copying, pasting, and hard-coding variables like a public domain or those from another service, you can use reference variables to build them dynamically. Example VITE_BACKEND_HOST=${{Backend.RAILWAY_PUBLIC_DOMAIN}}

This approach is better than hard-coding variables, as it keeps your variable values in sync. Change your public domain? The variable updates. Change your TCP proxy? The variable updates.

<Image src="https://res.cloudinary.com/railway/image/upload/v1725659271/docs/best-practices/use_reference_variables_h8qtik.png"
alt="screenshot of a service showing the use of reference variables"
layout="intrinsic"
width={1048} height={818} quality={100} />

<span style={{'font-size': "0.9em"}}>Screenshot showing a reference variable used to reference the Backend's domain.</span>


# Advanced Concepts
Source: https://docs.railway.com/overview/advanced-concepts

A guide that outlines the advanced concepts of Railway.



## Build and Deploy Options

Out of the box, many defaults are applied to builds and deployments. However, there are several ways to tailor things to your project spec.

### Build Options

Railway uses <a href="https://railpack.com" target="_blank">Railpack</a> to build and deploy your code with zero configuration. When your needs require adjustments to the defaults, we make it easy to configure things like install, build, and start commands.

### Deploy Options

Deployments are created with some default options that can be overridden. Some of the options available are -

- **Replicas**: By default, your deployment will go out with a single instance. With replicas, you have the ability to scale up your deployment instances.
- **Deployment Region**: Deployments by default are pushed to your preferred region.
- **Scheduled Executions**: Your deployment will be run once by default. If the service is intended to be a scheduled task of sorts, you can create a cron schedule.
- **App Sleep**: Services are serverful and always-on. You can control this behavior, to spin down resources when they're not being used, by enabling App Sleep.

## Networking

Networking can be tricky and time-consuming. We wanted to provide the best-in-class experience when it came to wiring things up. There are two basic ways we accomplish this.

### Private Networking

Private Networking is a feature within Railway that will open network communication through a IPv6 wireguard mesh only accessible to your Railway services within a project.

All projects have private networking enabled and services are assigned a DNS name under the railway.internal domain. This DNS name resolves to the internal IPv6 address of the services in a project.

### Railway-Provided Domains

With the click of a button, Railway will expose your service to the internet and provide you with a domain. In order to make this work, you must configure your application appropriately to ensure we know the port it is listening on. Instructions for how to do this can be found in the Public Networking guide.

#### Custom Domains

If you have a custom domain, you can easily add it to your Railway service.

## Integration Tools

A <a href="https://docs.railway.com/guides/cli" target="_blank">CLI</a> and an <a href="https://docs.railway.com/guides/public-api" target="_blank">API</a> are available to wire your Railway projects into any workflow.

### CLI

The Railway Command Line Interface (CLI) lets you interact with your Railway project from the command line, allowing you to do things like:

- Trigger deployments programmatically.
- Run services locally using environment variables from your Railway project.
- Create new Railway projects from the Terminal.
- Deploy <a href="https://docs.railway.com/reference/templates" target="_blank">templates</a>.

### Public API

The Railway <a href="https://docs.railway.com/guides/public-api" target="_blank">public API</a> is built with GraphQL and is the same API that powers the Railway dashboard. Similar to the CLI, you can interact with your Railway project programmatically by communicating with the API.

## Environments

Railway environments give you an isolated instance of all databases and services in a project. You can use them to

- Have development environments for each team member that are identical to the production environment
- Have separate staging and production environments

Within a service and environment, you can specify which branch to auto-deploy to that environment when a change is merged.

## Observability

Any build or deployment logs emitted to standard output or standard error ( eg. console.log(...)) are captured by Railway so you can view or search for it later.

### Service Logs

Logs for a specific service deployment are available from a service's view in your project, useful when debugging build or deployment failures.

### Centralized Logs

Logs for all of the services in a project can be viewed together in our Observability tool within a project. This is useful for debugging more general problems that may span multiple services.



# Guides
Source: https://docs.railway.com/guides

# Projects
Source: https://docs.railway.com/guides/projects

A guide to managing projects on Railway.

Click on a project card to go to the project canvas:

<Image src="https://res.cloudinary.com/railway/image/upload/v1644620884/docs/ProjectPage_new_pa52tp.png"
alt="Screenshot of Project Canvas"
layout="responsive"
width={1377} height={823} quality={100} />

Project settings can be managed through the Settings button at the top right of the project canvas.

## Managing Project Info

A project's name and description can be changed from the General tab within a project's settings.

The project id can also be retrieved here.

## Deleting a Project

A project can be deleted by selecting the Delete Project button in the Danger tab. Deleting a project will delete all services, environments, and deployments associated with the project.

Specific services within a project can also be deleted from this page.

## Inviting Members

Invite members to access a project through the Members tab in your Project Settings.

You can invite a member by sending an invitation to their email address, or by generating an invite link to send to them directly.

Click here to view the scope definitions for permissions.

### Invite by Email

Invite a new member via email by specifying their email address and scope of permissions, then click Invite.

This will send an email to the address specified containing a link to join your project.

### Invite by Link

Each project generates a project invite link. To invite someone via a link:

1. Select the desired invited member scope
2. Copy link and send to the invitee

## Transferring Projects

Depending on your plan, you can transfer Projects to other users or Teams.

#### Hobby User to Hobby User

To transfer a project from one Hobby User to another Hobby User, you must first add the user as a member in the project.

You can then transfer the project to the new member by selecting the three dots next to the user and choosing Transfer Ownership.

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917785/docs/project-transfer_iz4myn.png"
alt="Screenshot of Project Transfer Menu"
layout="intrinsic"
width={411} height={253} quality={80} />

The transferee receives an email requesting to transfer the project.

#### Hobby User to Team || Team to Team

You can transfer a Project in your Hobby workspace to a Team (or between Teams) in which you are an Admin. Inside your project, visit the Settings page and click the Transfer Project button to view the project transfer modal.

<Image src="https://res.cloudinary.com/railway/image/upload/v1692378671/project-transfer_iukfwb.png" alt="Project Transfer" layout="responsive" height={968} width={1240} />

Note: If you do not see the Transfer Project section in your Project Settings, you may not be an Admin of the Team to which you wish to transfer the Project. See the reference page for Teams for more information on team member permissions.

## Viewing Recent Activity

The activity feed shows all the changes that have been made to a project. This includes changes to services and volumes. You can click on a change to see everything that was committed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743121231/docs/recent-activity_g2hupm.png"
            alt="Commit activity feed"
            layout="responsive"
            width={1273} height={631} quality={100} />

## Updating Project Visibility

Projects are private by default and only accessible to members of the project. However, you can make your projects public to share in a read-only state by changing the visibility in project settings -

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743121306/docs/project-visiblity_ksafj3.png"
alt="Screenshot of Project Visibility Setting"
layout="intrinsic"
width={1273} height={451} quality={80} />


# Staged Changes
Source: https://docs.railway.com/guides/staged-changes

Discover how to use staged changes in Railway to deploy updates gradually.

It is important to be familiar with this flow as you explore the upcoming guides.

### What to Expect

As you create or update components within your project:

1. The number of staged changes will be displayed in a banner on the canvas
2. Staged changes will appear as purple in the UI

<Image src="https://res.cloudinary.com/railway/image/upload/v1743124823/docs/what-to-expect_geldie.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1400} height={720} quality={100} />

### Review and Deploy Changes

To review the staged changes, click the "Details" button in the banner. Here, you will see a diff of old and new values. You can discard a change by clicking the "x" to the right of the change.

You can optionally add a commit message that will appear in the activity feed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743123181/docs/changes_qn15ls.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1200} height={792} quality={100} />

Clicking "Deploy" will deploy all of the changes at once. Any services that are affected will be redeployed.

Holding the "Alt" key while clicking the "Deploy" button allows you to commit the changes without triggering a redeploy.

### Caveats

- Networking changes are not yet staged and are applied immediately
- Adding databases or templates will only affect the current environment. However, they do not yet create a commit in the history


# Services
Source: https://docs.railway.com/guides/services

A step by step guide to managing services on Railway.

_As you create and manage your services, your changes will be collected in a set of staged changes that you must review and deploy, in order to apply them._

## Creating a Service

Create a service by clicking the New button in the top right corner of your project canvas, or by typing new service from the **command palette**, accessible via CMD + K (Mac) or Ctrl + K(Windows).

<Image src="https://res.cloudinary.com/railway/image/upload/v1656640995/docs/CleanShot_2022-06-30_at_18.17.31_cl0wlr.gif"
alt="GIF of the Services view"
layout="responsive"
width={370} height={300} quality={100} />

Services on Railway can be deployed from a GitHub repository, a local directory, or a Docker image.

## Accessing Service Settings

To access a service's settings, simply click on the service tile from your project canvas and go to the Settings tab.

## Defining a Deployment Source

If you've created an empty service, or would like to update the source for a deployed service, you can do so in the Service settings.

Click on the service, go to the Settings tab, and find the **Service Source** setting.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743121798/docs/deployment-source_sir4mo.png"
alt="Screenshot of how to connect a service to a GitHub repo or Docker image"
layout="responsive"
width={1200} height={421} quality={80} />

### Deploying From a GitHub Repo

Define a GitHub repository as your service source by selecting Connect Repo and choosing the repository you'd like to deploy.

When a new commit is pushed to the linked branch, Railway will automatically build and deploy the new code.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743121857/docs/github-repo_z8qkst.png"
alt="Screenshot of a GitHub deployment trigger"
layout="responsive"
width={1200} height={371} quality={80} />

You must link your Railway account to GitHub, to enable Railway to connect to your GitHub repositories. <a href="https://github.com/apps/railway-app/installations/new" target="_blank">You can configure the Railway App in GitHub by clicking this link.</a>

### Deploying a Public Docker Image

To deploy a public Docker image, specify the path of the image when prompted in the creation flow.

Railway can deploy images from <a href="https://hub.docker.com/" target="_blank">Docker Hub</a>, <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry" target="_blank">GitHub Container Registry</a>, <a href="https://quay.io/" target="_blank">Quay.io</a>, or <a href="https://docs.gitlab.com/ee/user/packages/container_registry/">GitLab Container Registry</a>. Example paths -

Docker Hub:

- bitnami/redis

GitHub Container Registry:

- ghcr.io/railwayapp-templates/postgres-ssl:latest

GitLab Container Registry:

- registry.gitlab.com/gitlab-cicd15/django-project

Microsoft Container Registry:

- mcr.microsoft.com/dotnet/aspire-dashboard

Quay.io:

- quay.io/username/repo:tag

### Updating Docker Images

Railway automatically monitors Docker images for new versions. When an update is available, an update button appears in your service settings. If your image tag specifies a version (e.g., nginx:1.25.3), updating will stage the new version tag. For tags without versions (e.g., nginx:latest), Railway redeploys the existing tag to pull the latest image digest.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757369631/docs/screenshot-2025-09-08-18.09.17_rkxbqa.png"
alt="Screenshot of a Docker image update button"
layout="responsive"
width={681} height={282} quality={100} />

To enable automatic updates, configure the update settings in your service. You can specify an update schedule and maintenance window. Note that automatic updates trigger a redeployment, which may cause brief downtime (typically under 2 minutes) for services with attached volumes.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757369630/docs/screenshot-2025-09-08-18.12.09_u2jiz4.png"
alt="Screenshot of a auto update configuration"
layout="responsive"
width={836} height={684} quality={100} />

### Deploying a Private Docker Image

<Banner variant="info">
Private Docker registry deployments require the Pro plan.
</Banner>

To deploy from a private Docker registry, specify the path of the image when prompted in the creation flow, as well as authentication credentials (username, password) to the registry.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743197249/docs/source-image_gn52ff.png"
alt="GIF of the Services view"
layout="intrinsic"
width={1200} height={746} quality={100} />

If deploying an image from <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry" target="_blank">GitHub Container Registry</a>, provide a <a href="https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#authenticating-to-the-container-registry" target="_blank">personal access token (classic)</a>.

## Deploying From a Local Directory

Use the CLI to deploy a local directory to a service -

1. Create an Empty Service by choosing Empty Service during the service creation flow.
2. In a Terminal, navigate to the directory you would like to deploy.
3. Link to your Railway project using the railway link CLI command.
4. Deploy the directory using railway up. The CLI will prompt you to choose a service target, be sure to choose the empty service you created.

## Deploying a Monorepo

For information on how to deploy a Monorepo click here.

## Monitoring

Logs, metrics, and usage information is available for services and projects. Check out the monitoring guides for information on how to track this data.

## Changing the Service Icon

Customize your project canvas for easier readability by changing the service icon.

1. Right click on the service
2. Choose Update Info
3. Choose Icon
4. Begin typing to see a list of available icons, pulled from our <a href="https://devicons.railway.com/" target="_blank">devicons</a>service.

You can also access this configuration from the command palette.

## Approving a Deployment

If a member of a GitHub repo doesn't have a linked Railway account. Railway by default will not deploy any pushes to a connected GitHub branch within Railway.

Railway will then create a Deployment Approval within a Service prompting a user to determine if they want to deploy their commit or not.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724222405/CleanShot_2024-08-21_at_02.38.25_2x_vxurvb.png"
alt="screenshot of the deployment approval ui"
layout="responsive"
width={874} height={302} quality={100} />

Deploy the queued deployment by clicking the "Approve" button. You can dismiss the request by clicking the three dots menu and clicking "Reject".

## Storing Data

Every service has access to 10GB of ephemeral storage. If your service requires data to persist between deployments, or needs more than 10GB of storage, you should add a volume.

## Deleting a Service

Delete a service by opening the project's settings and scrolling to the danger section.


# Variables
Source: https://docs.railway.com/guides/variables

Learn how to use variables and secrets across services on Railway.

When defined, they are made available to your application as environment variables in the following scenarios:

- The build process for each service deployment.
- The running service deployment.
- The command invoked by railway run <COMMAND>
- The local shell via railway shell

In Railway, there is also a notion of configuration variables which allow you to control the behavior of the platform.

_Adding, updating, or removing variables, results in a set of staged changes that you must review and deploy, in order to apply them._

## Service Variables

Variables scoped to individual services can be defined by navigating to a service's "Variables" tab.

<Image src="https://res.cloudinary.com/railway/image/upload/c_scale,w_2026/v1678820924/docs/CleanShot_2023-03-14_at_12.07.44_2x_rpesxd.png"
alt="Screenshot of Variables Pane"
layout="responsive"
width={2026} height={933} quality={100} />

#### Define a Service Variable

From a service's variables tab, click on New Variable to enter your variable into a form field, or use the RAW Editor to paste the contents of your .env or json-formatted file.

### Suggested Variables

Your connected GitHub repository to your Service will automatically detect and suggest environment variables from .env files. This feature streamlines the setup process by populating your service variables at the click of a button. Railway scans the root directory of your repository for environment files and suggests their variables for import.

#### Supported .env File Patterns

Railway scans for the following .env file patterns in your repository's root directory:

- .env
- .env.example
- .env.local
- .env.production
...
- Or any other files matching the pattern .env.<suffix>

## Shared Variables

Shared variables help reduce duplication of variables across multiple services within the same project.

<Image src="https://res.cloudinary.com/railway/image/upload/v1669678393/docs/shared-variables-settings_vchmzn.png"
alt="Screenshot of Shared Variables Settings"
layout="responsive"
width={2402} height={1388} quality={100} />

#### Define a Shared Variable

From your Project Settings -> Shared Variables page, choose the Environment, enter the variable name and value, and click Add.

#### Use a Shared Variable

To use a shared variable, either click the Share button from the Project Settings -> Shared Variables menu and select the services with which to share, or visit the Variables tab within the service itself and click "Shared Variable".

Adding a shared variables to a service creates a Reference Variable in the service.

## Reference Variables

Reference variables are those defined by referencing variables in other services, shared variables, or even variables in the same service.

When using reference variables, you also have access to Railway-provided variables.

Railway's template syntax is used when defining reference variables.

### Referencing a Shared Variable

Use the following syntax to reference a shared variable:

- ${{ shared.VARIABLE_KEY }}

<Collapse slug="referencing-a-shared-variable-example" title="Example">
- You have a shared variable defined in your project called API_KEY, and you need to make the API key available to a service.  Go to the service's variables tab, and add a variable with the following value:
  - API_KEY=${{shared.API_KEY}}
</Collapse>

### Referencing Another Service's Variable

Use the following syntax to reference variables in another service:

- ${{SERVICE_NAME.VAR}}

<Collapse slug="referencing-another-services-variable-example" title="Example">
- You have a variable set on your database service called DATABASE_URL which contains the connection string to connect to the database.  The database service name is **Clickhouse**.

- You need to make this connection string available to another service in the project. Go to the service's variables that needs the connection string and add a variable with the following value:

  - DATABASE_URL=${{ Clickhouse.DATABASE_URL }}

- Your frontend service needs to make requests to your backend. You do not want to hardcode the backend URL in your frontend code. Go to your frontend service settings and add the Railway-provided variable for the backend URL

  - API_URL=https://${{ backend.RAILWAY_PUBLIC_DOMAIN }}

</Collapse>

### Referencing Variables in the Same Service

Use the following syntax to reference variables in the same service:

- ${{ VARIABLE_NAME }}

<Collapse slug="referencing-variables-in-the-same-service-example" title="Example">
- You have the variables needed to construct an API endpoint already defined in your service - BASE_URL and AUTH_PATH - and you would like to combine them to create a single variable.  Go to your service variables and add a new variable referencing other variables in the same service -
  - AUTH_ENDPOINT=https://${{ BASE_URL }}/${{ AUTH_PATH }}
</Collapse>

### Autocomplete Dropdown

The Railway dashboard provides an autocomplete dropdown in both the name and value fields to help create reference variables.

<Image src="https://res.cloudinary.com/railway/image/upload/c_scale,w_2000/v1678823846/docs/CleanShot_2023-03-14_at_12.56.56_2x_mbb6hu.png"
alt="Screenshot of Variables Pane"
layout="responsive"
width={2408} height={1150} quality={100} />

## Sealed Variables

Railway provides the ability to seal variable values for extra security. When a variable is sealed, its value is provided to builds and deployments but is never visible in the UI nor can it be retrieved via the API.

### Sealing a Variable

To seal an existing variable, click the 3-dot menu on the right-side of the variable and choose the "Seal" option.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743199483/docs/seal_ky7w4s.png"
alt="Seal an existing variable"
layout="responsive"
width={1200} height={552} quality={100} />

### Updating a Sealed Variable

Sealed variables can be updated by clicking the edit option in the 3-dot menu just like normal variables but they cannot be updated via the Raw Editor.

### Caveats

Sealed variables are a security-first feature and with that come some constraints:

- Sealed variables cannot be un-sealed.
- Sealed variable values are not provided when using railway variables or railway run via the CLI.
- Sealed variables are not copied over when creating PR environments.
- Sealed variables are not copied when duplicating an environment.
- Sealed variables are not copied when duplicating a service.
- Sealed variables are not shown as part of the diff when syncing environment changes.
- Sealed variables are not synced with external integrations.

## Railway-provided Variables

Railway provides many variables to help with development operations. Some of the commonly used variables include -

- RAILWAY_PUBLIC_DOMAIN
- RAILWAY_PRIVATE_DOMAIN
- RAILWAY_TCP_PROXY_PORT

For an exhaustive list, please check out the Variables Reference page.

## Multiline Variables

Variables can span multiple lines. Press Control + Enter (Cmd + Enter on Mac) in the variable value input field to add a newline, or simply type a newline in the Raw Editor.

## Using Variables in Your Services

Variables are made available at runtime as environment variables. To use them in your application, simply use the interface appropriate for your language to retrieve environment variables.

For example, in a node app -

#### Local Development

Using the Railway CLI, you can run your code locally with the environment variables configured in your Railway project.

- Ensure that you have the Railway CLI installed and linked to your project
- In your terminal, execute railway run <run command>
  -> for example, railway run npm run dev

Check out the CLI guide for more information on using the CLI.

## Using Variables in your Dockerfile

For information on how to use variables in your Dockerfile refer to the Dockerfiles guide.

## Import Variables from Heroku

You can import variables from an existing Heroku app using the command palette
on the service variables page. After connecting your Heroku account you can
select any of your Heroku apps and the config variables will be added to the current service and environment.

<Image src="/images/connect-heroku-account.png"
alt="Screenshot of connect Heroku account modal"
layout="responsive"
width={521} height={404} quality={100} />

## Using Doppler for Secrets Management

Our friends at Doppler maintain an integration that makes it easy to sync your secrets in Doppler to your project(s) in Railway.

You can get instructions on how to use Doppler with Railway on the <a href="https://docs.doppler.com/docs/railway" target="_blank">Doppler Docs
integration</a>.

## Code Examples

process.env.VARIABLE_NAME;


# Volumes
Source: https://docs.railway.com/guides/volumes

Use volumes on Railway to securely store and persist your data permanently.

<Image
    layout="intrinsic"
    quality={100}
    width={574}
    height={454}
    src="https://res.cloudinary.com/railway/image/upload/v1687540596/docs/volumes/volumes_su6dly.png"
    alt="Volume"
/>

## Creating A Volume

You can create a new volume through the Command Palette (âŒ˜K)
or by right-clicking the project canvas to bring up a menu:

<div style={{ display: 'flex', flexDirection: 'row', gap: '5px' }}>
    <div>
        <Image
            layout="intrinsic"
            quality={100}
            width={1118}
            height={476}
            src="https://res.cloudinary.com/railway/image/upload/v1687539860/docs/volumes/creating-volume-cmdk_w3wsv1.png"
            alt="Creating a volume via command palette"
        />
        <p style={{ marginTop: '-0.2em', fontSize: '0.8em', opacity: '0.6' }}>via command palette</p>
    </div>
    <div>
        <Image
            layout="intrinsic"
            quality={100}
            width={582}
            height={476}
            src="https://res.cloudinary.com/railway/image/upload/v1687539860/docs/volumes/creating-volume-menu_lqax4n.png"
            alt="Creating a volume via context menu"
        />
        <p style={{ marginTop: '-0.2em', fontSize: '0.8em', opacity: '0.6' }}>via right-click menu</p>
    </div>
</div>

When creating a volume, you will be prompted to select a service to connect the volume to:
<Image
    layout="intrinsic"
    quality={100}
    width={1148}
    height={524}
    src="https://res.cloudinary.com/railway/image/upload/v1687542048/docs/volumes/connect-volume-to-service_ao4s5h.png"
    alt="Connect volume to service"
/>

You must configure the mount path of the volume in your service:
<Image
    layout="intrinsic"
    quality={100}
    width={1136}
    height={400}
    src="https://res.cloudinary.com/railway/image/upload/v1687542048/docs/volumes/mount-point_kedfak.png"
    alt="Connect volume to service"
/>

## Using the Volume

The volume mount point you specify will be available in your service as a directory to which you can read/write. If you mount a volume to /foobar, your application will be able to access it at the absolute path /foobar.

### Relative Paths

Nixpacks, the default buildpack used by Railway, puts your application files in an /app folder at the root of the container. If your application writes to a directory at a relative path, and you need to persist that data on the volume, your mount path should include the app path.

For example, if your application writes data to ./data, you should mount the volume to /app/data.

### Provided Variables

Attaching a Volume to a service will automatically make these environment variables available
to the service at runtime:

- RAILWAY_VOLUME_NAME: Name of the volume (e.g. foobar)
- RAILWAY_VOLUME_MOUNT_PATH: Mount path of the volume (e.g. /foobar)

You do not need to define these variables on the service, they are automatically set by Railway at runtime.

### Volume Availability

Volumes are mounted to your service's container when it is started, not during build time.

If you write data to a directory at build time, it will not persist on the volume, even if it writes to the directory to which you have mounted the volume.

**Note:** Volumes are not mounted during pre-deploy time, if your pre-deploy command attempts to read or write data to a volume, it should be done as part of the start command.

Volumes are not mounted as overlays.

### Permissions

Volumes are mounted as the root user. If you run an image that uses a non-root user, you should set the following variable on your service:

## Growing the Volume

**_Only available to Pro users and above._**

To increase capacity in a volume, you can "grow" it from the volume settings.

- Click on the volume to open the settings
- Click Grow
- Follow the prompts to grow the volume

<Image
    layout="intrinsic"
    quality={100}
    width={1148}
    height={584}
    src="https://res.cloudinary.com/railway/image/upload/v1730326473/docs/volumes/growvolume_zbsjjq.png"
    alt="Grow volume"
/>

Note: growing a volume requires a restart of the attached service.

## Backups

Services with volumes support manual and automated backups, backups are covered in the backups reference guide.

## Code Examples

RAILWAY_RUN_UID=0


# Environments
Source: https://docs.railway.com/guides/environments

Manage complex development workflows via environments in your projects on Railway.



## Create an Environment

1. Select + New Environment from the environment drop down in the top navigation. You can also go to Settings > Environments.
2. Choose which type of environment to create -

   - **Duplicate Environment** creates a copy of the selected environment, including services, variables, and configuration.

     When the duplicate environment is created, all services and their configuration will be staged for deployment.
     _You must review and approve the staged changes before the services deploy._

   - **Empty Environment** creates an empty environment with no services.

---

## Sync Environments

You can easily sync environments to _import_ one or more services from one environment into another environment.

1. Ensure your current environment is the one that should _receive_ the synced service(s)
2. Click Sync at the top of the canvas
3. Select the environment from which to sync changes
4. Upon sync, each service card that has received a change will be tagged "New", "Edited", "Removed"
5. Review the staged changes by clicking Details on the staged changes banner
6. Click "Deploy" once you are ready to apply the changes and re-deploy

<Image src="https://res.cloudinary.com/railway/image/upload/v1743192480/docs/sync-environments_sujrxq.png"
            alt="Staged changes on Railway canvas"
            layout="responsive"
            width={1200} height={843} quality={100} />

---

## Enable PR Environments

Railway can spin up a temporary environment whenever you open a Pull Request. To enable PR environments, go to your Project Settings -> Environments tab.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1699568846/docs/enablePrEnv_f5n2hx.png"
alt="Screenshot of Deploy Options"
layout="responsive"
width={1622} height={506} quality={80} />

When enabled, a temporary environment is spun up to support the Pull Request deploy. These environments are deleted as soon as these PRs are merged or closed.

#### How Come my GitHub PR Won't Deploy?

Railway will not deploy a PR branch from a user who is not in your team or invited to your project without their associated GitHub account.

#### Domains in PR Environments

To enable automatic domain provisioning in PR environments, ensure that services in your base environment use Railway-provided domains. Services in PR environments will only receive domains automatically when their corresponding base environment services have Railway-provided domains.

### Bot PR Environments

You can enable automatic PR environment creation for PRs opened by GitHub bots (Dependabot, Renovatebot) using the Enable Bot PR Environments toggle on the Environments tab in the Project Settings page.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1720605990/bot-pr-envs_sa3tlo.png"
  alt="Bot PR Environments toggle"
  layout="responsive"
  width={1468}
  height={439}
  quality={80}
/>

## Forked Environments

As of January 2024, forked environments have been deprecated in favor of Isolated Environments with the ability to Sync.

Any environments forked prior to this change will remain, however, you must adopt the Sync Environments flow, in order to merge changes into your base environment.


# CLI
Source: https://docs.railway.com/guides/cli

Learn how to install and use the Railway CLI to manage your projects.

Railway project from the command line.

<Image src="https://res.cloudinary.com/railway/image/upload/v1645060494/docs/CLIexample_fiflvb.gif"
alt="GIF of the CLI in Action"
layout="intrinsic"
width={800} height={468} quality={100} />

## Installing the CLI

The Railway CLI can be installed via Homebrew, npm, Scoop, or directly from the source.

### Homebrew (macOS)

In a Terminal, enter the following command:

### npm (macOS, Linux, Windows)

In a Terminal, enter the following command:

This requires version =>16 of Node.js.

### Shell Script (macOS, Linux, Windows via WSL)

In a Terminal, enter the following command:

On Windows, you should use Windows Subsystem for Linux
with a Bash shell.

### Scoop (Windows)

In a PowerShell terminal, enter the following command:

This installs a native Windows binary (.exe). To learn more about Scoop,
see https://scoop.sh/.

### Pre-built Binaries

We publish pre-built binaries
on our GitHub repository that you can
download and use directly.

### From Source

The Railway CLI is an open source project on GitHub.
You can build a binary from source
if you wish.

## Authenticating With the CLI

Before you can use the Railway CLI, you must authenticate the CLI to your Railway account:

This command opens a new tab in your default browser to the https://railway.com
authentication page. Follow the instructions to complete the authentication process.

### Manual Login

You can also authenticate manually using a Pairing Code. This can be useful if
you're authenticating the CLI inside an environment without a browser (e.g. SSH
sessions).

Use the --browserless flag to authenticate manually:

### Tokens

In situations where user input or interaction isn't possible, such as in CI/CD pipelines, you can set either the RAILWAY_TOKEN or RAILWAY_API_TOKEN environment variable, based on your specific requirements as detailed below.

A Project Token is set via the RAILWAY_TOKEN environment variable.

An Account or Team Token is set via the RAILWAY_API_TOKEN environment variable.

**Note:** You can only use one type of token at a time. If both are set, the RAILWAY_TOKEN variable will take precedence.

#### Project Tokens

You can use Project Tokens to authenticate project-level actions.

Project Tokens allow the CLI to access all the project-level actions in the environment set when the token was created.

Some actions you can perform with a project token include -

- Deploying code - railway up
- Redeploying a deployment - railway redeploy
- Viewing build and deployment logs - railway logs

Some actions you **cannot** perform with a project token include -

- Creating a new project - railway init
- Printing information about the user - railway whoami
- Linking to another workspace - railway link

Use the token by setting the RAILWAY_TOKEN environment variable and then running railway <command>.

#### Account Tokens

Account Tokens come in two types - Personal Account Tokens and Team Tokens.

You can use Account Tokens to authenticate all CLI actions across all workspaces.

However, you can only use Team tokens to authenticate actions on projects within the workspace the token was scoped to when it was created.

Some actions you can perform with a personal account token include -

- Creating a new project - railway init
- Printing information about the user - railway whoami

Some actions you **cannot** perform with Team Token include -

- Printing information about the user - railway whoami
- Linking to another workspace - railway link

Use the token by setting the RAILWAY_API_TOKEN environment variable and then running railway <command>.

## Common Examples of CLI Usage

Below are some of the most commonly used CLI commands. Find a complete list of CLI commands in the CLI API reference page.

### Link to a Project

To associate a project and environment with your current directory:

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/railway-link_juslvt.png"
alt="Screenshot of Railway"
layout="intrinsic"
width={389} height={116} quality={80} />

This prompts you to select a team, project, and environment to associate with
your current directory. Any future commands will be run against this project and environment.

### Link to a Service

Associate a service in a project and environment with your current directory:

This links your current directory with the chosen service.

### Create a Project

Create a new project directly from the command line.

This prompts you to name your project and select a team to create the project in.

### Local Development

Run code locally with the same environment variables as your Railway project.

For example, to run your Node.js project with your remote environment variables:

### Local Shell

Open a new local shell with Railway environment variables. Similar to railway run but opens a new shell.

### Environments

Projects might have multiple environments, but by default the CLI links to the production environment.
You can change the linked environment with the environment command.

### Deploy

Deploy the linked project directory (if running from a subdirectory, the project root is still deployed).

If there are multiple services within your project, the CLI will prompt you for a service to deploy to.

### Add Database Service

Provision database services for a project.

Prompts you to select one or more databases to provision for your project.

### Logout

## SSH

The Railway CLI enables you to start a shell session inside your deployed Railway services. This command is useful for:

- **Debugging and development**: Live debugging production issues, running ad-hoc commands, accessing language REPLs, and comparing environments to identify discrepancies.
- **Database operations**: Executing migrations and rollbacks, running recovery operations, importing database dumps, and managing job queues.
- **System administration**: Inspecting log files, monitoring service status, examining file systems, troubleshooting network issues, and modifying application-level configurations within the container.
- **Framework-specific tasks**: Accessing Rails console, Django shell, or NestJS CLI for model inspection, database queries, and large-scale data operations.
- **Content and asset management**: Verifying asset deployment, debugging file uploads, and troubleshooting static asset issues.

Note that this command differs from railway run and railway shell, which pull environment variables and execute commands locally

### Prerequisites

Ensure you have the necessary setup in place:

1. **The Railway CLI installed** on your local machine.
2. **Logged in with your Railway account** using railway login.

### Usage

You can copy the exact command directly from the Railway dashboard:

1. Navigate to your project in the Railway dashboard.
2. Right-click on the service you want to connect to.
3. Select "Copy SSH Command" from the dropdown menu.

!image.png

This generates a complete command with all necessary IDs. Hereâ€™s an example

This command establishes a shell session with your running service container. You'll be dropped into either /bin/bash or /bin/sh, depending on what's available in your container.

Alternatively, you can run railway link, followed by railway ssh to achieve the same result.

The CLI also supportsÂ single command execution.Â This enables you to run commands and get their output instantly and exit without staying in an interactive session. Here's an example:

### How it works

Railway SSH differs significantly from traditional SSH implementations. Understanding how it works helps explain its capabilities and limitations.

Railway SSH does **not** use the standard SSH protocol (sshd). Instead, it establishes connections via a custom protocol built on top of websockets.

This approach provides several advantages:

- No need to configure SSH daemons in your containers.
- Secure communication through Railway's existing authentication.
- Works with any container that has a shell available.

This approach is secure by design:

- No SSH daemon exposed publicly on your containers.
- All communication goes through Railway's authenticated infrastructure.
- Services remain isolated from direct internet access.
- Uses Railway's existing security and access control mechanisms.

### Limitations and Workarounds

Understanding Railway SSH's limitations helps you plan appropriate workflows and implement effective workarounds for tasks that aren't directly supported.

**File Transfer Limitations**

Railway SSH does not support traditional file transfer methods:

- No SCP (Secure Copy Protocol) support for copying files between local and remote systems.
- No sFTP (SSH File Transfer Protocol) functionality for file management.
- No direct file download/upload capabilities through the SSH connection.

File transfer workarounds

- **Connect volume to file explorer service**: Deploy a simple file browser service that mounts the same volume as your main application. This provides web-based access to your files for download and upload operations.
- **Use CURL for file uploads**: From within the SSH session, upload files to external services:

- **Create temporary secure endpoints**: Modify your application to include a temporary, secured endpoint that serves specific files for download:

**SSH Protocol Limitations**

Railway SSH **does not implement the standard SSH protocol**, which means:

- **No SSH tunneling**: Cannot create secure tunnels to access private services or databases through the SSH connection.
- **No port forwarding**: Cannot forward ports from the remote container to your local machine for accessing internal services.
- **No IDE integration**: Cannot use VS Code's Remote-SSH extension or similar tools that depend on the SSH protocol for remote development.

**For private service access**: Use Tailscale subnet router to create secure network access to your Railway services without exposing them publicly.

**Container and Image Limitations**

- **Scratch images**: Containers built from scratch images typically don't include shell programs (/bin/bash or /bin/sh), making SSH connections impossible. These minimal images are designed for security and size optimization but sacrifice interactive access.
- **Minimal containers**: Some optimized container images may not include common debugging tools, text editors, or system utilities that you might expect in a traditional server environment.

### Troubleshooting

When Railway SSH connections fail or behave unexpectedly, several common issues and solutions can help resolve the problems.

1. The service must be actively running for SSH connections to work. If your service is configured with "serverless mode" and has gone to sleep, you'll need to wake it up by sending a request before attempting to SSH.
2. Firewall or network restrictions: Corporate networks or restrictive firewalls may block WebSocket connections used by Railway SSH.

### Best Practices

- **Use SSH for debugging only**: Avoid making permanent changes through SSH sessions. Instead, implement changes in your application code and deploy them properly.
- **Limit sensitive operations**: While SSH provides powerful access, avoid storing sensitive data or credentials in ways that might be exposed during SSH sessions.
- **Monitor SSH usage**: Regularly review who has SSH access to your services and ensure permissions align with current team structure and responsibilities. Note that SSH usage is currently not displayed in the dashboardâ€™s Activity tab.
- **Temporary access patterns**: Consider SSH access for debugging and investigation rather than routine administrative tasks, which should be automated through proper deployment processes.

### Contributing

Our CLI is open source. Contribute to the development of the Railway CLI by opening an issue or Pull Request on our GitHub Repo.

You can see the full documentation of the CLI API here.

## Code Examples

brew install railway

npm i -g @railway/cli

bash <(curl -fsSL cli.new)

scoop install railway

railway login

railway login --browserless

RAILWAY_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX railway up

RAILWAY_API_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX railway whoami

# Link to a project
railway link

# Link to a service
railway service

# Create a new project
railway init

# Run <cmd> locally with the same environment variables as your Railway project
railway run <cmd>

# Run your Node.js project with your remote environment variables
railway run npm start

# Open a new shell with Railway environment variables
railway shell

# Change the linked environment
railway environment

# Show build logs
railway up

# Return immediately after uploading
railway up --detach

railway add

railway logout

railway ssh --project=de609d2a-d70b-4457-8cb2-f1ce1410f779 --environment=f5bdd2a8-e2d1-4405-b814-eaa24fb9f7e8 --service=3ba723f0-5a20-44e1-9cff-7acd021d0a45

railway ssh -- ls

# Upload file to a temporary file sharing service
curl -X POST -F "file=@database_dump.sql" https://file.io/

# Upload to cloud storage (example with AWS S3)
aws s3 cp database_dump.sql s3://your-bucket/backups/

# Upload via HTTP to your own endpoint
curl -X POST -F "file=@logfile.txt" https://your-app.com/admin/upload

// Express.js example
app.get("/admin/download/:filename", authenticateAdmin, (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join("/app/data", filename);
  res.download(filePath);
});


# Join Priority Boarding!
Source: https://docs.railway.com/guides/join-priority-boarding

Priority Boarding is Railway's beta program for getting access early to new features. Learn how to be a part of it.



## Connect Railway to Discord

Visit <a href="https://railway.com/account" target="_blank">General Settings</a>, scroll down to Account Settings, and connect your account to the Railway Discord server.

<Image src="https://res.cloudinary.com/railway/image/upload/v1666373029/docs/discord-connect_ok03jw.png"
alt="Screenshot of Account Settings - Priority Boarding"
layout="responsive"
width={992} height={422} quality={80} />

## Let Percy Know

Once connected to Discord, you'll need to let Percy, the Railway Discord bot, know that you'd like to be a part of priority boarding.

In Discord, open up any channel, enter /beta, and follow the prompts.

Alternatively, you can open the command palette using CMD + K or Ctrl + K, then scroll down to Utilities, and select the join Priority Boarding button.

You should now have access to the #priority-boarding channel. You should also see that your Account Settings now display a new Priority Boarding status.

<Image src="https://res.cloudinary.com/railway/image/upload/v1666372408/docs/priority-boarding-settings_wvvza4.png"
alt="Screenshot of Account Settings - Priority Boarding"
layout="responsive"
width={1004} height={468} quality={80} />

## Keep Us Posted

From this point forward, you'll have Priority Boarding features automatically enabled for your account. We'll notify you of any new features via the Changelog.

We kindly request that you report any issues you encounter in the <a href="https://discord.com/channels/713503345364697088/921233523719946260" target="_blank">Priority Boarding Discord channel</a>.

That's all there is to it! Thanks for helping improve Railway, and we'll see you in Priority Boarding.


# Express
Source: https://docs.railway.com/guides/express

Learn how to deploy an Express app to Railway with one-click templates, GitHub, CLI, or Dockerfile. This guide covers setup, private networking, database integration, and deployment strategies.

This guide covers how to deploy an Express app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create an Express app!

## Create an Express App

**Note:** If you already have an Express app locally or on GitHub, you can skip this step and go straight to the Deploy Express App to Railway.

To create a new Express app, ensure that you have Node installed on your machine.

Create a directory, helloworld, and cd into it.

Run the following command in your terminal to create a new Express app within the helloworld directory:

A new Express app will be provisioned for you in the helloworld directory using pug as the view engine.

### Run the Express App locally

Run npm install to install all the dependencies.

Next, start the app by running the following command:

Launch your browser and navigate to http://localhost:3000 to view the app.

If you'd prefer to run the app on a different port, simply use the command PORT=8080 npm start in the terminal.

Afterward, you can access the app at http://localhost:8080.

### Add and Configure Database

**Note:** We will be using Postgres for this app. If you donâ€™t have it installed locally, you can either install it or use a different Node.js database package of your choice.

1. Create a database named expresshelloworld_dev.

2. Install the pg-promise package:

3. Open the routes/index.js file and modify the content to the code below:

The code above sets up a simple Express app with a route handler for the home page. It uses the pg-promise library to connect to a Postgres database and runs a query to fetch the current time from the database using SELECT NOW(). Upon receiving the data, it renders the index view with the fetched time, sending it to the client along with a title.

If an error occurs during the database query, the code catches the error, logs it, and sends a 500 status response to the client, indicating that there was an issue querying the database.

The page is only rendered after successfully receiving the database response to ensure proper handling of the data.

4. Open the views/index.pug file, and update it to display the timeFromDB value on the page.

5. Run the app again to see your changes in action!

### Prepare Express App for Deployment

In the routes/index.js file, replace the hardcoded Postgres database URL with an environment variable:

This allows the app to dynamically pull the correct database configuration from Railway during deployment.

## Deploy the Express App to Railway

Railway offers multiple ways to deploy your Express app, depending on your setup and preference.

### One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started with Express, Pug and connected to a Postgres database, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/template/BC51z6)

For Express API, here's another template you can begin with:

![Deploy on Railway](https://railway.com/template/Y6zLKF)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=express" target="_blank">variety of Express app templates</a> created by the community.

### Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Express app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:

   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter DATABASE_URL=${{Postgres.DATABASE_URL}}.
     - The value, ${{Postgres.DATABASE_URL}}, references the URL of your new Postgres database. Learn more about referencing service variables.

   **Note:** Explore the Railway CLI reference for a variety of options.

5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731505753/express_on_railway.png"
alt="screenshot of the deployed Express service"
layout="responsive"
width={2194} height={1652} quality={100} />

### Deploy From a GitHub Repo

To deploy an Express app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that it's a Node.js app via Railpack.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the Express app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Express apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npx express-generator --view=pug

npm start

npm i pg-promise

const express = require("express");
const pgp = require("pg-promise")();
const db = pgp(
  "postgres://username:password@127.0.0.1:5432/expresshelloworld_dev",
);
const router = express.Router();

/* GET home page. */
router.get("/", function (req, res, next) {
  db.one("SELECT NOW()")
    .then(function (data) {
      // Render the page only after receiving the data
      res.render("index", {
        title: "Hello World, Railway!",
        timeFromDB: data.now,
      });
    })
    .catch(function (error) {
      console.error("ERROR:", error);
      // If thereâ€™s an error, send a 500 response and do not call res.render
      res.status(500).send("Error querying the database");
    });
});

module.exports = router;

extends layout 

block content 
  h1= title 
  p Welcome to #{title} 
  p This is the time retrieved from the database: 
  p #{timeFromDB}

...
const db = pgp(process.env.DATABASE_URL);
...

railway init

# Use the Node official image
   # https://hub.docker.com/_/node
   FROM node:lts

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image
   COPY . ./

   # Install packages
   RUN npm ci

   # Serve the app
   CMD ["npm", "run", "start"]


# Nest
Source: https://docs.railway.com/guides/nest

Learn how to deploy a NestJS app to Railway with this step-by-step guide. It covers quick setup, database integration, one-click deploys and other deployment strategies.

This guide covers how to deploy a Nest app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's go ahead and create a Nest app!

## Create a Nest App

**Note:** If you already have a Nest app locally or on GitHub, you can skip this step and go straight to the Deploy Nest App to Railway.

To create a new Nest app, ensure that you have Node and NestJS installed on your machine.

Run the following command in your terminal to create a new Nest app:

A new Nest app will be provisioned for you in the helloworld directory.

### Run the Nest App locally

Next, start the app locally by running the following command:

Launch your browser and navigate to http://localhost:3000 to view the app.

If you'd prefer to run the app on a different port, simply use the command PORT=8080 npm run start in the terminal.

Afterward, you can access the app at http://localhost:8080.

### Add and Configure Database

**Note:** We will be using Postgres for this app. If you donâ€™t have it installed locally, you can either install it or use a different Node.js database package of your choice.

1. Create a database named nestjshelloworld_dev.

2. Install the following packages:

- typeorm is an ORM library for Typescript and JavaScript.
- pg is for communicating with Postgres database.

3. Open the src/app.module.ts file and modify the content to the code below:

Start the app using the command, npm run start:dev. The code above tries to connect to the database once the app is started. If any of the credentials are wrong, you will see a warning stating that the app can't connect to the database.

4. Open src/app.service.ts file and modify the content to return Hello World, Welcome to Railway!.

5. Run the app again to see your changes in action!

### Prepare NestJS App for deployment

In the src/app.module.ts file, replace the hardcoded Postgres database credentials with environment variables:

This allows the app to dynamically pull the correct database configuration from Railway during deployment.

## Deploy the Nest App to Railway

Railway offers multiple ways to deploy your Nest app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started with Nest connected to a Postgres database, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/template/nvnuEH)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=nest" target="_blank">variety of Nest app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Nest app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:

   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter
     - DB_DATABASE=${{Postgres.PGDATABASE}}.
     - DB_USERNAME=${{Postgres.PGUSER}}
     - DB_PASSWORD=${{Postgres.PGPASSWORD}}
     - DB_HOST=${{Postgres.PGHOST}}
     - The Postgres values references the credentials of your new Postgres database. Learn more about referencing service variables.

   **Note:** Explore the Railway CLI reference for a variety of options.

5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1732547945/docs/quick-start/nest_on_railway.png"
alt="screenshot of the deployed Nest service"
layout="responsive"
width={2069} height={2017} quality={100} />

### Deploy from a GitHub Repo

To deploy a Nest app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DB_DATABASE=${{Postgres.PGDATABASE}}.
     - DB_USERNAME=${{Postgres.PGUSER}}
     - DB_PASSWORD=${{Postgres.PGPASSWORD}}
     - DB_HOST=${{Postgres.PGHOST}}
     - The Postgres values references the credentials of your new Postgres database. Learn more about referencing service variables.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Node.js app via Nixpacks.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the Nest app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Nest apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

nest new helloworld

npm run start

npm i @nestjs/typeorm typeorm pg

import { Module } from "@nestjs/common";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";
import { TypeOrmModule } from "@nestjs/typeorm";

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: "postgres",
      host: "localhost",
      port: 5432,
      username: "username",
      password: "password",
      database: "nestjshelloworld_dev",
      entities: [],
      synchronize: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

import { Injectable } from "@nestjs/common";

@Injectable()
export class AppService {
  getHello(): string {
    return "Hello World, Welcome to Railway!";
  }
}

import { Module } from "@nestjs/common";
import { AppController } from "./app.controller";
import { AppService } from "./app.service";
import { TypeOrmModule } from "@nestjs/typeorm";

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: "postgres",
      host: process.env.DB_HOST,
      port: 5432,
      username: process.env.DB_USERNAME,
      password: process.env.DB_PASSWORD,
      database: process.env.DB_DATABASE,
      entities: [],
      synchronize: true,
    }),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

railway init

# Use the Node official image
   # https://hub.docker.com/_/node
   FROM node:lts

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image
   COPY . ./

   # Install packages
   RUN npm ci

   # Serve the app
   CMD ["npm", "run", "start:prod"]


# Fastify
Source: https://docs.railway.com/guides/fastify

Learn how to deploy a Fastify app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Fastify app on Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

## One-Click Deploy From a Template

![Deploy on Railway](https://railway.com/new/template/ZZ50Bj)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=fastify" target="_blank">variety of Fastify app templates</a> created by the community.

## Deploy From a GitHub Repo

To deploy a Fastify app on Railway directly from GitHub, follow the steps below:

1. Fork the basic <a href="https://github.com/railwayapp-templates/fastify" target="_blank">fastify GitHub repo</a>.
   - If you already have a GitHub repo you want to deploy, you can skip this step.
2. Create a <a href="https://railway.com/new" target="_blank">New Project.</a>
3. Click **Deploy from GitHub repo**.
4. Select the fastify repo or your own GitHub repo.
   - Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it.
5. Click **Deploy Now**.

Once the deployment is successful, a Railway service will be created for you. By default, this service will not be publicly accessible.

To set up a publicly accessible URL for the service, navigate to the **Networking** section in the Settings tab of your new service and click on Generate Domain.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727377689/docs/languages-and-frameworks/fastifyhelloworld_xbkrry.png"
alt="screenshot of new project menu with deploy from github selected"
layout="responsive"
width={2447} height={1029} quality={100} />

**Note:** Railway requires that Fastify's .listen method for the host be set to ::. This allows the app to be available over the <a href="/guides/public-networking" target="_blank">public</a> and <a href="/guides/private-networking" target="_blank">private network</a>.
You can find this in the <a href="https://github.com/railwayapp-templates/fastify/blob/main/src/app.ts" target="_blank">sample Fastify GitHub repo</a>.

If you donâ€™t set it correctly, you may encounter a 502 error page.

## Deploy From the CLI

1. <a href="/guides/cli#installing-the-cli" target="_blank">Install</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate with the CLI.</a>
2. Clone the forked <a href="https://github.com/railwayapp-templates/fastify" target="_blank">fastify GitHub repo</a> and cd into the directory.
   - You can skip this step if you already have an app directory or repo on your machine that you want to deploy.
3. Run railway init within the app directory to create a new project.
4. Run railway up to deploy.
   - The CLI will now scan, compress and upload our fastify app files to Railway's backend for deployment.

## Use a Dockerfile

1. Clone the forked fastify repo and cd into the directory.
   - You can skip this step if you already have an app directory or repo on your machine that you want to deploy.
2. Create a Dockerfile in the fastify or app's root directory.
3. Add the content below to the Dockerfile:

4. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a CDN using Amazon CloudFront to your Fastify app
- Add a Database Service
- Monitor your app

## Code Examples

# Use the Node.js 18 alpine official image
   # https://hub.docker.com/_/node
   FROM node:18-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . .

   # Install project dependencies
   RUN npm ci

   # Run the web service on container startup.
   CMD ["npm", "start"]


# FastAPI
Source: https://docs.railway.com/guides/fastapi

Learn how to deploy a FastAPI app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a FastAPI app on Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

## One-Click Deploy From a Template

![Deploy on Railway](https://railway.com/template/-NvLj4)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=fastapi" target="_blank">variety of FastAPI app templates</a> created by the community.

## Deploy From a GitHub Repo

To deploy a FastAPI app on Railway directly from GitHub, follow the steps below:

1. Fork the basic <a href="https://github.com/railwayapp-templates/fastapi" target="_blank">FastAPI GitHub repo</a>.
   - If you already have a GitHub repo you want to deploy, you can skip this step.
2. Create a <a href="https://railway.com/new" target="_blank">New Project.</a>
3. Click **Deploy from GitHub repo**.
4. Select the fastapi or your own GitHub repo.
   - Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it.
5. Click **Deploy Now**.

Once the deployment is successful, a Railway service will be created for you. By default, this service will not be publicly accessible.

To set up a publicly accessible URL for the service, navigate to the **Networking** section in the Settings tab of your new service and click on Generate Domain.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727418781/docs/languages-and-frameworks/CleanShot_2024-09-27_at_07.31.37_2x_m3zaxx.png"
alt="screenshot of the deployed fastapi service showing a hello world API response on a browser"
layout="responsive"
width={2435} height={919} quality={100} />

The FastAPI app is run via a <a href="https://hypercorn.readthedocs.io/en/latest/" target="_blank">Hypercorn server</a> as defined by the startCommand in the <a href="https://github.com/railwayapp-templates/fastapi/blob/main/railway.json" target="_blank">railway.json</a> file in the GitHub repository.

Railway makes it easy to define deployment configurations for your services directly in your project using a <a href="/guides/config-as-code" target="_blank">railway.toml or railway.json file</a>, alongside your code.

## Deploy From the CLI

1. <a href="/guides/cli#installing-the-cli" target="_blank">Install</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate with the CLI.</a>
2. Clone the forked <a href="https://github.com/railwayapp-templates/fastapi" target="_blank">fastapi GitHub repo</a> and cd into the directory.
   - You can skip this step if you already have an app directory or repo on your machine that you want to deploy.
3. Run railway init within the app directory to create a new project.
4. Run railway up to deploy.
   - The CLI will now scan, compress and upload our fastapi app files to Railway's backend for deployment.

## Use a Dockerfile

**Note:** If you already have an app directory or repo on your machine that you want to deploy, you can skip the first two steps.

1. Clone the forked fastapi repo and cd into the directory.
2. Delete the railway.json file.
3. Create a Dockerfile in the fastapi or app's root directory.
4. Add the content below to the Dockerfile:

5. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app
- Running a Cron Job

## Code Examples

# Use the Python 3 alpine official image
   # https://hub.docker.com/_/python
   FROM python:3-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . .

   # Install project dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Run the web service on container startup.
   CMD ["hypercorn", "main:app", "--bind", "::"]


# Flask
Source: https://docs.railway.com/guides/flask

Learn how to deploy a Flask app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Flask app to Railway in four ways:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.
4. Using a Dockerfile.

Now, let's create a Flask app!

## Create a Flask App

**Note:** If you already have a Flask app locally or on GitHub, you can skip this step and go straight to the Deploy Flask App to Railway.

To create a new Flask app, ensure that you have Python and Flask installed on your machine.

Follow the steps blow to set up the project in a directory.

Create a project directory and cd into it.

Create a virtual environment

Activate the virtual environment

**Note:** For windows developers, run it as env\Scripts\activate in your terminal.

Install Flask

Now create a new file, helloworld.py in the flaskproject directory. Add the following content to it:

1. from flask import Flask:
   - This line imports the Flask class from the Flask framework, which is used to create and manage a web application.
2. app = Flask(__name__):
   - This line creates an instance of the Flask class and assigns it to the app variable.
   - The __name__ argument helps Flask identify the location of the application. It's useful for determining resource paths and error reporting.
3. @app.route('/'):
   - The @app.route('/') decorator sets up a URL route for the app. When the root URL (/) is accessed, Flask will execute the function immediately below this decorator.
4. def hello():
   - The hello function returns a plain text message, _"Hello world, welcome to Railway!"_, which is displayed in the browser when the root URL of the app is accessed.

### Run the Flask App Locally

To run the application, use the flask command.

Open your browser and go to http://127.0.0.1:5000 to see the app running with a local development server.

### Prepare the Flask App for Deployment

1. Run the following command to install a production web server, gunicorn:

Next, run the following command to serve the app with gunicorn:

2. Open your browser and go to http://127.0.0.1:8000 to see the app running with a production server.

Create a requirements.txt file to store the dependencies of the packages needed to run the app.

**Note:** It's only safe to run the command above in a virtual environment, else it will freeze all python packages installed on your system.

3. Finally, create a nixpacks.toml file in the root directory of the app. Add the following content to it:

This setup instructs Railway to use Gunicorn as the server to start the application.

**Note:** The nixpacks.toml file is a configuration file used by Nixpacks, a build system developed and used by Railway, to set up and deploy applications.

In this file, you can specify the instructions for various build and deployment phases, along with environment variables and package dependencies.

With these changes, your Flask app is now ready to be deployed to Railway!

## Deploy Flask App to Railway

Railway offers multiple ways to deploy your Flask app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy From a Template

![Deploy on Railway](https://railway.com/template/zUcpux)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=flask" target="_blank">variety of Flask app templates</a> created by the community.

## Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Flask app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1730473731/docs/quick-start/flask_app_on_railway.png"
alt="screenshot of the deployed Flask service"
layout="responsive"
width={2164} height={1814} quality={100} />

## Deploy From a GitHub Repo

To deploy a Flask app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
4. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that it's a Python app via Railpack.

5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

## Use a Dockerfile

1. Create a Dockerfile in the app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app
- Running a Cron Job

## Code Examples

mkdir flaskproject
cd flaskproject

python -m venv env

source env/bin/activate

python -m pip install flask

import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world, welcome to Railway!'

flask --app helloworld run

pip install gunicorn

gunicorn main:app

pip freeze > requirements.txt

# nixpacks.toml

[start]
cmd = "gunicorn main:app"

railway init

railway up

# Use the Python 3 official image
   # https://hub.docker.com/_/python
   FROM python:3

   # Run in unbuffered mode
   ENV PYTHONUNBUFFERED=1

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . ./

   # Install project dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Run the web service on container startup.
   CMD ["gunicorn", "main:app"]


# Beego
Source: https://docs.railway.com/guides/beego

Learn how to deploy a Beego app to Railway with this step-by-step guide. It covers quick setup, private networking, database integration, one-click deploys and other deployment strategies.

This guide covers how to deploy a Beego app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Beego app!

## Create a Beego App

**Note:** If you already have a Beego app locally or on GitHub, you can skip this step and go straight to the Deploy Beego App to Railway.

To create a new Beego app, ensure that you have Go and Bee tool installed on your machine.

Run the following command in your terminal to create a new Beego app and install all dependencies:

A new Beego app will be provisioned for you in the helloworld directory.

### Configure Database

Run go get github.com/lib/pq in your terminal to install the Go Postgres driver.

Create a database, helloworld_dev in your local Postgres instance.

Open the main.go file and modify the content to the code below:

Replace this postgres://username:@localhost/helloworld_dev?sslmode=disable with the appropriate URL for your local Postgres database.

**Code Summary**:

- The Users struct defines the schema for the users table in the database.
- The init() function registers the Postgres driver, registers the Users model, and automatically creates the users table in the database. If any errors occur while inserting users, they are logged.
- The main() function creates an ORM instance, defines sample user data (first name and last name), inserts the data into the users table, and starts the Beego web server to serve your app.

### Run the Beego App Locally

To start your app, run:

Once the app is running, open your browser and navigate to http://localhost:8080 to view it in action.

In your terminal, youâ€™ll see logs indicating that the user data is being inserted. Head over to your database, and you should see the users table populated with the seeded data.

### Prepare Beego App for Deployment

1. Open the conf/app.conf file and add an environment variable, DATABASE_URL to it.

2. Head over to the main.go file and make some modifications to the way we retrieve the Postgres database url. The init() function should look like this:

## Deploy the Beego App to Railway

Railway offers multiple ways to deploy your Beego app, depending on your setup and preference.

### One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/CPq9Ry)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=beego" target="_blank">variety of Beego app templates</a> created by the community.

### Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Beego app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:

   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter DATABASE_URL=${{Postgres.DATABASE_URL}}.
     - The value, ${{Postgres.DATABASE_URL}}, references the URL of your new Postgres database. Learn more about referencing service variables.

   **Note:** Explore the Railway CLI reference for a variety of options.

5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731331898/docs/quick-start/beego_on_railway.png"
alt="screenshot of the deployed Beego service"
layout="responsive"
width={2420} height={1986} quality={100} />

### Deploy From a GitHub Repo

To deploy a Beego app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Go app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the Beego app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Beego apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

bee new helloworld
cd helloworld
go mod tidy

package main

import (
	"fmt"
	_ "helloworld/routers"

	_ "github.com/lib/pq"

	"github.com/beego/beego/v2/client/orm"
	beego "github.com/beego/beego/v2/server/web"
)

// Users -
type Users struct {
	ID        int    `orm:"column(id)"`
	FirstName string `orm:"column(first_name)"`
	LastName  string `orm:"column(last_name)"`
}

func init() {
	// set default database
	orm.RegisterDriver("postgres", orm.DRPostgres)

	// set default database
	orm.RegisterDataBase("default", "postgres", "postgres://unicodeveloper:@localhost/helloworld_dev?sslmode=disable")

	// register model
	orm.RegisterModel(new(Users))

	// create table
	orm.RunSyncdb("default", false, true)
}

func main() {
	o := orm.NewOrm()

	// Create a slice of Users to insert
	users := []Users{
		{FirstName: "John", LastName: "Doe"},
		{FirstName: "Jane", LastName: "Doe"},
		{FirstName: "Railway", LastName: "Deploy Beego"},
	}

	// Iterate over the slice and insert each user
	for _, user := range users {
		id, err := o.Insert(&user)
		if err != nil {
			fmt.Printf("Failed to insert user %s %s: %v\n", user.FirstName, user.LastName, err)
		} else {
			fmt.Printf("Inserted user ID: %d, Name: %s %s\n", id, user.FirstName, user.LastName)
		}
	}

	beego.Run()
}

bee run

db_url = ${DATABASE_URL}

func init() {
	// set default database
	orm.RegisterDriver("postgres", orm.DRPostgres)

	// set default database
	dbURL, err := beego.AppConfig.String("db_url")
	if err != nil {
		log.Fatal("Error getting database URL: ", err)
	}

	orm.RegisterDataBase("default", "postgres", dbURL)

	// register model
	orm.RegisterModel(new(Users))

	// create table
	orm.RunSyncdb("default", false, true)
}

railway init

# Use the Go 1.22 official image
   # https://hub.docker.com/_/golang
   FROM golang:1.22

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . ./

   # Install project dependencies
   RUN go mod download

   # Build the app
   RUN go build -o app

   # Run the service on container startup.
   ENTRYPOINT ["./app"]


# Gin
Source: https://docs.railway.com/guides/gin

Learn how to deploy a Gin app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Gin app on Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

## One-Click Deploy From a Template

![Deploy on Railway](https://railway.com/new/template/dTvvSf)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=gin" target="_blank">variety of Gin app templates</a> created by the community.

## Deploy From a GitHub Repo

To deploy a Gin app on Railway directly from GitHub, follow the steps below:

1. Fork the basic <a href="https://github.com/railwayapp-templates/gin" target="_blank">Gin GitHub repo</a>.
   - If you already have a GitHub repo you want to deploy, you can skip this step.
2. Create a <a href="https://railway.com/new" target="_blank">New Project.</a>
3. Click **Deploy from GitHub repo**.
4. Select the gin or your own GitHub repo.
   - Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it.
5. Click **Deploy Now**.

Once the deployment is successful, a Railway service will be created for you. By default, this service will not be publicly accessible.

To set up a publicly accessible URL for the service, navigate to the **Networking** section in the Settings tab of your new service and click on Generate Domain.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727691646/docs/languages-and-frameworks/gin-production_nvsmvf.png"
alt="screenshot of the deployed gin service showing a hello world API response on a browser"
layout="responsive"
width={2661} height={1019} quality={100} />

## Deploy From the CLI

1. <a href="/guides/cli#installing-the-cli" target="_blank">Install</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate with the CLI.</a>
2. Clone the forked <a href="https://github.com/railwayapp-templates/gin" target="_blank">gin GitHub repo</a> and cd into the directory.
   - You can skip this step if you already have an app directory or repo on your machine that you want to deploy.
3. Run railway init within the app directory to create a new project.
4. Run railway up to deploy.
   - The CLI will now scan, compress and upload our gin app files to Railway's backend for deployment.

## Use a Dockerfile

1. Clone the forked gin repo and cd into the directory.
   - You can skip this step if you already have an app directory or repo on your machine that you want to deploy.
2. Create a Dockerfile in the gin or app's root directory.
3. Add the content below to the Dockerfile:

4. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app
- Running a Cron Job

## Code Examples

# Use the Go 1.23 alpine official image
   # https://hub.docker.com/_/golang
   FROM golang:1.23-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy go mod and sum files
   COPY go.mod go.sum ./

   # Copy local code to the container image.
   COPY . ./

   # Install project dependencies
   RUN go mod download

   # Build the app
   RUN go build -o app

   # Run the service on container startup.
   ENTRYPOINT ["./app"]


# Rails
Source: https://docs.railway.com/guides/rails

Learn how to deploy a Rails app to Railway with this step-by-step guide. It covers quick setup, database integration, cron and sidekiq setups, one-click deploys and other deployment strategies.



## Create a Rails App

**Note:** If you already have a Rails app locally or on GitHub, you can skip this step and go straight to the Deploy Ruby on Rails App on Railway.

To create a new Rails app, ensure that you have Ruby and Rails installed on your machine. Once everything is set up, run the following command in your terminal:

This command will create a new Rails app named blog with PostgreSQL as the database config. Now, letâ€™s create a simple "Hello World" page to ensure everything is working correctly.

1. **Generate a Controller**: Run the following command to create a new controller named HelloWorld with an index action:

   This will generate the necessary files for the controller, along with a view, route, and test files.

2. **Update the Routes File**: Open the config/routes.rb file and modify it to set the root route to the hello_world#index action:

3. **Modify the View**: Open the app/views/hello_world/index.html.erb file and replace its content with the following:

4. **Run the Application Locally**: Start the Rails server by running:

   Open your browser and go to http://localhost:3000 to see your "Hello World" page in action.

Now that your app is running locally, letâ€™s move on to deploying it to Railway!

## Deploy Ruby on Rails App on Railway

Railway offers multiple ways to deploy your Rails app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Rails app along with a Postgres database and Redis.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/sibk1f)

After deploying, we recommend that you eject from the template to create a copy of the repository under your own GitHub account. This will give you full control over the source code and project.

## Deploy from the CLI

To deploy the Rails app using the Railway CLI, please follow the steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Rails app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.

- **Note:** If you see an error about a missing secret_key_base for the production environment, donâ€™t worry. Weâ€™ll fix this in the next step.

4. **Add a Database Service**:
   - Run railway add.
   - Select PostgreSQL by pressing space and hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
5. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - SECRET_KEY_BASE or RAILS_MASTER_KEY: Set the value to the key from your local app's config/master.key.
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_PUBLIC_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
   - Use the **Raw Editor** to add any other required environment variables in one go.
6. **Redeploy the Service**:
   - Click **Deploy** on the Railway dashboard to apply your changes.
7. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

**Note:** If your app has a Dockerfile (which newer Rails apps typically include by default), Railway will automatically detect and use it to build your app. If not, Railway will still handle the deployment process for you.

8. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1728049734/docs/quick-start/railsapp_on_railway.png"
alt="screenshot of the deployed Rails service showing the Hello world page"
layout="responsive"
width={2375} height={1151} quality={100} />

## Deploy from a GitHub Repo

To deploy the Rails app to Railway, start by pushing the app to a GitHub repo. Once thatâ€™s set up, follow the steps below to complete the deployment process.

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables**:
   - Click **Add Variables** and configure all the necessary environment variables for your app.
     - E.g RAILS_ENV: Set the value to production.
     - E.g SECRET_KEY_BASE or RAILS_MASTER_KEY: Set the value to the key from your app's config/master.key.
4. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
5. **Add a Database Service**:
   - Right-click on the Railway project canvas or click the **Create** button.
   - Select **Database**.
   - Select **Add PostgreSQL** from the available databases.
     - This will create and deploy a new Postgres database service for your project.
6. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
   - Use the **Raw Editor** to add any other required environment variables in one go.
7. **Prepare Database and Start Server**:
   - Go to your app service <a href="/overview/the-basics#service-settings">**Settings**</a> section.
     - In the **Deploy** section, set bin/rails db:prepare && bin/rails server -b :: as the <a href="/guides/start-command">**Custom Start Command**</a>. This command will run your database migrations and start the server.
8. **Redeploy the Service**:
   - Click **Deploy** on the Railway dashboard to apply your changes.
9. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

**Note:** During the deployment process, Railway will automatically detect that itâ€™s a Rails app.

10. **Set Up a Public URL**:
    - Navigate to the **Networking** section under the Settings tab of your new service.
    - Click Generate Domain to create a public URL for your app.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Rails apps effortlessly!

Next, we'll cover how to set up workers and cron jobs for your Rails app on Railway.

## Set Up Workers & Cron Jobs with Sidekiq

Sidekiq is a powerful and efficient background job processor for Ruby apps, and it integrates seamlessly with Rails. Follow the instructions below to configure and run Sidekiq in your Rails app on Railway:

1. **Install Sidekiq**
   - Start by adding sidekiq and sidekiq-cron to your Rails app. In your terminal, run the following command:
     
2. **Add a Redis Database Service**
   - Sidekiq uses Redis as a job queue. To set this up:
     - Right-click on the Railway project canvas or click the **Create** button.
     - Select **Database**.
     - Select **Add Redis** from the available databases.
       - This will create and deploy a new Redis service for your app.
3. **Create and Configure a Worker Service**
   - Now, set up a <a href="/guides/services#creating-a-service">separate service</a> to run your Sidekiq workers.
     - Create a new <a href="/overview/the-basics#service-settings">**Empty Service**</a> and name it **Worker Service**.
     - Go to the <a href="/overview/the-basics#service-settings">**Settings**</a> tab of this service to configure it.
     - In the **Source** section, connect your GitHub repository to the **Source Repo**.
     - Under the <a href="/guides/build-configuration#customize-the-build-command">**Build**</a> section, set bundle install as the **Custom Build Command**. This installs the necessary dependencies.
     - In the **Deploy** section, set bundle exec sidekiq as the <a href="/guides/start-command">**Custom Start Command**</a>. This command will start Sidekiq and begin processing jobs.
     - Click on <a href="/overview/the-basics#service-variables">**Variables**</a> at the top of the service settings.
     - Add the following environment variables:
       - RAILS_ENV: Set the value to production.
       - SECRET_KEY_BASE or RAILS_MASTER_KEY: Set this to the value of your Rails appâ€™s secret key.
       - REDIS_URL: Set this to ${{Redis.REDIS_URL}} to reference the Redis database URL. This tells Sidekiq where to find the job queue. Learn more about referencing service variables.
       - Include any other environment variables your app might need.
     - Click **Deploy** to apply the changes and start the deployment.
4. **Verify the Deployment**:

   - Once the deployment is complete, click on **View Logs**. If everything is set up correctly, you should see Sidekiq starting up and processing any queued jobs.

   <Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1728065286/docs/quick-start/worker_service.png" alt="screenshot of the worker service running Sidekiq" 
   layout="responsive" width={2210} height={1696} quality={100} />

5. **Confirm All Services Are Connected**:
   - At this stage, your application should have the following services set up and connected:
     - **App Service**: Running the main Rails application.
     - **Worker Service**: Running Sidekiq to process background jobs.
     - **Postgres Service**: The database for your Rails app.
     - **Redis Service**: Used by Sidekiq to manage background jobs

Hereâ€™s how your setup should look:

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1728065005/docs/quick-start/rails_all_services_connected.png" alt="Diagram showing all Rails services connected on Railway" layout="responsive" width={3308} height={1920} quality={100} />

By following these steps, youâ€™ll have a fully functional Rails app with background job processing using Sidekiq on Railway. If you run into any issues or need to make adjustments, check the logs and revisit your environment variable configurations.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

rails new blog --database=postgresql

rails g controller HelloWorld index

Rails.application.routes.draw do
       get "hello_world/index"
       # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

       # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
       # Can be used by load balancers and uptime monitors to verify that the app is live.
       get "up" => "rails/health#show", as: :rails_health_check

       # Render dynamic PWA files from app/views/pwa/*
       get "service-worker" => "rails/pwa#service_worker", as: :pwa_service_worker
       get "manifest" => "rails/pwa#manifest", as: :pwa_manifest

       # Defines the root path route ("/")
       root "hello_world#index"
   end

<h1>Hello World</h1>

   <p> This is a Rails app running on Railway</p>

bin/rails server

railway init

railway up

bundle add sidekiq
     bundle add sidekiq-cron


# Axum
Source: https://docs.railway.com/guides/axum

Learn how to deploy an Axum app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, GitHub, Dockerfile and other deployment strategies.

This guide covers how to deploy an Axum app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create an Axum app! ðŸš€

## Create an Axum App

**Note:** If you already have an Axum app locally or on GitHub, you can skip this step and go straight to the Deploy Axum App to Railway.

To create a new Axum app, ensure that you have Rust installed on your machine.

Run the following command in your terminal to create a new Axum app:

The command creates a new binary-based Cargo project in a helloworld directory.

Next, cd into the directory and add axum and tokio as dependencies by running the following command:

This will add axum and tokio as dependencies, with tokio configured to use the "full" feature, which includes its complete set of capabilities. Youâ€™ll find both dependencies listed in your Cargo.toml file.

These dependencies are required to create a bare minimum axum application.

### Modify the Application File

Next, open the app in your IDE and navigate to the src/main.rs file.

Replace the content with the code below:

The code above sets up a simple web server using the Axum framework and the Tokio async runtime. The server listens on the port gotten from the environment variable, PORT and defaults to 3000 if there's none set.

It defines one route, /, which is mapped to a handler function called root. When a GET request is made to the root path, the handler responds with the static string "Hello World, from Axum!".

The Router from Axum is used to configure the route, and tokio::net::TcpListener binds the server to listen for connections on all available network interfaces (address 0.0.0.0).

The asynchronous runtime, provided by the #[tokio::main] macro, ensures the server can handle requests efficiently. The axum::serve function integrates with the Hyper server to actually process requests.

### Run the Axum App Locally

Run the following command in the helloworld directory via the terminal:

All the dependencies will be installed and your app will be launched.

Open your browser and go to http://localhost:3000 to see your app.

## Deploy the Axum App to Railway

Railway offers multiple ways to deploy your Axum app, depending on your setup and preference.

### One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/5HAMxu)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=axum" target="_blank">variety of Axum templates</a> created by the community.

### Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Axum app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
4. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Rust app.

5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729880417/docs/quick-start/axum_app_service.png"
alt="screenshot of the deployed Axum service"
layout="responsive"
width={1982} height={1822} quality={100} />

### Deploy From a GitHub Repo

To deploy an Axum app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Rust app.

5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Axum app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Axum apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

cargo new helloworld --bin

cargo add axum
cargo add tokio --features full

use axum::{
    routing::get,
    Router,
};

#[tokio::main]
async fn main() {
    // build our application with a single route
    let app = Router::new().route("/", get(root));

    // Get the port number from the environment, default to 3000
    let port: u16 = std::env::var("PORT")
        .unwrap_or_else(|_| "3000".to_string()) // Get the port as a string or default to "3000"
        .parse() // Parse the port string into a u16
        .expect("Failed to parse PORT");

    // Create a socket address (IPv6 binding)
    let address = SocketAddr::from(([0, 0, 0, 0, 0, 0, 0, 0], port));
    let listener = tokio::net::TcpListener::bind(&address).await.unwrap();

    // Run the app with hyper, listening on the specified address
    axum::serve(listener, app).await.unwrap();
}

// basic handler that responds with a static string
async fn root() -> &'static str {
    "Hello World, from Axum!"
}

cargo run

railway init

railway up

FROM lukemathwalker/cargo-chef:latest-rust-1 AS chef

   # Create and change to the app directory.
   WORKDIR /app

   FROM chef AS planner
   COPY . ./
   RUN cargo chef prepare --recipe-path recipe.json

   FROM chef AS builder
   COPY --from=planner /app/recipe.json recipe.json

   # Build dependencies - this is the caching Docker layer!
   RUN cargo chef cook --release --recipe-path recipe.json

   # Build application
   COPY . ./
   RUN cargo build --release

   CMD ["./target/release/helloworld"]


# Rocket
Source: https://docs.railway.com/guides/rocket

Learn how to deploy a Rust Rocket app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Rocket app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Rocket app! ðŸš€

## Create a Rocket App

**Note:** If you already have a Rocket app locally or on GitHub, you can skip this step and go straight to the Deploy Rocket App to Railway.

To create a new Rocket app, ensure that you have Rust installed on your machine.

Run the following command in your terminal to create a new Rust app:

The command creates a new binary-based Cargo project in a helloworld directory.

Next, cd into the directory and add Rocket as a dependency by running the following command:

This will add Rocket as a dependency, and youâ€™ll see it listed in your Cargo.toml file.

### Modify the Application File

Next, open the app in your IDE and navigate to the src/main.rs file.

Replace the content with the code below:

The code above uses the Rocket framework to create a basic web server that responds to HTTP requests. It defines a simple route using the #[get("/")] macro, which tells Rocket to handle GET requests to the root URL (/).

The index() function is the handler for this route and returns a static string, **"Hello world, Rocket!"**, which will be sent as the response when the root URL is accessed.

The #[launch] attribute on the rocket() function marks it as the entry point to launch the application. Inside rocket(), the server is built with rocket::build() and the index route is mounted to the root path / using mount().

When the application runs, it listens for incoming requests and serves the "Hello world, Rocket!" response for requests made to the root URL, demonstrating a simple routing and response mechanism in Rocket.

### Run the Rocket App locally

Run the following command in the helloworld directory via the terminal:

All the dependencies will be installed and your app will be launched.

Open your browser and go to http://localhost:8000 to see your app.

## Deploy the Rocket App to Railway

Railway offers multiple ways to deploy your Rocket app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/FkW8oU)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=rocket" target="_blank">variety of Rocket templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Rocket app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
4. **Set Up a Public URL**:

   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

   **Note:** You'll come across a 502 error where your application doesn't respond. We'll fix that in the next step.

5. **Configure Rocket app to accept non-local connections**:
   - Rocket apps need to be configured to accept external connections by listening on the correct address, which is typically 0.0.0.0. You can easily do this by setting the address through the environment variable.
     Run the following command to set the Rocket address to 0.0.0.0:
     bash
    railway variables --set "ROCKET_ADDRESS=0.0.0.0"
    
6. **Redeploy the Service**:
   - Run railway up again to trigger a redeployment of the service.
7. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully. Access your public URL again and you should see your app working well.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729858389/docs/quick-start/rocket_app_service.png"
alt="screenshot of the deployed Rocket service"
layout="responsive"
width={2038} height={1698} quality={100} />

### Deploy from a GitHub Repo

To deploy a Rocket app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables**:
   - Click **Add Variables**, then add ROCKET_ADDRESS with the value 0.0.0.0. This allows your Rocket app to accept external connections by listening on 0.0.0.0.
4. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Rust app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Rocket app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Rocket apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

cargo new helloworld --bin

cargo add rocket

#[macro_use]
extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello world, Rocket!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}

cargo run

railway init

railway up

FROM lukemathwalker/cargo-chef:latest-rust-1 AS chef

   # Create and change to the app directory.
   WORKDIR /app

   FROM chef AS planner
   COPY . ./
   RUN cargo chef prepare --recipe-path recipe.json

   FROM chef AS builder
   COPY --from=planner /app/recipe.json recipe.json

   # Build dependencies - this is the caching Docker layer!
   RUN cargo chef cook --release --recipe-path recipe.json

   # Build application
   COPY . ./
   RUN cargo build --release

   CMD ["./target/release/helloworld"]


# Laravel
Source: https://docs.railway.com/guides/laravel

Learn how to deploy a Laravel app to Railway with this step-by-step guide. It covers quick setup, private networking, database integration, one-click deploys and other deployment strategies.

This guide covers how to deploy a Laravel app on Railway in three ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.

## One-Click Deploy From a Template

![Deploy on Railway](https://railway.com/new/template/fWEWWf)

This template sets up a basic Laravel application along with a Postgres database on Railway. You can also choose from a <a href="https://railway.com/templates?q=laravel" target="_blank">variety of Laravel app templates</a> created by the community.

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

## Deploy From a GitHub Repo

To deploy a Laravel app on GitHub to Railway, follow the steps below:

1. Create a <a href="https://railway.com/new" target="_blank">New Project.</a>

2. Click **Deploy from GitHub repo**.

3. Select your GitHub repo.

   - Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it.

4. Click **Add Variables**.

   - Add all your app environment variables.

5. Click **Deploy**.

Once the deployment is successful, a Railway service will be created for you. By default, this service will not be publicly accessible.

**Note:** Railway will automatically detect that it's a Laravel app during deploy and run your app via php-fpm and nginx.

To set up a publicly accessible URL for the service, navigate to the **Networking** section in the Settings tab of your new service and click on Generate Domain.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727885952/docs/quick-start/CleanShot_2024-10-02_at_17.18.04_2x_nn78ga.png"
alt="screenshot of the deployed Laravel service showing the Laravel home page"
layout="responsive"
width={2855} height={2109} quality={100} />

**Note**: Jump to the **Set Up Database, Migrations, Crons and Workers** section to learn how to run your Laravel app along with a Postgres(or MySQL) database, cron jobs, and workers.

## Deploy From the CLI

If you have your Laravel app locally, you can follow these steps:

1. <a href="/guides/cli#installing-the-cli" target="_blank">Install</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate with the Railway CLI.</a>

2. Run railway init within your Laravel app root directory to create a new project on Railway.

   - Follow the steps in the prompt to give your project a name.

3. Run railway up to deploy.

   - The CLI will now scan, compress and upload our Laravel app files to Railway's backend for deployment.

   - Your terminal will display real-time logs as your app is being deployed on Railway.

4. Once the deployment is successful, click on **View logs** on the recent deployment on the dashboard.

   - You'll see that the server is running. However you'll also see logs prompting you to add your env variables.

5. Click on the <a href="/overview/the-basics#service-variables">**Variables**</a> section of your service on the Railway dashboard.

6. Click on **Raw Editor** and add all your app environment variables.

7. Click on **Deploy** to redeploy your app.

To set up a publicly accessible URL for the service, navigate to the **Networking** section in the Settings tab of your new service and click on Generate Domain.

**Note:** The next step shows how to run your Laravel app along with a database, migrations, cron jobs, and workers.

## Set Up Database, Migrations, Crons and Workers

This setup deploys your Laravel app on Railway, ensuring that your database, scheduled tasks (crons), and queue workers are all fully operational.

The deployment structure follows a "majestic monolith" architecture, where the entire Laravel app is managed as a single codebase but split into four separate services on Railway:

- **App Service**: Handles HTTP requests and user interactions.

- **Cron Service**: Manages scheduled tasks (e.g., sending emails or running reports).

- **Worker Service**: Processes background jobs from the queue.

- **Database Service**: Stores and retrieves your application's data.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727910244/docs/quick-start/deploy%20architecture.png"
alt="screenshot of the deploy architecture of the Laravel app"
layout="responsive"
width={3118} height={1776} quality={100} />
_My Majestic Monolith Laravel app_

Please follow these steps to get started:

1. Create four bash scripts in the root directory of your Laravel app: build-app.sh, run-worker.sh, and run-cron.sh.

   These scripts will contain the commands needed to deploy and run the app, worker, and cron services for your Laravel app on Railway.

   - Add the content below to the build-app.sh file:

     **Note:** You can add any additional commands to the script that you want to run each time your app service is built.

   - Add the content below to the run-worker.sh file:

   - Add the content below to the run-cron.sh file:

2. Create a Postgres Database service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas.</a>

   - Click on **Deploy**.

3. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas.</a>

   - Name the service **App service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a> to configure it.

   - Connect your GitHub repo to the **Source Repo** in the **Source** section.

   - Add chmod +x ./build-app.sh && sh ./build-app.sh to the **Custom Build Command** in the <a href="/guides/build-configuration#customize-the-build-command">**Build**</a> section.

   - Add php artisan migrate to the <a href="/guides/pre-deploy-command">**Pre-Deploy Command**</a> in the **Deploy** section.

   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.

   - Add all the necessary environment variables required for the Laravel app especially the ones listed below.

     - APP_KEY: Set the value to what you get from the php artisan key:generate command.

     - DB_CONNECTION: Set the value to pgsql.

     - QUEUE_CONNECTION: Set the value to database.

     - DB_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.

   - Click **Deploy**.

4. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>.

   - Name the service **cron service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.

   - Connect your GitHub repo to the **Source Repo** in the **Source** section.

   - Add chmod +x ./run-cron.sh && sh ./run-cron.sh to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.

   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.

   - Add all the necessary environment variables especially those highlighted already in step 3.

   - Click **Deploy**.

5. Create a new service again on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>.

   - Name the service **worker service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.

   - Connect your GitHub repo to the **Source Repo** in the **Source** section.

   - Add chmod +x ./run-worker.sh && sh ./run-worker.sh to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.

   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.

   - Add all the necessary environment variables especially those highlighted already in step 3.

   - Click **Deploy**.

At this point, you should have all three services deployed and connected to the Postgres Database service:

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727910244/docs/quick-start/deploy%20architecture.png"
alt="screenshot of the deploy architecture of the Laravel app"
layout="responsive"
width={3118} height={1776} quality={100} />

- **Cron Service**: This service should run the Laravel Scheduler to manage scheduled tasks.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727912479/docs/quick-start/CleanShot_2024-10-03_at_00.40.40_2x_cwgazh.png"
alt="screenshot of the cron service of the Laravel app"
layout="responsive"
width={2165} height={1873} quality={100} />

- **Worker Service**: This service should be running and ready to process jobs from the queue.

- **App Service**: This service should be running and is the only one that should have a public domain, allowing users to access your application.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1727885952/docs/quick-start/CleanShot_2024-10-02_at_17.18.04_2x_nn78ga.png"
alt="screenshot of the deployed Laravel service showing the Laravel home page"
layout="responsive"
width={2855} height={2109} quality={100} />
_App service_

**Note:** There is a community template available that demonstrates this deployment approach. You can easily deploy this template and then connect it to your own GitHub repository for your application.

## Logging

Laravel, by default, writes logs to a directory on disk. However, on Railwayâ€™s ephemeral filesystem, this setup wonâ€™t persist logs.

To ensure logs and errors appear in Railwayâ€™s console or with railway logs, update the LOG_CHANNEL environment variable to errorlog. You can set it via the Railway dashboard or CLI as shown:

## Can I Deploy with Laravel Sail?

You may be thinking about using Laravel Sail, which is the standard approach for deploying Laravel applications with Docker. At its core, Sail relies on a docker-compose.yml file to manage the environment.

However, it's important to note that Railway currently does not support Docker Compose.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x build-app.sh`

     # Exit the script if any command fails
     set -e

     # Build assets using NPM
     npm run build

     # Clear cache
     php artisan optimize:clear

     # Cache the various components of the Laravel application
     php artisan config:cache
     php artisan event:cache
     php artisan route:cache
     php artisan view:cache

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x run-worker.sh`

     # This command runs the queue worker.
     # An alternative is to use the php artisan queue:listen command
     php artisan queue:work

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x run-cron.sh`

     # This block of code runs the Laravel scheduler every minute
     while [ true ]
         do
             echo "Running the scheduler..."
             php artisan schedule:run --verbose --no-interaction &
             sleep 60
         done

railway variables --set "LOG_CHANNEL=errorlog"


# Symfony
Source: https://docs.railway.com/guides/symfony

Learn how to deploy a Symfony app to Railway with this step-by-step guide. It covers quick setup, database integration, cron and workers, one-click deploys and other deployment strategies.

This guide covers how to deploy a Symfony app to Railway in three ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.

Now, let's create a Symfony app!

## Create a Symfony App

**Note:** If you already have a Symfony app locally or on GitHub, you can skip this step and go straight to the Deploy Symfony App to Railway.

To create a new Symfony app, ensure that you have Composer, PHP and Symfony installed on your machine.

Run the following command in your terminal to create a new Symfony app:

A new Symfony app will be provisioned for you in the apphelloworld directory.

### Run the Symfony App locally

To start your app, run:

Once the app is running, open your browser and navigate to http://localhost:8000 to view it in action.

## Deploy the Symfony App to Railway

Railway offers multiple ways to deploy your Symfony app, depending on your setup and preference.

## One-Click Deploy from a Template

![Deploy on Railway](https://railway.com/new/template/4tnH_D)

This template sets up a starter Symfony application along with a Postgres database on Railway. You can also choose from a <a href="https://railway.com/templates?q=symfony" target="_blank">variety of Symfony app templates</a> created by the community.

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

## Deploy from the CLI

If you have your Symfony app locally, you can follow these steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Symfony app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:
   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter DATABASE_URL=${{Postgres.DATABASE_URL}}.
     - The value, ${{Postgres.DATABASE_URL}}, references the URL of your new Postgres database. Learn more about referencing service variables.
   - Set the other environment variables: - APP_ENV=prod - This setting informs Symfony that the app is running in a production environment, optimizing it for performance. - APP_SECRET=secret where _secret_ is your generated app secret. - COMPOSER_ALLOW_SUPERUSER="1" - This is necessary to allow Composer to run as root, enabling the plugins that Symfony requires during installation. - NIXPACKS_PHP_ROOT_DIR="/app/public" - This ensures the Nginx configuration points to the correct root directory path to serve the app.
     **Note:** Explore the Railway CLI reference for a variety of options.
5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432139/docs/quick-start/symfony7_on_railway.png"
alt="screenshot of the deployed Symfony service"
layout="responsive"
width={2741} height={2193} quality={100} />

## Deploy from a GitHub Repo

To deploy a Symfony app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - APP_ENV=prod - This setting informs Symfony that the app is running in a production environment, optimizing it for performance.
     - APP_SECRET=secret where _secret_ is your generated app secret.
     - COMPOSER_ALLOW_SUPERUSER="1" - This is necessary to allow Composer to run as root, enabling the plugins that Symfony requires during installation.
     - NIXPACKS_PHP_ROOT_DIR="/app/public" - This ensures the Nginx configuration points to the correct root directory path to serve the app.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a PHP app via Nixpacks.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

**Note:** The next step shows how to run your Symfony app along with a database, migrations, cron jobs, and workers.

## Set Up Database, Migrations, Crons and Workers

This setup deploys your Symfony app on Railway, ensuring that your database, scheduled tasks (crons), and queue workers are all fully operational.

The deployment structure follows a "majestic monolith" architecture, where the entire Symfony app is managed as a single codebase but split into four separate services on Railway:

- **App Service**: Handles HTTP requests and user interactions.
- **Cron Service**: Manages scheduled tasks (e.g., sending emails or running reports).
- **Worker Service**: Processes background jobs from the queue.
- **Database Service**: Stores and retrieves your application's data.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432227/docs/quick-start/symfony_architecture.png"
alt="screenshot of the deploy architecture of the Symfony app"
layout="responsive"
width={3294} height={2048} quality={100} />
_My Majestic Monolith Symfony app_

Please follow these steps to get started:

1. Create three bash scripts in the root directory of your Symfony app: run-app.sh, run-worker.sh, and run-cron.sh.

   These scripts will contain the commands needed to deploy and run the app, worker, and cron services for your Symfony app on Railway.

   - Add the content below to the run-app.sh file:

     **Note:** This is required to start your app service after the build phase is complete. This script will execute the migrations and then start the Nginx server.

   - Add the content below to the run-worker.sh file. This script will run the queue worker:

   - Symfony doesn't natively include a scheduler. So, please install the CronBundle to define and run scheduled tasks. With that set up, add the content below to the run-cron.sh file:

2. Create a Postgres Database service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas.</a>
   - Click on **Deploy**.
3. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas.</a>
   - Name the service **App Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a> to configure it.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Add chmod +x ./run-app.sh && sh ./run-app.sh to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.
   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables required for the Symfony app especially the ones listed below.
     - APP_ENV=prod
     - APP_SECRET=secret where _secret_ is your generated app secret.
     - COMPOSER_ALLOW_SUPERUSER="1" - This is necessary to allow Composer to run as root, enabling the plugins that Symfony requires during installation.
     - NIXPACKS_PHP_ROOT_DIR="/app/public" - This ensures the Nginx configuration points to the correct root directory path to serve the app.
     - DATABASE_URL=${{Postgres.DATABASE_URL}} (this references the URL of your Postgres database).
   - Click **Deploy**.
4. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>.
   - Name the service **Cron Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Add chmod +x ./run-cron.sh && sh ./run-cron.sh to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.
   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables especially those highlighted already in step 3.
   - Click **Deploy**.
5. Create a new service again on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>.
   - Name the service **Worker Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Add chmod +x ./run-worker.sh && sh ./run-worker.sh to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.
   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables especially those highlighted already in step 3.
   - Click **Deploy**.

At this point, you should have all three services deployed and connected to the Postgres Database service:

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432227/docs/quick-start/symfony_architecture.png"
alt="screenshot of the deploy architecture of the Symfony app"
layout="responsive"
width={3294} height={2048} quality={100} />

- **Cron Service**: This service should run the cron bundler Scheduler to manage scheduled tasks.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432857/docs/quick-start/cron_service.png"
alt="screenshot of the cron service of the Symfony app"
layout="responsive"
width={2547} height={2057} quality={100} />

- **Worker Service**: This service should be running and ready to process jobs from the queue.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432862/docs/quick-start/worker_service_symfony.png"
alt="screenshot of the worker service of the Symfony app"
layout="responsive"
width={2545} height={2069} quality={100} />

- **App Service**: This service should be running and is the only one that should have a public domain, allowing users to access your application.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731432139/docs/quick-start/symfony7_on_railway.png"
alt="screenshot of the deployed Symfony service"
layout="responsive"
width={2741} height={2193} quality={100} />
_App service_

**Note:** There is a community template available that demonstrates this deployment approach. You can easily deploy this template and then connect it to your own GitHub repository for your application.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

symfony new --webapp apphelloworld

symfony server:start

railway init

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x run-app.sh`
     # Run migrations, process the Nginx configuration template and start Nginx
     php bin/console doctrine:migrations:migrate --no-interaction && node /assets/scripts/prestart.mjs /assets/nginx.template.conf /nginx.conf && (php-fpm -y /assets/php-fpm.conf & nginx -c /nginx.conf)

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x run-worker.sh`

     # This command runs the queue worker.
     php bin/console messenger:consume async --time-limit=3600 --memory-limit=128M &

#!/bin/bash
     # Make sure this file has executable permissions, run `chmod +x run-cron.sh`

     # This block of code runs the scheduler every minute
     while [ true ]
         do
             echo "Running the scheduler..."
             php bin/console cron:start [--blocking] --no-interaction &
             sleep 60
         done


# Luminus
Source: https://docs.railway.com/guides/luminus

Learn how to deploy your Clojure Luminus app to Railway with this step-by-step guide. It covers quick setup, database integration, one-click deploys and other deployment strategies.

This guide covers how to deploy a Luminus app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Luminus app!

## Create a Luminus App

**Note:** If you already have a Luminus app locally or on GitHub, you can skip this step and go straight to the Deploy Luminus App to Railway.

To create a new Luminus app, ensure that you have JDK and Leiningen installed on your machine.

Run the following command in your terminal to create a new Luminus app with Postgres and a production ready server:

A new Luminus app will be provisioned for you in the helloworld directory with support for PostgreSQL as the database and configures Immutant as the web server, which is production-ready and optimized for Clojure applications.

**Note:** If you use MySQL or another database, you can pass it as an option when trying to create a new app.

### Run the Luminus App Locally

Open dev-config.edn and add your Postgres database URL like so:

- username:password is your database user and password.
- helloworld_dev is the database you have created locally.

Next, run lein run migrate to run the database migrations.

Finally, run lein run to launch your app!

Open your browser and go to http://localhost:3000 to see the app.

### Prepare Clojure Luminus App for Deployment

1. We need to add the ceshire library to our dependencies. cheshire is a popular JSON encoding/decoding library in Clojure.

Open your project.clj file and ensure you have the following under :dependencies:

Run the command below in your terminal to ensure it is installed:

2. Create a nixpacks.toml file in the root directory of the app.

The nixpacks.toml file is a configuration file used by Nixpacks, a build system developed and used by Railway, to set up and deploy applications.

In this file, you can specify the instructions for various build and deployment phases, along with environment variables and package dependencies.

Add the following content to the file:

Here, we are specifically instructing Nixpacks to use the following command to start the app.

The command searches for all .jar files in the target directory (where the standalone JAR file is located after the build), excludes any file with "SNAPSHOT" in its name, and passes the selected file to java -jar to run.

It starts by running the JAR file with the migrate option to apply database migrations. Once migrations are complete, it reruns the JAR file to launch the application.

## Deploy the Luminus App to Railway

Railway offers multiple ways to deploy your Clojure app, depending on your setup and preference.

### One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/DsDYI2)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=clojure" target="_blank">variety of Clojure app templates</a> created by the community.

### Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Luminus app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:

   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter DATABASE_URL=${{Postgres.DATABASE_URL}}.
     - The value, ${{Postgres.DATABASE_URL}}, references the URL of your new Postgres database. Learn more about referencing service variables.

   **Note:** Explore the Railway CLI reference for a variety of options.

5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/v1730897279/docs/quick-start/clojure_luminus_on_railway.png"
alt="screenshot of the deployed Clojure service"
layout="responsive"
width={2325} height={2187} quality={100} />

### Deploy From a GitHub Repo

To deploy a Clojure Luminus app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Clojure app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the Luminus app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Clojure apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

lein new luminus helloworld +postgres +immutant

:database-url "postgresql://username:password@127.0.0.1:5432/helloworld_dev"

...
[cheshire "5.10.0"]

lein deps

# nixpacks.toml

[start]
cmd = "java -jar $(find ./target -name '*.jar' ! -name '*SNAPSHOT*') migrate && java -jar $(find ./target -name '*.jar' ! -name '*SNAPSHOT*')"

railway init

# Use the Clojure official image
   # https://hub.docker.com/_/clojure
   FROM clojure:temurin-23-lein-bookworm

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN lein uberjar

   # Run the app by dynamically finding the standalone JAR file in the target/uberjar directory
   CMD ["sh", "-c", "java -jar $(find target/uberjar -name '*.jar' ! -name '*SNAPSHOT*')"]


# Play
Source: https://docs.railway.com/guides/play

Learn how to deploy a Scala Play app to Railway with this step-by-step guide. It covers quick setup, database integration, one-click deploys and other deployment strategies.

This guide covers how to deploy a Scala Play app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Play app!

## Create a Play App

**Note:** If you already have a Play app locally or on GitHub, you can skip this step and go straight to the Deploy Play App to Railway.

To create a new Scala Play app, ensure that you have JDK and sbt installed on your machine.

Run the following command in your terminal to create a new Play app:

A list of templates will be shown to select from. Select the playframework/play-scala-seed.g8 template.

- Give it a name, helloworld.
- Give it an organization name, com.railwayguide
- Hit Enter for the rest to use the latest versions of play, scala and sbt scaffold.

A new Scala Play app will be provisioned in the helloworld directory.

### Modify Scala Play Views and Set Up Database Config

_Step 1_ : Modify the Index File

Open the project in your editor. Head over to the app/views/index.scala.html file.

Modify it to the following:

This change adds a new heading, which you'll see when you run the app locally.

_Step 2_ : Run the App Locally

- Now, letâ€™s run the app locally to verify our changes. You should see the new headers appear in the browser.

_Step 3_ : Add PostgreSQL Driver as a Dependency

Play doesnâ€™t provide built-in database drivers, so we need to add the PostgreSQL JDBC driver manually to our project.

In your build.sbt, add the following dependency:

_Step 4_ : Configure PostgreSQL in application.conf

Next, configure the PostgreSQL database connection in conf/application.conf:

Make sure to replace username and password with your PostgreSQL credentials.

_Step 5_ : Update Project Dependencies

To download the PostgreSQL driver and any updated dependencies, run the following:

_Step 6_ : Add Database Migration Tool (Flyway)

Play doesnâ€™t include built-in support for database migrations, so weâ€™ll use Flyway.

1. Install Flyway Plugin: Open your project/plugin.sbt and add the Flyway plugin:

2. Configure Flyway in build.sbt: Enable Flyway and configure the database connection in your build.sbt:

Replace username with your database username.

_Step 7_ : Create the Migration Files

1. **Create Migration Folder**: Create the folder structure for your migration files:

2. **Create Migration SQL File**: In src/main/resources/db/migration, create a schema migration file called V1_0__create_employees_table.sql with the following content:

_Step 8_ : Run Database Migrations

Once your migration file is in place, run the Flyway migration with the following command:

This will apply the migration and create the employee table in your PostgreSQL database.

Check your database to confirm that the employee table has been successfully created. You can use a database tool like psql or any PostgreSQL client to view the table.

### Run the Play App locally

Next, run sbt run in the terminal to build the project, install all the dependencies and start the embedded Pekko HTTP server.

Open your browser and go to http://localhost:9000 to see the app.

### Prepare Scala Play App for deployment

1. **Set Application Secret**:
   - Open up the application.conf file and add the following to it to set the app's secret.
     
2. **Set Database URL**:
   - Open up the application.conf file and add the following to it to ensure the DATABASE_URL is read from the environment variable.
     
3. **Set Allowed Hosts**:
   - By default, Play ships with a list of default Allowed Hosts filter. This is the list of allowed valid hosts = ["localhost", ".local", "127.0.0.1"]. You need to add an option to allow Railway hosts, [".up.railway.app"].
   - Add the following to the application.conf file:
     scala
    play.filters.hosts.allowed=[".up.railway.app"]
    
     **Note:** Railway provided domains end in .up.railway.app. Once you add your custom domain, please update the allowed hosts to the new URL.
4. **Add sbt-native-packager sbt plugin**:

   - Add the sbt-native-packager sbt plugin to project/plugins.sbt
     
   - Enable the JavaAppPackaging plugin in build.sbt and set the executableScriptName to main. Your build.sbt should be looking like this now:

   - Run sbt update to install the sbt-native-packager and update the dependencies.

Now, we are ready to deploy to Railway!

## Deploy the Play App to Railway

Railway offers multiple ways to deploy your Scala app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/my9q_q)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=scala" target="_blank">variety of Scala app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Luminus app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Add a Postgres Database Service**:
   - Run railway add -d postgres.
   - Hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
4. **Add a Service and Environment Variable**:

   - Run railway add.
   - Select Empty Service from the list of options.
   - In the Enter a service name prompt, enter app-service.
   - In the Enter a variable prompt, enter APPLICATION_SECRET=<generated-app-secret> where <generated-app-secret> is the secret generated from running playGenerateSecret in your terminal.
   - In the Enter a variable prompt, enter DATABASE_URL=${{Postgres.DATABASE_URL}}.
     - The value, ${{Postgres.DATABASE_URL}}, references the URL of your new Postgres database. Learn more about referencing service variables.

   **Note:** Explore the Railway CLI reference for a variety of options.

5. **Deploy the Application**:
   - Run railway up to deploy your app.
     - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment is complete, we can proceed to generate a domain for the app service.
6. **Set Up a Public URL**:
   - Run railway domain to generate a public URL for your app.
   - Visit the new URL to see your app live in action!

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731046089/docs/quick-start/scala_on_railway.png"
alt="screenshot of the deployed Scala service"
layout="responsive"
width={1676} height={1490} quality={100} />

### Deploy from a GitHub Repo

To deploy a Scala Play app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**.
     - This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - APPLICATION_SECRET: Set the value to the generated app secret.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Scala app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the Play app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Scala apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

sbt new

@()

@main("Welcome to Play") {
  <h1>Welcome to Play!</h1>
  <h1>Hello World, Railway!</h1>
}

libraryDependencies += "org.postgresql" % "postgresql" % "42.7.4" // Always use the latest stable version

# Default database configuration using PostgreSQL
db.default.driver = org.postgresql.Driver
db.default.url = "jdbc:postgresql://username:password@127.0.0.1:5432/scala_play"  # Replace with correct credentials

sbt update

addSbtPlugin("io.github.davidmweber" % "flyway-sbt" % "7.4.0")

name := """helloworld"""
organization := "com.railwayguide"
version := "1.0-SNAPSHOT"
executableScriptName := "main"

lazy val root = (project in file(".")).enablePlugins(PlayScala).enablePlugins(FlywayPlugin)

scalaVersion := "2.13.15"

libraryDependencies += guice
libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "7.0.1" % Test
libraryDependencies += "org.postgresql" % "postgresql" % "42.7.4" // Latest version

flywayUrl := "jdbc:postgresql://127.0.0.1:5432/scala_play?user=<username>"  # Replace with correct credentials
flywayLocations := Seq("filesystem:src/main/resources/db/migration")

src/main/resources/db/migration

CREATE TABLE employee (
  id VARCHAR(20) PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  email VARCHAR(30),
  admin BOOLEAN
);

sbt flywayMigrate

play.http.secret.key=${?APPLICATION_SECRET}

db.default.url="jdbc:${?DATABASE_URL}"

addSbtPlugin("com.github.sbt" % "sbt-native-packager" % "x.x.x")

name := """helloworld"""
     organization := "com.railwayguide"

     version := "1.0-SNAPSHOT"

     executableScriptName := "main"

     lazy val root = (project in file(".")).enablePlugins(PlayScala).enablePlugins(JavaAppPackaging).enablePlugins(FlywayPlugin)

     scalaVersion := "2.13.15"

     libraryDependencies += guice
     libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "7.0.1" % Test
     libraryDependencies += "org.postgresql" % "postgresql" % "42.7.4" // Always use the latest stable version

     flywayUrl := sys.env.getOrElse("DATABASE_URL", "jdbc:postgresql://127.0.0.1:5432/scala_play?user=username")

     flywayLocations := Seq("filesystem:src/main/resources/db/migration")

railway init

# Use the Scala sbt official image
   # https://hub.docker.com/r/sbtscala/scala-sbt/tags
   FROM sbtscala/scala-sbt:eclipse-temurin-21.0.5_11_1.10.5_3.5.2

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN sbt stage

   # Run the app
   CMD ["./target/universal/stage/bin/main"]


# Sails
Source: https://docs.railway.com/guides/sails

Learn how to deploy a Sails app to Railway with this step-by-step guide. It covers quick setup, database integration, the Boring JavaScript stack, one-click deploys and other deployment strategies.

Sails makes it easy to build custom, enterprise-grade Node.js apps.

## Create a Sails App

**Note:** If you already have a Sails app locally or on GitHub, you can skip this step and go straight to the Deploy Sails App on Railway.

To create a new Sails app, ensure that you have Node installed on your machine.

Run the following command in your terminal to install Sails:

Next, run the command below to create a new Sails app

Select Web App as the template for your new Sails app. Once the dependencies have been installed, cd into the workapp directory and run sails lift to start your app.

Open your browser and go to http://localhost:1337 to see your app.

Now, let's deploy to Railway!

## Deploy Sails App on Railway

Railway offers multiple ways to deploy your Sails app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Sails app along with a Postgres database and Redis.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/t3sAEH)

After deploying, we recommend that you eject from the template to create a copy of the repository under your own GitHub account. This will give you full control over the source code and project.

## Deploy from the CLI

To deploy the Sails app using the Railway CLI, please follow the steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Sails app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Modify Sails Config**:
   - Open up config/env/production.js file and make some changes:
     - Set http.trustProxy to true because our app will be behind a proxy.
     - Set session.cookie.secure to true
     - Add this function to the socket object just after the onlyAllowOrigins array:
       
       **Note:** We only added this because we don't need sockets now. If you do, skip this step and add your public app URL to the onlyAllowOrigins array. The function simply rejects socket connection attempts.
4. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.

- **Note:** You'll come across an error about how the default sails-disk adapter and connect.session() MemoryStore is not designed for use as a production database, donâ€™t worry. Weâ€™ll fix this in the next step.

5. **Add PostgreSQL & Redis Database Services**:
   - Run railway add.
   - Select PostgreSQL by pressing space
   - Select Redis by also pressing space and hit **Enter** to add both database services to your project.
6. **Modify Sails Database Config**:
   - Open up config/env/production.js file and make some changes to let your app know what database to connect to and where to save sessions:
     - In the datastores: section,
       - Add adapter: 'sails-postgresql',
       - Add url: process.env.DATABASE_URL
     - In the session: section,
       - Add adapter: '@sailshq/connect-redis',
       - Add url: process.env.REDIS_URL,
   - Run npm install sails-postgresql --save to add the new adapter to your app locally.
7. **Configure Environment Variables on Railway**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - REDIS_URL: Set the value to ${{Redis.REDIS_URL}} (this references the URL of your new Redis Database)
   - Use the **Raw Editor** to add any other required environment variables in one go.
8. **Redeploy the Service**:
   - Click **Deploy** on the Railway dashboard to apply your changes.
9. **Upload Local Changes**:
   - Run railway up to upload all the changes we made locally and redeploy our service.
10. **Verify the Deployment**:
    - Once the deployment completes, go to **View logs** to check if the server is running successfully.
11. **Set Up a Public URL**:
    - Navigate to the **Networking** section under the Settings tab of your new service.
    - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1728580600/docs/quick-start/new_sails_service.png"
alt="screenshot of the deployed Sails service"
layout="responsive"
width={2986} height={2140} quality={100} />

## Deploy from a GitHub Repo

To deploy the Sails app to Railway, start by pushing the app to a GitHub repo. Once thatâ€™s set up, follow the steps below to complete the deployment process.

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables**:
   - Click **Add Variables** and configure all the necessary environment variables for your app.
4. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
5. **Add a Database Service**:
   - Right-click on the Railway project canvas or click the **Create** button.
   - Select **Database**.
   - Select **Add PostgreSQL** from the available databases.
     - This will create and deploy a new Postgres database service for your project.
6. **Add a Redis Database Service**:
   - Right-click on the Railway project canvas or click the **Create** button.
   - Select **Database**.
   - Select **Add Redis** from the available databases.
     - This will create and deploy a new Redis database service for your project.
7. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - REDIS_URL: Set the value to ${{Redis.REDIS_URL}} (this references the URL of your new Redis Database)
   - Use the **Raw Editor** to add any other required environment variables in one go.
8. **Modify Sails Config**:
   - Follow steps 3 & 5 mentioned in the CLI guide.
9. **Redeploy the Service**:
   - Click **Deploy** on the Railway dashboard to apply your changes.
10. **Verify the Deployment**:
    - Once the deployment completes, go to **View logs** to check if the server is running successfully.
11. **Set Up a Public URL**:
    - Navigate to the **Networking** section under the Settings tab of your new service.
    - Click Generate Domain to create a public URL for your app.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Sails apps effortlessly!

Hereâ€™s how your setup should look:

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1728580319/docs/quick-start/all_services_connected.png" alt="Diagram showing all sails services connected on Railway" layout="responsive" width={2985} height={1815} quality={100} />

By following these steps, youâ€™ll have a fully functional Sails app. If you run into any issues or need to make adjustments, check the logs and revisit your environment variable configurations.

## The Boring JavaScript Stack Sails Starter

If you're a fan of The Boring JavaScript Stack, weâ€™ve got a one-click deploy option for you.

Simply click the button below to get started:

![Deploy on Railway](https://railway.com/new/template/ia84_3)

**Note:** After deploying, we recommend ejecting from the template to create your own GitHub repository. This will give you full control over the project and source code.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

npm install sails -g

sails new workapp

railway init

beforeConnect: function(handshake, proceed) {
         // Send back `true` to allow the socket to connect.
         // (Or send back `false` to reject the attempt.)
         return proceed(undefined, false);
       },

railway up


# Django
Source: https://docs.railway.com/guides/django

Learn how to deploy a Python Django app to Railway with this step-by-step guide. It covers quick setup, database integration, private networking, Celery, one-click deploys and other deployment strategies.

Itâ€™s free, open-source, and comes with a range of features to streamline tasks like authentication, routing, and database management, so developers can focus on building their applications without handling everything from scratch.

## Create a Django App

**Note:** If you already have a Django app locally or on GitHub, you can skip this step and go straight to the Deploy Django App on Railway.

To create a new Django app, ensure that you have Python and Django installed on your machine.

Follow the steps below to set up the project in a directory.

Create a virtual environment

Activate the virtual environment

**Note:** For windows developers, run it as env\Scripts\activate in your terminal.

Install Django

Once everything is set up, run the following command in your terminal to provision a new Django project:

This command will create a new Django project named liftoff.

Next, cd into the directory and run python manage.py runserver to start your project.

Open your browser and go to http://127.0.0.1:8000 to see the project. You'll see the Django welcome page with a "The install worked successfully! Congratulations!" paragraph.

**Note:** You'll see a red notice about unapplied migration(s). You can ignore them for now. We'll run them when we deploy the project.

Now that your app is running locally, letâ€™s move on to make some changes and install some dependencies before deployment.

## Configure Database, Static Files & Dependencies

1. Install the following packages within the liftoff directory, where you can see the manage.py file.

whitenoise is a Python package for serving static files directly from your web app. It serves compressed content and sets far-future cache headers on content that won't change.

gunicorn is a production ready web server.

pyscog is python package that allows Django work with Postgresql.

2. Import the os module:

Open the liftoff/settings.py file located in the inner liftoff directory (the one containing the main project settings).

At the top of the file, add the following line to import the os module, placing it just before the Path import:

3. Configure the database and run migrations:

A fresh Django project uses SQLite by default, but we need to switch to PostgreSQL.

Create a database named liftoff_dev in your local Postgres instance.

Open the liftoff/settings.py file. In the Database section, replace the existing configuration with:

Replace the values of PGUSER, PGPASSWORD with your local credentials.

Run python manage.py migrate in your terminal to apply the database migrations. Once it completes successfully, check your database. You should see the auth and other Django tables created.

4. Static files configuration:

We'll configure Django to serve static files using WhiteNoise.

Open liftoff/settings.py and configure the static files settings:

Add the WhiteNoise middleware in the **MIDDLEWARE** section, just below the security middleware:

5. Update ALLOWED_HOSTS settings:

This setting represents the list of all the host/domain names our Django project can serve.

6. Create a **static** folder:

Inside your liftoff directory, create a static folder where all static assets will reside.

7. Create a requirements.txt file:

To track all the dependencies for deployment, create a requirements.txt file:

**Note:** It's only safe to run the command above in a virtual environment, else it will freeze all python packages installed on your system.

With these changes, your Django app is now ready to be deployed to Railway!

## Deploy Django App on Railway

Railway offers multiple ways to deploy your Django app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Django app along with a Postgres database.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/GB6Eki)

After deploying, we recommend that you eject from the template to create a copy of the repository under your own GitHub account. This will give you full control over the source code and project.

## Deploy From the CLI

To deploy the Django app using the Railway CLI, please follow the steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Django app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:

   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.

   **Note:** You'll encounter an error about the PGDATABASE environment not set. Don't worry, we'll fix that in the next steps.

4. **Add a Database Service**:
   - Run railway add.
   - Select PostgreSQL by pressing space and hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
5. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - PGDATABASE: Set the value to ${{Postgres.PGDATABASE}} (this references the Postgres database name). Learn more about referencing service variables.
     - PGUSER: Set the value to ${{Postgres.PGUSER}}
     - PGPASSWORD: Set the value to ${{Postgres.PGPASSWORD}}
     - PGHOST: Set the value to ${{Postgres.PGHOST}}
     - PGPORT: Set the value to ${{Postgres.PGPORT}}
   - Use the **Raw Editor** to add any other required environment variables in one go.
6. **Redeploy the App Service**:
   - Click **Deploy** on the app service on the Railway dashboard to apply your changes.
7. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
8. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/v1729121823/docs/quick-start/django_app.png"
alt="screenshot of the deployed Django project"
layout="responsive"
width={2783} height={2135} quality={100} />

## Deploy From a GitHub Repo

To deploy the Django app to Railway, start by pushing the app to a GitHub repo. Once thatâ€™s set up, follow the steps below to complete the deployment process.

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables**:

   - Click **Add Variables** and configure all the necessary environment variables for your app.
     - PGDATABASE: Set the value to ${{Postgres.PGDATABASE}} (this references the Postgres database name). Learn more about referencing service variables.
     - PGUSER: Set the value to ${{Postgres.PGUSER}}
     - PGPASSWORD: Set the value to ${{Postgres.PGPASSWORD}}
     - PGHOST: Set the value to ${{Postgres.PGHOST}}
     - PGPORT: Set the value to ${{Postgres.PGPORT}}

   **Note:** We don't have the Postgres Database service yet. We'll add that soon.

4. **Add a Database Service**:
   - Right-click on the Railway project canvas or click the **Create** button.
   - Select **Database**.
   - Select **Add PostgreSQL** from the available databases.
     - This will create and deploy a new Postgres database service for your project.
5. **Deploy the App**:
   - Click **Deploy** to start the deployment process and apply all changes.
   - Once deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
6. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Django app.

7. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Django apps effortlessly!

**Note:** The next step shows how to configure and run your Django app along with Celery and Celery beat.

## Set Up Database, Migrations, Celery Beat and Celery

This setup deploys your Django app on Railway, ensuring that your database, scheduled tasks (crons)--Celery Beat, and queue workers (Celery) are all fully operational.

The deployment structure follows a "majestic monolith" architecture, where the entire Django app is managed as a single codebase but split into four separate services on Railway:

- **App Service**: Handles HTTP requests and user interactions.
- **Cron Service**: Manages scheduled tasks (e.g., sending emails or running reports) using Celery Beat.
- **Worker Service**: Processes background jobs from the queue using Celery.
- **Database Service**: Stores and retrieves your application's data.

<Image src="https://res.cloudinary.com/railway/image/upload/v1731604331/docs/quick-start/deployed_django_app_architecture.png"
alt="screenshot of the deploy architecture of the Django app"
layout="responsive"
width={3237} height={1951} quality={100} />
_My Monolith Django app_

**Note:** This guide follows the assumption that you have installed Celery and Celery Beat in your app, the broker uses Redis and you already have a Postgres database service provisioned for your app as shown earlier.

Please follow these steps to get it setup on Railway:

1. Create a Redis Database service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a> by clicking the **Create** button. Then select **Database** and choose **Add Redis**.
   - Click on **Deploy**.
2. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a> by clicking the **Create** button. Then select **Empty service**.
   - Name the service **App Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a> to configure it.
     - **Note:** If you followed the guide from the beginning, simply rename the existing service to **App Service**.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Go to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables required for the Django app especially the ones listed below.
     - REDIS_URL: Set the value to ${{Postgres.REDIS_URL}}
     - PGUSER: Set the value to ${{Postgres.PGUSER}}
     - PGPASSWORD: Set the value to ${{Postgres.PGPASSWORD}}
     - PGHOST: Set the value to ${{Postgres.PGHOST}}
     - PGPORT: Set the value to ${{Postgres.PGPORT}}
     - PGDATABASE: Set the value to ${{Postgres.PGDATABASE}} (this references the Postgres database name). Learn more about referencing service variables.
   - Click **Deploy**.
3. Create a new service on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a> by clicking the **Create** button. Then select **Empty service**.
   - Name the service **Cron Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Add celery -A liftoff beat -l info --concurrency=3 to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.
     - _Note:_ liftoff is the name of the app. You can find the app name in your Django projectâ€™s main folder, typically in the directory containing settings.py.
     - The --concurrency=3 option here means it can process up to 3 tasks in parallel. You can adjust the concurrency level based on your system resources. The higher the level, the more memory and resources it consumes.
   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables especially those highlighted already in step 2.
   - Click **Deploy**.
4. Create a new service again on the <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>.
   - Name the service **Worker Service**, and click on <a href="/overview/the-basics#service-settings">**Settings**</a>.
   - Connect your GitHub repo to the **Source Repo** in the **Source** section.
   - Add celery -A liftoff worker -l info --concurrency=3 to the <a href="/guides/start-command">**Custom Start Command**</a> in the **Deploy** section.
     - _Note:_ liftoff is the name of the app. You can find the app name in your Django projectâ€™s main folder, typically in the directory containing settings.py.
     - The --concurrency=3 option here means it can process up to 3 tasks in parallel. You can adjust the concurrency level based on your system resources. The higher the level, the more memory and resources it consumes.
   - Head back to the top of the service and click on <a href="/overview/the-basics#service-variables">**Variables**</a>.
   - Add all the necessary environment variables especially those highlighted already in step 2.
   - Click **Deploy**.

At this point, you should have all services deployed and connected to the Postgres and Redis Database service:

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731604331/docs/quick-start/deployed_django_app_architecture.png"
alt="screenshot of the deploy architecture of the Django app"
layout="responsive"
width={3237} height={1951} quality={100} />

- **Cron Service**: This service should run Celery Beat Scheduler to manage scheduled tasks.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731605926/docs/quick-start/django_cron_service.png"
alt="screenshot of the cron service of the Django app"
layout="responsive"
width={2766} height={2056} quality={100} />

- **Worker Service**: This service should be running Celery and ready to process jobs from the queue.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1731605981/docs/quick-start/django_worker_service.png"
alt="screenshot of the worker service of the Django app"
layout="responsive"

width={2752} height={2094} quality={100} />

- **App Service**: This service should be running and is the only one that should have a public domain, allowing users to access your application.

**Note:** There is a community template available that demonstrates this deployment approach. You can easily deploy this template and then connect it to your own GitHub repository for your application.

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

python -m venv env

source env/bin/activate

python -m pip install django

django-admin startproject liftoff

python -m pip install gunicorn whitenoise psycopg[binary,pool]

import os
from pathlib import Path

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Set default values for the environment variables if theyâ€™re not already set
os.environ.setdefault("PGDATABASE", "liftoff_dev")
os.environ.setdefault("PGUSER", "username")
os.environ.setdefault("PGPASSWORD", "")
os.environ.setdefault("PGHOST", "localhost")
os.environ.setdefault("PGPORT", "5432")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ALLOWED_HOSTS = ["*"]

pip freeze > requirements.txt

railway init

railway up


# Angular
Source: https://docs.railway.com/guides/angular

Learn how to deploy an Angular app to Railway with this step-by-step guide. It covers quick setup, caddy server setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy an Angular app to Railway in four ways:

1. One-click deploy from a template
2. From a GitHub repository
3. Using the CLI
4. Using a Dockerfile

Now, let's create an Angular app!

## Create an Angular App

**Note:** If you already have an Angular app locally or on GitHub, you can skip this step and go straight to the Deploy Angular App on Railway.

To create a new Angular app, ensure that you have Node and Angular CLI installed on your machine.

Run the following command in your terminal to create a new Angular app:

You'll be presented with some config options in the prompts for your project.

- Select CSS
- Select Yes for enabling Server-Side Rendering (SSR) and Static Site Generation (SSG)
- Select Yes for enabling Server Routing and App Engine APIs (Developer Preview)

### Run the Angular App locally

Next, cd into the directory and run the app.

Open your browser and go to http://localhost:4200 to see your app.

## Modify Start Script

Before deploying, we need to update the package.json file.

Angular builds the project into the dist directory. For server-side rendered apps, the server starts with the command: node dist/gratitudeapp/server/server.mjs as defined in the scripts section below:

- The development server starts with npm start.
- The production server runs with npm run serve:ssr:gratitudeapp.

Since Railway relies on the build and start scripts to automatically build and launch applications, we need to update the start script to ensure it runs the production server correctly.

Your scripts section should look like this:

Now, we are good to go!

## Deploy the Angular App to Railway

Railway offers multiple ways to deploy your Angular app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/A5t142)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=angular" target="_blank">variety of Angular app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Angular app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/v1741028014/CleanShot_2025-03-03_at_18.49.07_2x_ewelfy.png"
alt="screenshot of the deployed Angular service"
layout="responsive"
width={2644} height={2114} quality={100} />

### Deploy from a GitHub Repo

To deploy an Angular app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the gratitudeapp or Angular app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Angular apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

ng new gratitudeapp

npm start

"scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "serve:ssr:gratitudeapp": "node dist/gratitudeapp/server/server.mjs"
  },

...
"scripts": {
    "ng": "ng",
    "dev": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "start": "node dist/gratitudeapp/server/server.mjs"
  },
...

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Serve the app
   CMD ["npm", "run", "start"]


# React
Source: https://docs.railway.com/guides/react

Learn how to deploy a React app to Railway with this step-by-step guide. It covers quick setup, caddy server setup, one-click deploys and other deployment strategies.

React simplifies the process of creating interactive and dynamic UIs by breaking them down into reusable components.

This guide covers how to deploy a React app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a React app!

## Create a React App

**Note:** If you already have a React app locally or on GitHub, you can skip this step and go straight to the Deploy React App on Railway.

To create a new React app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new React app using Vite:

A new React app will be provisioned for you in the helloworld directory.

### Run the React App locally

Next, cd into the directory and install the dependencies.

Start the Vite development server by running the following command:

Open your browser and go to http://localhost:5173 to see your app.

## Deploy the React App to Railway

Railway offers multiple ways to deploy your React app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a React app with Caddy to serve the dist folder.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/NeiLty)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=react" target="_blank">variety of React app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your React app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729182225/docs/quick-start/vite_react_app.png"
alt="screenshot of the deployed React service"
layout="responsive"
width={2431} height={2051} quality={100} />

### Deploy from a GitHub Repo

To deploy a React app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or React app's root directory.
2. Add the content below to the Dockerfile:

   The Dockerfile will use Caddy to serve the React app.

3. Add a Caddyfile to the app's root directory:

4. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your React apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npm create vite@latest helloworld -- --template react

npm install

npm run dev

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine AS build

   # Set config
   ENV NPM_CONFIG_UPDATE_NOTIFIER=false
   ENV NPM_CONFIG_FUND=false

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Use the Caddy image
   FROM caddy

   # Create and change to the app directory.
   WORKDIR /app

   # Copy Caddyfile to the container image.
   COPY Caddyfile ./

   # Copy local code to the container image.
   RUN caddy fmt Caddyfile --overwrite

   # Copy files to the container image.
   COPY --from=build /app/dist ./dist

   # Use Caddy to run/serve the app
   CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]

# global options
   {
       admin off # there's no need for the admin api in railway's environment
       persist_config off # storage isn't persistent anyway
       auto_https off # railway handles https for us, this would cause issues if left enabled
       # runtime logs
       log {
           format json # set runtime log format to json mode
       }
       # server options
       servers {
           trusted_proxies static private_ranges 100.0.0.0/8 # trust railway's proxy
       }
   }

   # site block, listens on the $PORT environment variable, automatically assigned by railway
   :{$PORT:3000} {
       # access logs
       log {
           format json # set access log format to json mode
       }

       # health check for railway
       rewrite /health /*

       # serve from the 'dist' folder (Vite builds into the 'dist' folder)
       root * dist

       # enable gzipping responses
       encode gzip

       # serve files from 'dist'
       file_server

       # if path doesn't exist, redirect it to 'index.html' for client side routing
       try_files {path} /index.html
   }


# Remix
Source: https://docs.railway.com/guides/remix

Learn how to deploy a Remix app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Remix app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Remix app!

## Create a Remix App

**Note:** If you already have a Remix app locally or on GitHub, you can skip this step and go straight to the Deploy Remix App on Railway.

To create a new Remix app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new Remix app:

Follow the prompts by giving a directory name, like helloworld, where you want your app to be set up. When asked, select **Yes** to automatically install all the necessary dependencies.

A new Remix app will be provisioned for you in the helloworld directory.

### Run the Remix App locally

Start the Vite development server by running the following command:

Open your browser and go to http://localhost:5173 to see your app.

## Deploy the Remix App to Railway

Railway offers multiple ways to deploy your Remix app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/remix)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=remix" target="_blank">variety of Remix app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Vue app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729528294/remix_app_on_railway.png"
alt="screenshot of the deployed Remix service"
layout="responsive"
width={2266} height={2040} quality={100} />

### Deploy from a GitHub Repo

To deploy a Remix app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Remix app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Remix apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npx create-remix@latest

npm run dev

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Serve the app
   CMD ["npm", "run", "start"]


# Vue
Source: https://docs.railway.com/guides/vue

Learn how to deploy a Vue app to Railway with this step-by-step guide. It covers quick setup, caddy server setup, one-click deploys, Dockerfile and other deployment strategies.

Vue prides itself as **The Progressive JavaScript Framework**.

This guide covers how to deploy a Vue app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Vue app!

## Create a Vue App

**Note:** If you already have a Vue app locally or on GitHub, you can skip this step and go straight to the Deploy Vue App on Railway.

To create a new Vue app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new Vue app using Vite:

You'll be presented with choices for different options in the prompts. Give the app a name, helloworld and answer Yes to the other options or select what you want.

A new Vue app will be provisioned for you in the helloworld directory.

### Run the Vue App locally

Next, cd into the directory and install the dependencies.

Start the Vite development server by running the following command:

Open your browser and go to http://localhost:5173 to see your app.

## Deploy the Vue App to Railway

Railway offers multiple ways to deploy your Vue app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Vue app with Caddy to serve the dist folder.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/Qh0OAU)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=vue" target="_blank">variety of Vue app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Vue app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729252336/docs/quick-start/vue_app_on_railway.png"
alt="screenshot of the deployed Vue service"
layout="responsive"
width={2642} height={2080} quality={100} />

### Deploy from a GitHub Repo

To deploy a Vue app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Vue app's root directory.
2. Add the content below to the Dockerfile:

   The Dockerfile will use Caddy to serve the Vue app.

3. Add a Caddyfile to the app's root directory:

4. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Vue apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npm create vue@latest

npm install

npm run dev

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine AS build

   # Set config
   ENV NPM_CONFIG_UPDATE_NOTIFIER=false
   ENV NPM_CONFIG_FUND=false

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Use the Caddy image
   FROM caddy

   # Create and change to the app directory.
   WORKDIR /app

   # Copy Caddyfile to the container image.
   COPY Caddyfile ./

   # Copy local code to the container image.
   RUN caddy fmt Caddyfile --overwrite

   # Copy files to the container image.
   COPY --from=build /app/dist ./dist

   # Use Caddy to run/serve the app
   CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]

# global options
   {
       admin off # there's no need for the admin api in railway's environment
       persist_config off # storage isn't persistent anyway
       auto_https off # railway handles https for us, this would cause issues if left enabled
       # runtime logs
       log {
           format json # set runtime log format to json mode
       }
       # server options
       servers {
           trusted_proxies static private_ranges 100.0.0.0/8 # trust railway's proxy
       }
   }

   # site block, listens on the $PORT environment variable, automatically assigned by railway
   :{$PORT:3000} {
       # access logs
       log {
           format json # set access log format to json mode
       }

       # health check for railway
       rewrite /health /*

       # serve from the 'dist' folder (Vite builds into the 'dist' folder)
       root * dist

       # enable gzipping responses
       encode gzip

       # serve files from 'dist'
       file_server

       # if path doesn't exist, redirect it to 'index.html' for client side routing
       try_files {path} /index.html
   }


# Nuxt
Source: https://docs.railway.com/guides/nuxt

Learn how to deploy a Nuxt app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

Nuxt is known as **The Intuitive Vue Framework** because it simplifies building Vue.js applications with features like server-side rendering and easy routing.

This guide covers how to deploy a Nuxt app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Nuxt app!

## Create a Nuxt App

**Note:** If you already have a Nuxt app locally or on GitHub, you can skip this step and go straight to the Deploy Nuxt App on Railway.

To create a new Nuxt app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new Nuxt app:

A new Nuxt app will be provisioned for you in the helloworld directory.

### Run the Nuxt App locally

Next, cd into the directory and start the development server by running the following command:

Open your browser and go to http://localhost:3000 to see your app.

## Deploy the Nuxt App to Railway

Railway offers multiple ways to deploy your Nuxt app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/lQQgLR)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=nuxt" target="_blank">variety of Nuxt app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Vue app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Modify Package.json Config**:

   - By default, Nuxt doesn't add a start script in the package.json file. We'll need to add that to instruct Railway on how to run our app.

   - Add "start":"node .output/server/index.mjs" to the package.json file.

   **package.json**

   **Note:** Railway uses Nixpacks to build and deploy your code with zero configuration. The Nixpack Node provider will pick up the start script in the package.json file and use it to serve the app.

4. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729262446/docs/quick-start/nuxt_app.png"
alt="screenshot of the deployed Nuxt service"
layout="responsive"
width={2383} height={2003} quality={100} />

### Deploy from a GitHub Repo

To deploy a Nuxt app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Modify Package.json Config**:
   - Follow step 3 mentioned in the CLI guide
3. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
4. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
5. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Nuxt app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Nuxt apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npx nuxi@latest init helloworld

npm run dev

railway init

{
       "name": "nuxt-app",
       "private": true,
       "type": "module",
       "scripts": {
           "build": "nuxt build",
           "dev": "nuxt dev",
           "start": "node .output/server/index.mjs",
           "generate": "nuxt generate",
           "preview": "nuxt preview",
           "postinstall": "nuxt prepare"
       },
       "dependencies": {
           "nuxt": "^3.13.0",
           "vue": "latest",
           "vue-router": "latest"
       }
   }

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine AS build

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Copy files to the container image.
   COPY --from=build /app ./

   # Serve the app
   CMD ["npm", "run", "start"]


# Spring Boot
Source: https://docs.railway.com/guides/spring-boot

Learn how to deploy a Spring Boot app to Railway with this step-by-step guide. It covers quick setup, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy a Spring Boot app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Spring Boot app!

## Create a Spring Boot App

**Note:** If you already have a Spring Boot app locally or on GitHub, you can skip this step and go straight to the Deploy Spring Boot App to Railway.

To create a new Spring Boot app, ensure that you have JDK installed on your machine.

Go to start.spring.io to initialize a new Spring Boot app. Select the options below to customize and generate your starter app.

- Project: Maven
- Language: Java
- Spring Boot: 3.3.4
- Project Metadata:
  - Group: com.railwayguide
  - Artifact: helloworld
  - Name: helloworld
  - Description: Demo project for Railway Guide
  - Package name: com.railwayguide.helloworld
  - Packaging: jar
  - Java: 17
- Dependencies:
  - Click the **Add Dependencies** button and search for **Spring Web**. Select it.

!Spring Boot App Initializer
_Config to initialize our new app_

Now, click on the **Generate** button, download the zipped file and unpack it into a folder on your machine.

### Modify the Application File

Next, open the app in your IDE and navigate to the src/main/java/com/railwayguide/helloworld/HelloWorldApplication.java file.

Replace the content with the code below:

We added a hello() method that returns the response: Hello world from Java Spring Boot!.

The @RestController annotation designates this class as a web controller, while @GetMapping("/") maps the hello() method to handle requests sent to the root URL, /.

### Run the Spring Boot App locally

Next, cd into the helloworld directory via the terminal and run the following Maven command:

**Note:** This is a Maven wrapper for Linux and macOS, which uses a bundled version of Maven from **.mvn/wrapper/maven-wrapper.jar** instead of relying on the system-installed version.

Open your browser and go to http://localhost:8080 to see your app.

## Deploy the Spring Boot App to Railway

Railway offers multiple ways to deploy your Spring Boot app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/-NFGrr)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=spring boot" target="_blank">variety of Spring Boot app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Spring Boot app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729621960/springboot_service_on_railway.png"
alt="screenshot of the deployed Spring Boot service"
layout="responsive"
width={2172} height={1590} quality={100} />

### Deploy from a GitHub Repo

To deploy a Spring Boot app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s a Java app.

5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the helloworld or Spring Boot app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Spring Boot apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

package com.railwayguide.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class HelloworldApplication {

	public static void main(String[] args) {
		SpringApplication.run(HelloworldApplication.class, args);
	}

	@GetMapping("/")
    public String hello() {
      return String.format("Hello world from Java Spring Boot!");
    }

}

./mvnw spring-boot:run

railway init

railway up

# Use the Eclipse temurin alpine official image
   # https://hub.docker.com/_/eclipse-temurin
   FROM eclipse-temurin:21-jdk-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN ./mvnw -DoutputFile=target/mvn-dependency-list.log -B -DskipTests clean dependency:list install

   # Run the app by dynamically finding the JAR file in the target directory
   CMD ["sh", "-c", "java -jar target/*.jar"]


# Astro
Source: https://docs.railway.com/guides/astro

Learn how to deploy an Astro app to Railway with this step-by-step guide. It covers quick setup, server side rendering, one-click deploys, Dockerfile and other deployment strategies.

This guide covers how to deploy an Astro app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create an Astro app!

## Create an Astro App

**Note:** If you already have an Astro app locally or on GitHub, you can skip this step and go straight to the Deploy Astro Apps on Railway.

To create a new Astro app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new Astro app:

Follow the prompts and provide a directory name, such as blog, where you'd like to set up your app.

When prompted to choose how you'd like to start your project, select **Use blog template**. For TypeScript, choose **Yes**.

For the remaining options, select the defaults and press Enter. All necessary dependencies will then be installed.

A new Astro app will be provisioned for you in the blog directory.

### Run the Astro App Locally

Enter your project directory using cd blog.

Start the local dev server by running the following command:

Open your browser and go to http://localhost:4321 to see your app.

### Enable Server Side Rendering (SSR)

Astro has several SSR adapters. These adapters are used to run your project on the server and handle SSR requests.

Let's add the Node adapter to enable SSR in our blog project.

Run the command below in your terminal:

Select **Yes** at the prompt to proceed. The Node adapter will be installed, and our Astro config file will be updated accordingly.

Open up the astro.config.mjs file:

In the config file, output is set to server, meaning every page in the app is server-rendered by default.

For mostly static sites, set output to hybrid. This allows you to add export const prerender = false to any file that needs to be server-rendered on demand.

### Modify Start Script and Astro Config

Astro builds your project into a dist directory. In standalone mode, a server starts when the server entry point is executed, which is by default located at ./dist/server/entry.mjs.

In this mode, the server handles file serving as well as page and API routes.

Open up the package.json file and modify the start script from astro dev to node ./dist/server/entry.mjs.

Open the astro.config.mjs file and configure the server to run on host 0.0.0.0 by adding the following block inside the defineConfig function.

Your app needs to listen on either 0.0.0.0 or :: to accept traffic. If not configured properly, you'll encounter a 502 error.

## Deploy the Astro App to Railway

Railway offers multiple ways to deploy your Astro app, depending on your setup and preference.

### One-Click Deploy From a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/Ic0JBh)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=astro" target="_blank">variety of Astro app templates</a> created by the community.

### Deploy From the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Vue app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1729535599/astro_blog_app.png"
alt="screenshot of the deployed Astro service"
layout="responsive"
width={2556} height={2164} quality={100} />

### Deploy From a GitHub Repo

To deploy an Astro app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the blog or Astro app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Astro apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npm create astro@latest

npm run dev

npx astro add node

// @ts-check
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";

import sitemap from "@astrojs/sitemap";

import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
  site: "https://example.com",
  integrations: [mdx(), sitemap()],
  output: "server",

  adapter: node({
    mode: "standalone",
  }),
});

{
    "name": "astroblog",
    "type": "module",
    "version": "0.0.1",
    "scripts": {
        "dev": "astro dev",
        "start": "node ./dist/server/entry.mjs",
        "build": "astro check && astro build",
        "preview": "astro preview",
        "astro": "astro"
    },
    "dependencies": {
        "@astrojs/check": "^0.9.4",
        "@astrojs/mdx": "^3.1.8",
        "@astrojs/node": "^8.3.4",
        "@astrojs/rss": "^4.0.9",
        "@astrojs/sitemap": "^3.2.1",
        "astro": "^4.16.6",
        "typescript": "^5.6.3"
    }
}

...
server: {
    host: '0.0.0.0'
},

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Serve the app
   CMD ["npm", "run", "start"]


# SvelteKit
Source: https://docs.railway.com/guides/sveltekit

Learn how to deploy a Sveltekit app to Railway with this step-by-step guide. It covers quick setup, adapter configuration, one-click deploys and other deployment strategies.

This guide covers how to deploy a SvelteKit app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a SvelteKit app!

## Create a SvelteKit App

**Note:** If you already have a SvelteKit app locally or on GitHub, you can skip this step and go straight to the Deploy SvelteKit App to Railway.

To create a new SvelteKit app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new SvelteKit app using Vite:

Follow the prompts:

1. Select the SvelteKit demo template.
2. Add typechecking with Typescript.
3. Add prettier, eslint, and tailwindcss.
4. No tailwindcss plugins. Hit enter and move on.
5. Select npm as the package manager to install dependencies.

A new SvelteKit app will be provisioned for you in the svelteapp directory.

### Run the SvelteKit App locally

Next, cd into the directory and start the Vite development server by running the following command:

Open your browser and go to http://localhost:5173 to see the app. You can play the demo game by visiting the /sverdle route.

### Prepare SvelteKit App for deployment

First, we need to enable SvelteKit Node adapter.

SvelteKit adapters are plugins that take the built app as input and generate output for deployment. These adapters are used to run your project on deployment platforms.

Let's add the Node adapter to the app. Run the command below in your terminal:

Once it is installed, add the adapter to the app's svelte.config.js file.

The svelte.config.js file should look like this:

Next, we need to add the start script to the package.json file.

Svelte builds your project into a build directory. The server starts when the server entry point is executed, which is by default located at build/index.js.

Open up the package.json file and add the start script. Set it to node build/index.js like so:

_package.json_

Now, we are ready to deploy!

## Deploy the SvelteKit App to Railway

Railway offers multiple ways to deploy your SvelteKit app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/svelte-kit)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

**Note:** You can also choose from a <a href="https://railway.com/templates?q=sveltekit" target="_blank">variety of Svelte app templates</a> created by the community.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your SvelteKit app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1730489695/docs/quick-start/sveltekit_on_railway.png"
alt="screenshot of the deployed SvelteKit service"
layout="responsive"
width={2695} height={2199} quality={100} />

### Deploy from a GitHub Repo

To deploy a SvelteKit app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once the deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the SvelteKit app's root directory.
2. Add the content below to the Dockerfile:

3. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your SvelteKit apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npx sv create svelteapp

npm run dev

npm i -D @sveltejs/adapter-node

import adapter from "@sveltejs/adapter-node";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://svelte.dev/docs/kit/integrations
  // for more information about preprocessors
  preprocess: vitePreprocess(),

  kit: {
    // adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
    // If your environment is not supported, or you settled on a specific environment, switch out the adapter.
    // See https://svelte.dev/docs/kit/adapters for more information about adapters.
    adapter: adapter(),
  },
};

export default config;

{
	"name": "svelteapp",
	"version": "0.0.1",
	"type": "module",
	"scripts": {
		"dev": "vite dev",
		"build": "vite build",
		"start": "node build/index.js",
		"preview": "vite preview",
		"check": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json",
		"check:watch": "svelte-kit sync && svelte-check --tsconfig ./tsconfig.json --watch",
		"format": "prettier --write .",
		"lint": "prettier --check . && eslint ."
	},
	"devDependencies": {
		"@fontsource/fira-mono": "^5.0.0",
		"@neoconfetti/svelte": "^2.0.0",
		"@sveltejs/adapter-auto": "^3.0.0",
		"@sveltejs/adapter-node": "^5.2.9",
		"@sveltejs/kit": "^2.0.0",
		"@sveltejs/vite-plugin-svelte": "^4.0.0",
		"@types/eslint": "^9.6.0",
		"autoprefixer": "^10.4.20",
		"eslint": "^9.7.0",
		"eslint-config-prettier": "^9.1.0",
		"eslint-plugin-svelte": "^2.36.0",
		"globals": "^15.0.0",
		"prettier": "^3.3.2",
		"prettier-plugin-svelte": "^3.2.6",
		"prettier-plugin-tailwindcss": "^0.6.5",
		"svelte": "^5.0.0",
		"svelte-check": "^4.0.0",
		"tailwindcss": "^3.4.9",
		"typescript": "^5.0.0",
		"typescript-eslint": "^8.0.0",
		"vite": "^5.0.3"
	}
}

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Serve the app
   CMD ["npm", "run", "start"]


# Solid
Source: https://docs.railway.com/guides/solid

Learn how to deploy a SolidJS app to Railway with this step-by-step guide. It covers quick setup, one-click deploys and other deployment strategies.

It uses fine-grained reactivity, meaning it updates only when the data your app actually depends on changes. This minimizes unnecessary work, leading to faster load times and a seamless user experience.

This guide covers how to deploy a Solid app to Railway in four ways:

1. One-click deploy from a template.
2. From a GitHub repository.
3. Using the CLI.
4. Using a Dockerfile.

Now, let's create a Solid app!

## Create a Solid App

**Note:** If you already have a Solid app locally or on GitHub, you can skip this step and go straight to the Deploy Solid App on Railway.

To create a new Solid app, ensure that you have Node installed on your machine.

Run the following command in your terminal to create a new Solid app from a template:

A new Solid app will be provisioned for you in the solidjsapp directory.

### Run the Solid App locally

Next, cd into the directory and install the dependencies.

Start the Vite development server by running the following command:

Open your browser and go to http://localhost:3000 to see your app.

## Deploy the Solid App to Railway

Railway offers multiple ways to deploy your Solid app, depending on your setup and preference.

### One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/w5OSVq)

We highly recommend that you eject from the template after deployment to create a copy of the repo on your GitHub account.

### Deploy from the CLI

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Solid app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:
   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.
   - Once the deployment completes, go to **View logs** to check if the service is running successfully.
4. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/v1741198862/CleanShot_2025-03-05_at_18.19.11_2x_isjut5.png"
alt="screenshot of the deployed Solid service"
layout="responsive"
width={2610} height={2110} quality={100} />

### Deploy from a GitHub Repo

To deploy a Solid app to Railway directly from GitHub, follow the steps below:

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Deploy the App**:
   - Click **Deploy** to start the deployment process.
   - Once deployed, a Railway service will be created for your app, but it wonâ€™t be publicly accessible by default.
4. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
5. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

### Use a Dockerfile

1. Create a Dockerfile in the solidjsapp or Solid app's root directory.
2. Add the content below to the Dockerfile:

   The Dockerfile will use Caddy to serve the Solid app.

3. Add a Caddyfile to the app's root directory:

4. Either deploy via the CLI or from GitHub.

Railway automatically detects the Dockerfile, and uses it to build and deploy the app.

**Note:** Railway supports also <a href="/guides/services#deploying-a-public-docker-image" target="_blank">deployment from public and private Docker images</a>.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Solid apps seamlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Add a Database Service
- Monitor your app

## Code Examples

npx degit solidjs/templates/js solidjsapp

npm install

npm run dev

railway init

railway up

# Use the Node alpine official image
   # https://hub.docker.com/_/node
   FROM node:lts-alpine AS build

   # Set config
   ENV NPM_CONFIG_UPDATE_NOTIFIER=false
   ENV NPM_CONFIG_FUND=false

   # Create and change to the app directory.
   WORKDIR /app

   # Copy the files to the container image
   COPY package*.json ./

   # Install packages
   RUN npm ci

   # Copy local code to the container image.
   COPY . ./

   # Build the app.
   RUN npm run build

   # Use the Caddy image
   FROM caddy

   # Create and change to the app directory.
   WORKDIR /app

   # Copy Caddyfile to the container image.
   COPY Caddyfile ./

   # Copy local code to the container image.
   RUN caddy fmt Caddyfile --overwrite

   # Copy files to the container image.
   COPY --from=build /app/dist ./dist

   # Use Caddy to run/serve the app
   CMD ["caddy", "run", "--config", "Caddyfile", "--adapter", "caddyfile"]

{
       # global options
       admin off # there's no need for the admin api in railway's environment
       persist_config off # storage isn't persistent anyway
       auto_https off # railway handles https for us, this would cause issues if left enabled
       # runtime logs
       log {
           format json # set runtime log format to json mode
       }
       # server options
       servers {
           trusted_proxies static private_ranges 100.0.0.0/8 # trust railway's proxy
       }
   }

   # site block, listens on the $PORT environment variable, automatically assigned by railway
   :{$PORT:3000} {
       # access logs
       log {
           format json # set access log format to json mode
       }

       # health check for railway
       rewrite /health /*

       # serve from the 'dist' folder (Vite builds into the 'dist' folder)
       root * dist

       # enable gzipping responses
       encode gzip

       # serve files from 'dist'
       file_server

       # if path doesn't exist, redirect it to 'index.html' for client side routing
       try_files {path} /index.html
   }


# Phoenix
Source: https://docs.railway.com/guides/phoenix

Learn how to deploy a Phoenix app to Railway with this step-by-step guide. It covers quick setup, ecto setup, database integration, one-click deploys and other deployment strategies.



## Create a Phoenix App

**Note:** If you already have a Phoenix app locally or on GitHub, you can skip this step and go straight to the Deploy Phoenix App on Railway.

To create a new Phoenix app, ensure that you have Elixir and Hex package manager installed on your machine. Once everything is set up, run the following command in your terminal to install the Phoenix application generator:

Next, run the following command:

Select Y to install all dependencies.

This command will create a new Phoenix app named helloworld with some optional dependencies such as:

- Ecto for communicating with a database such as PostgreSQL, MySQL etc
- Phoenix live view for building realtime & interactive web apps.
- Phoenix HTML and Tailwind CSS for HTML apps.

### Configure Database

Next, navigate into the helloworld directory using the cd command.

Open up the config/dev.exs file. You'll notice that a new Phoenix app is already set up with PostgreSQL settings. It assumes the database has a postgres user with the right permissions and a default password of postgres. Update the username and password to match your local PostgreSQL account credentials.

**Note**: If you prefer using a different database, like MySQL, you can easily switch the database adapter in the mix.exs file. Simply remove the Postgrex dependency and add MyXQL instead. For detailed instructions, check out this guide on using other databases in Phoenix.

The default database name is set to helloworld_dev, but feel free to change it to whatever you'd prefer.

Next, create the database for our app by running the following command:

A database will be created for our app.

### Run the Phoenix App locally

Start the app by running the following command:

By default, Phoenix accepts requests on port 4000.

Open your browser and go to http://localhost:4000 to see your app.

Now that your app is running locally, letâ€™s move on to deploying it to Railway!

### Prepare our Phoenix App for deployment

Go ahead and create a nixpacks.toml file in the root directory of our Phoenix app.

The nixpacks.toml file is a configuration file used by Nixpacks, a build system developed and used by Railway, to set up and deploy applications.

In this file, you can specify the instructions for various build and deployment phases, along with environment variables and package dependencies.

Add the following content to the file:

1. [variables] This section contains the list of env variables you want to set for the app.
   - MIX_ENV = 'prod': It sets the Elixir environment to prod.
2. [phases.setup]: This defines a list of Nix packages to be installed during the setup phase. The placeholder '...' should be replaced with any additional packages needed for your application. The inclusion of erlang indicates that the Erlang runtime is required for the Elixir application.
3. [phases.install]: This section contains a list of commands to run during the installation phase.
   - mix local.hex --force: Installs the Hex package manager for Elixir, which is necessary for managing dependencies.
   - mix local.rebar --force: Installs Rebar, a build tool for Erlang.
   - mix deps.get --only prod: Fetches only the production dependencies defined in the mix.exs file.
4. [phases.build]: This section contains commands to run during the build phase.
   - mix compile: Compiles the Elixir application.
   - mix assets.deploy: This is a command to handle the deployment of static assets (e.g., JavaScript, CSS) for our app.
5. [start]: This section contains commands to run when starting the application.
   - mix ecto.setup: This command is used to set up the database by running migrations and seeding it. It prepares the database for the application to connect.
   - mix phx.server: This starts the Phoenix server, allowing the application to begin accepting requests.

Now, we are ready to deploy!

## Deploy Phoenix App to Railway

Railway offers multiple ways to deploy your Phoenix app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Phoenix app along with a Postgres database.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/0LSBzw)

After deploying, we recommend that you eject from the template to create a copy of the repository under your own GitHub account. This will give you full control over the source code and project.

## Deploy from the CLI

To deploy the Phoenix app using the Railway CLI, please follow the steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Phoenix app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:

   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.

   **Note:** You might encounter an errorâ€“â€“warning: the VM is running with native name encoding of latin1 which may cause Elixir to malfunction as it expects utf8..... Donâ€™t worry, weâ€™ll address this in the next step.

4. **Add a Database Service**:
   - Run railway add.
   - Select PostgreSQL by pressing space and hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
5. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - SECRET_KEY_BASE : Set the value to the your app's secret key. You can run mix phx.gen.secret locally to generate one.
     - LANGand LC_CTYPE: Set both values to en_US.UTF-8. This sets your app's locale and gets rid of the _native name encoding of latin1_ warning.
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - ECTO_IPV6: Set the value to true to enable your Phoenix app to connect to the database through the IPv6 private network.
   - Use the **Raw Editor** to add any other required environment variables in one go.
6. **Redeploy the Service**:
   - Click **Deploy** on the Railway Project Canvas to apply your changes.
7. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
8. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1730139857/docs/quick-start/phoenix_elixir_app.png"
alt="screenshot of the deployed Phoenix service showing the welcome page"
layout="responsive"
width={2757} height={2111} quality={100} />

## Deploy from a GitHub Repo

To deploy the Phoenix app to Railway, start by pushing the app to a GitHub repo. Once thatâ€™s set up, follow the steps below to complete the deployment process.

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**. This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - SECRET_KEY_BASE : Set the value to the your app's secret key. You can run mix phx.gen.secret locally to generate one.
     - LANGand LC_CTYPE: Set both values to en_US.UTF-8 to ensure proper locale settings and avoid the _native name encoding of latin1 warning_.
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - ECTO_IPV6: Set the value to true to enable your Phoenix app to connect to the database through the IPv6 private network.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s an Elixir app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Phoenix apps effortlessly!

## Want to Deploy Livebook?

Livebook, an interactive notebook tool built specifically for Elixir, provides a powerful and intuitive environment for exploring data, running code, and documenting insights, all in one place. Itâ€™s perfect for experimenting with Elixir code, prototyping, and sharing live documentation.

Click the button below to deploy an instance of Livebook quickly.

![Deploy Livebook on Railway](https://railway.com/new/template/4uLt1s)

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Deploy Phoenix with Distillery
- Monitoring
- Deployments

## Code Examples

mix archive.install hex phx_new

mix phx.new helloworld

mix ecto.create

mix phx.server

# nixpacks.toml
[variables]
MIX_ENV = 'prod'

[phases.setup]
nixPkgs = ['...', 'erlang']

[phases.install]
cmds = [
  'mix local.hex --force',
  'mix local.rebar --force',
  'mix deps.get --only prod'
]

[phases.build]
cmds = [
  'mix compile',
  'mix assets.deploy'
]

[start]
cmd = "mix ecto.setup && mix phx.server"

railway init

railway up


# Phoenix Distillery
Source: https://docs.railway.com/guides/phoenix-distillery

Learn how to deploy a Phoneix app with Distillery to Railway with this step-by-step guide. It covers quick setup, ecto setup, database integration, one-click deploys and other deployment strategies.

In this guide, you'll learn how to deploy Phoenix apps with Distillery to Railway.

## Create a Phoenix App with Distillery

**Note:** If you already have a Phoenix app locally or on GitHub, you can skip this step and go straight to the Deploy Phoenix App with Distillery to Railway.

To create a new Phoenix app, ensure that you have Elixir and Hex package manager installed on your machine. Once everything is set up, run the following command in your terminal to install the Phoenix application generator:

Next, run the following command:

Select Y to install all dependencies.

This command will create a new Phoenix app named helloworld_distillery with some optional dependencies such as:

- Ecto for communicating with a database such as PostgreSQL, MySQL etc
- Phoenix live view for building realtime & interactive web apps.
- Phoenix HTML and Tailwind CSS for HTML apps.

### Configure Database

Next, navigate into the helloworld directory using the cd command.

Open up the config/dev.exs file. You'll notice that a new Phoenix app is already set up with PostgreSQL settings. It assumes the database has a postgres user with the right permissions and a default password of postgres. Update the username and password to match your local PostgreSQL account credentials.

**Note**: If you prefer using a different database, like MySQL, you can easily switch the database adapter in the mix.exs file. Simply remove the Postgrex dependency and add MyXQL instead. For detailed instructions, check out this guide on using other databases in Phoenix.

The default database name is set to helloworld_dev, but feel free to change it to whatever you'd prefer.

Next, create the database for our app by running the following command:

A database will be created for our app.

### Add and Configure Distillery

1. Open up the mix.exs file and add Distillery to the deps function:

Now, run mix deps.get to update your dependencies.

2. Open up config/prod.exs file and update the endpoint section to the following:

server configures the endpoint to boot the Cowboy application http endpoint on start.
root configures the application root for serving static files
version ensures that the asset cache will be busted on versioned application upgrades.

3. Initialize your Distillery release by running the following command:

This will create the rel/config.exs and rel/vm.args files. A rel/plugins directory will be created too.

4. Create a Mix config file at rel/config/config.exs. Here, we are creating a mix config provider. Add the following to it:

Now, update the rel/config.exs file to use our new provider. In the environment :prod part of the file, replace with the following:

5. Finally, let's configure Ecto to fetch the database credentials from the runtime environment variables.

Open the lib/helloworld_distillery/repo.ex file and modify it to this:

### Build the Release with Distillery

To build the release, run the following command:

#### Handling Errors

If you encounter the following error after running the command:

You need to modify your mix.exs file to include :sasl. Open the file and add :sasl to the extra_applications list in the application function:

After saving your changes, try running the command again as a super user to prevent access errors:

**Additional Errors**

If you encounter this error:

Youâ€™ll need to create the RELEASES directory manually. Once created, run the command again.

#### Successful Build

Upon a successful build, you should see output similar to the following:

### Test the Release with Distillery locally

Now, let's test our release locally. First, create your database by running the following command:

Next, export the necessary environment variables by running:

With the environment set up, you can start the release with:

Once your app is running, open your browser and visit http://localhost:4000 to see it in action.

With your app up and running locally, let's move on to deploying the release to Railway!

### Prepare App for Deployment

Create a nixpacks.toml file in the root of your app directory and add the following content:

This nixpacks.toml file instructs Railway to execute specific commands during the setup, install, build, and start phases of the deployment. It ensures your app is compiled, assets are digested, and the release is created correctly using Distillery.

## Deploy Phoenix App to Railway

Railway offers multiple ways to deploy your Phoenix app, depending on your setup and preference. Choose any of the following methods:

1. One-click deploy from a template.
2. Using the CLI.
3. From a GitHub repository.

## One-Click Deploy from a Template

If youâ€™re looking for the fastest way to get started, the one-click deploy option is ideal. It sets up a Phoenix app with Distillery along with a Postgres database.

Click the button below to begin:

![Deploy on Railway](https://railway.com/new/template/_qWFnI)

After deploying, we recommend that you eject from the template to create a copy of the repository under your own GitHub account. This will give you full control over the source code and project.

## Deploy from the CLI

To deploy the Phoenix app using the Railway CLI, please follow the steps:

1. **Install the Railway CLI**:
   - <a href="/guides/cli#installing-the-cli" target="_blank">Install the CLI</a> and <a href="/guides/cli#authenticating-with-the-cli" target="_blank">authenticate it</a> using your Railway account.
2. **Initialize a Railway Project**:
   - Run the command below in your Phoenix app directory.
     
   - Follow the prompts to name your project.
   - After the project is created, click the provided link to view it in your browser.
3. **Deploy the Application**:

   - Use the command below to deploy your app:
     
   - This command will scan, compress and upload your app's files to Railway. Youâ€™ll see real-time deployment logs in your terminal.

   **Note:** You might encounter an errorâ€“â€“warning: the VM is running with native name encoding of latin1 which may cause Elixir to malfunction as it expects utf8..... Donâ€™t worry, weâ€™ll address this in the next step.

4. **Add a Database Service**:
   - Run railway add.
   - Select PostgreSQL by pressing space and hit **Enter** to add it to your project.
   - A database service will be added to your Railway project.
5. **Configure Environment Variables**:
   - Go to your app service <a href="/overview/the-basics#service-variables">**Variables**</a> section and add the following:
     - SECRET_KEY_BASE : Set the value to the your app's secret key. You can run mix phx.gen.secret locally to generate one.
     - LANGand LC_CTYPE: Set both values to en_US.UTF-8. This sets your app's locale and gets rid of the _native name encoding of latin1_ warning.
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - ECTO_IPV6: Set the value to true to enable your Phoenix app to connect to the database through the IPv6 private network.
   - Use the **Raw Editor** to add any other required environment variables in one go.
6. **Redeploy the Service**:
   - Click **Deploy** on the Railway Project Canvas to apply your changes.
7. **Verify the Deployment**:
   - Once the deployment completes, go to **View logs** to check if the server is running successfully.
8. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

<Image src="https://res.cloudinary.com/railway/image/upload/f_auto,q_auto/v1730309171/docs/quick-start/phoenix_distillery.png"
alt="screenshot of the deployed Phoenix with Distillery service"
layout="responsive"
width={2667} height={2177} quality={100} />

## Deploy from a GitHub Repo

To deploy the Phoenix app to Railway, start by pushing the app to a GitHub repo. Once thatâ€™s set up, follow the steps below to complete the deployment process.

1. **Create a New Project on Railway**:
   - Go to <a href="https://railway.com/new" target="_blank">Railway</a> to create a new project.
2. **Deploy from GitHub**:
   - Select **Deploy from GitHub repo** and choose your repository.
     - If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.
3. **Add Environment Variables and Provision a Database Service**:
   - Click **Add Variables**, but hold off on adding anything just yet. First, proceed with the next step.
   - Right-click on the Railway project canvas or click the **Create** button, then select **Database** and choose **Add PostgreSQL**. This will create and deploy a new PostgreSQL database for your project.
   - Once the database is deployed, you can return to adding the necessary environment variables:
     - SECRET_KEY_BASE : Set the value to the your app's secret key. You can run mix phx.gen.secret locally to generate one.
     - LANGand LC_CTYPE: Set both values to en_US.UTF-8 to ensure proper locale settings and avoid the _native name encoding of latin1 warning_.
     - DATABASE_URL: Set the value to ${{Postgres.DATABASE_URL}} (this references the URL of your new Postgres database). Learn more about referencing service variables.
     - ECTO_IPV6: Set the value to true to enable your Phoenix app to connect to the database through the IPv6 private network.
4. **Deploy the App Service**:
   - Click **Deploy** on the Railway project canvas to apply your changes.
5. **Verify the Deployment**:

   - Once the deployment completes, go to **View logs** to check if the server is running successfully.

   **Note:** During the deployment process, Railway will automatically detect that itâ€™s an Elixir app.

6. **Set Up a Public URL**:
   - Navigate to the **Networking** section under the Settings tab of your new service.
   - Click Generate Domain to create a public URL for your app.

This guide covers the main deployment options on Railway. Choose the approach that suits your setup, and start deploying your Phoenix apps with Distillery effortlessly!

## Next Steps

Explore these resources to learn how you can maximize your experience with Railway:

- Monitoring
- Deployments

## Code Examples

mix archive.install hex phx_new

mix phx.new helloworld_distillery

mix ecto.create

defp deps do
    [ ...,
     {:distillery, "~> 2.1"},
      ...,
    ]
  end

config :helloworld_distillery, HelloworldDistilleryWeb.Endpoint,
  cache_static_manifest: "priv/static/cache_manifest.json",
  server: true,
  root: ".",
  version: Application.spec(:phoenix_distillery, :vsn)

mix distillery.init

import Config

port = String.to_integer(System.get_env("PORT") || "4000")
default_secret_key_base = :crypto.strong_rand_bytes(43) |> Base.encode64

config :helloworld_distillery, HelloworldDistilleryWeb.Endpoint,
  http: [port: port],
  url: [host: "localhost", port: port],
  secret_key_base: System.get_env("SECRET_KEY_BASE") || default_secret_key_base

environment :prod do
  set include_erts: true
  set include_src: false
  set cookie: :"Jo2*~U0C1x!*E}!o}W*(mx=pzd[XWG[bW)T~_Kjy3eJuEJ;M&!eqj7AUR1*9Vw]!"
  set config_providers: [
    {Distillery.Releases.Config.Providers.Elixir, ["${RELEASE_ROOT_DIR}/etc/config.exs"]}
  ]
  set overlays: [
    {:copy, "rel/config/config.exs", "etc/config.exs"}
  ]
end

defmodule HelloworldDistillery.Repo do
  use Ecto.Repo,
    otp_app: :helloworld_distillery,
    adapter: Ecto.Adapters.Postgres,
    pool_size: 10
  def init(_type, config) do
    {:ok, Keyword.put(config, :url, System.get_env("DATABASE_URL"))}
  end
end

npm run deploy --prefix assets && MIX_ENV=prod mix do phx.digest, distillery.release --env=prod

==> Invalid application `:sasl`! The file sasl.app does not exist or cannot be loaded.

def application do
    [
      mod: {HelloworldDistillery.Application, []},
      extra_applications: [:logger, :runtime_tools, :sasl]
    ]
  end

sudo npm run deploy --prefix assets && MIX_ENV=prod mix do phx.digest, distillery.release --env=prod

Failed to archive release: _build/prod/rel/helloworld_distillery/releases/RELEASES: no such file or directory

...
==> Packaging release..
Release successfully built!
To start the release you have built, you can use one of the following tasks:

    # start a shell, like 'iex -S mix'
    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery console

    # start in the foreground, like 'mix run --no-halt'
    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery foreground

    # start in the background, must be stopped with the 'stop' command
    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery start

If you started a release elsewhere, and wish to connect to it:

    # connects a local shell to the running node
    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery remote_console

    # connects directly to the running node's console
    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery attach

For a complete listing of commands and their use:

    > _build/prod/rel/helloworld_distillery/bin/helloworld_distillery help

mix ecto.create

export DATABASE_URL=postgresql://username:password@127.0.0.1:5432/helloworld_distillery
export SECRET_KEY_BASE=<your-secret-key-base>

_build/prod/rel/helloworld_distillery/bin/helloworld_distillery foreground

# nixpacks.toml
[variables]
MIX_ENV = 'prod'

[phases.setup]
nixPkgs = ['...', 'erlang']

[phases.install]
cmds = [
  'mix local.hex --force',
  'mix local.rebar --force',
  'mix deps.get --only prod'
]

[phases.build]
cmds = [
  'mix compile',
  'mkdir -p _build/prod/rel/helloworld_distillery/releases/RELEASES',
  'mix do phx.digest, distillery.release --env=prod',
]

[start]
cmd = "mix ecto.setup && _build/prod/rel/helloworld_distillery/bin/helloworld_distillery foreground"

railway init

railway up


# Public Networking
Source: https://docs.railway.com/guides/public-networking

Learn everything about public networking on Railway.



## Port Variable

An essential part of connecting to your service from the internet, is properly handling the PORT variable.

The easiest way to get up and running is by using the Railway-provided port.

### Railway-provided port

As long as you have not defined a PORT variable, Railway will provide and expose one for you.

To have your application use the Railway-provided port, you should ensure it is listening on 0.0.0.0:$PORT, where PORT is the Railway-provided environment variable.

**Examples** -

More information and examples for this can be found in the Fixing Common Errors guide.

**Note:** If your application needs to be accessible over both public and private networks, your application server must support dual stack binding. Most servers handle this automatically when listening on ::, but some, like Uvicorn, do not.

### User-defined port

If you prefer to explicitly set a port, you can set the PORT variable in your service variables to the port on which your service is listening.

If your domain does not have a target port set, Railway will direct incoming traffic to the port specified in the PORT variable, this is sometimes needed when creating a template.

For information on how to configure variables, see the Variables guide.

## Railway-Provided Domain

Railway services don't obtain a domain automatically, but it is easy to set one up.

To assign a domain to your service, go to your service's settings, find the Networking -> Public Networking section, and choose Generate Domain.

#### Automated Prompt

If Railway detects that a deployed service is listening correctly (as described above), you will see a prompt on the service tile in the canvas, and within the service panel.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1654560212/docs/add-domain_prffyh.png"
alt="Screenshot of adding Service Domain"
layout="responsive"
width={1396} height={628} quality={80} />

Simply follow the prompts to generate a domain and your app will be exposed to the internet.

**Don't see the Generate Domain Button?**

If you have previously assigned a TCP Proxy to your service, you will not see the Generate Domain option. You must remove the TCP Proxy (click the Trashcan icon), then you can add a domain.

## Custom Domains

Custom domains can be added to a Railway service and once setup we will automatically issue an SSL certificate for you.

1. Navigate to the Settings tab of your desired service.

2. Click + Custom Domain in the Public Networking section of Settings

3. Type in the custom domain (wildcard domains are supported, see below for more details)

   You will be provided with a CNAME domain to use, e.g., g05ns7.up.railway.app.

4. In your DNS provider (Cloudflare, DNSimple, Namecheap, etc), create a CNAME record with the CNAME value provided by Railway.

5. Wait for Railway to verify your domain. When verified, you will see a greencheck mark next to the domain(s) -

   <Image
   src="https://res.cloudinary.com/railway/image/upload/v1654563209/docs/domains_uhchsu.png"
   alt="Screenshot of Custom Domain"
   layout="responsive"
   width={1338} height={808} quality={80} />

   You will also see a Cloudflare proxy detected message if we have detected that you are using Cloudflare.

   **Note:** Changes to DNS settings may take up to 72 hours to propagate worldwide.

**Important Considerations**

- Freenom domains are not allowed and not supported.
- The Trial Plan is limited to 1 custom domain. It is therefore not possible to use both yourdomain.com and www.yourdomain.com as these are considered two distinct custom domains.
- The Hobby Plan is limited to 2 custom domains per service.
- The [Pro Plan]() is limited to 20 domains per service by default. This limit can be increased for Pro users on request, simply reach out to us via a private thread.

## Wildcard Domains

Wildcard domains allow for flexible subdomain management. There are a few important things to know when using them -

- Ensure that the CNAME record for authorize.railwaydns.net is not proxied by your provider (eg: Cloudflare). This is required for the verification process to work.

- Wildcards cannot be nested (e.g., \*.\*.yourdomain.com).

- Wildcards can be used for any subdomain level (e.g., *.example.com or *.subdomain.example.com).

### Subdomains

E.g. *.example.com

- Make sure Universal SSL is enabled.

- Enable Full SSL/TLS encryption.

- Add CNAME records for the wildcard subdomain.

### Nested Subdomains

E.g. *.nested.example.com

- Disable Universal SSL.

- Purchase Cloudflare's Advanced Certificate Manager.

- Enable Edge Certificates.

- Enable Full SSL/TLS encryption.

- Add CNAME records for the wildcard nested subdomain.

When you add a wildcard domain, you will be provided with two domains for which you should add two CNAME records -

<Image
src="https://res.cloudinary.com/railway/image/upload/v1679693511/wildcard_domains_zdguqs.png"
alt="Screenshot of Wildcard Domain"
layout="responsive"
width={1048} height={842} quality={80} />

One record is for the wildcard domain, and one for the \_acme-challenge. The \_acme-challenge CNAME is required for Railway to issue the SSL Certificate for your domain.

### Wildcard Domains on Cloudflare

If you have a wildcard domain on Cloudflare, you must:

- Turn off Cloudflare proxying is on the _acme-challenge record (disable the orange cloud)

- Enable Cloudflare's Universal SSL

## Target Ports

Target Ports, or Magic Ports, correlate a single domain to a specific internal port that the application listens on, enabling you to expose multiple HTTP ports through the use of multiple domains.

Example -

https://example.com/ â†’ :8080

https://management.example.com/ â†’ :9000

When you first generate a Railway-provided domain, if your application listens on a single port, Railway's magic automatically detects and sets it as the domain's target port. If your app listens on multiple ports, you're provided with a list to choose from.

When you add a custom domain, you're given a list of ports to choose from, and the selected port will handle all traffic routed to the domain. You can also specify a custom port if needed.

These target ports inform Railway which public domain corresponds to each internal port, ensuring that traffic from a specific domain is correctly routed to your application.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743196226/docs/custom-domain_ulvgap.png"
alt="Screenshot of target port selection on a custom domain"
layout="intrinsic"
width={1200} height={1035}
quality={100} />

You can change the automatically detected or manually set port at any time by clicking the edit icon next to the domain.

## Adding a Custom Domain

When adding a root or apex domain to your Railway service, you must ensure that you add the appropriate DNS record to the domain within your DNS provider. At this time, Railway supports <a href="https://developers.cloudflare.com/dns/cname-flattening/" target="_blank">CNAME Flattening</a> and dynamic ALIAS records.

**Additional context**

Generally, direct CNAME records at the root or apex level are incompatible with DNS standards (which assert that you should use an "A" or "AAAA" record). However, given the dynamic nature of the modern web and PaaS providers like Railway, some DNS providers have incorporated workarounds enabling CNAME-like records to be associated with root domains.
_Check out <a href="https://www.ietf.org/rfc/rfc1912.txt#:~:text=root%20zone%20data).-,2.4%20CNAME%20records,-A%20CNAME%20record" target="_blank">RFC 1912</a> if you're interested in digging into this topic._

**Choosing the correct record type**

The type of record to create is entirely dependent on your DNS provider. Here are some examples -

- <a href="https://developers.cloudflare.com/dns/zone-setups/partial-setup" target="_blank">Cloudflare CNAME</a> - Simply set up a CNAME record for your root domain in Cloudflare, and they take care of the rest under the hood. Refer to <a href="https://support.cloudflare.com/hc/en-us/articles/205893698-Configure-Cloudflare-and-Heroku-over-HTTPS" target="_blank">this guide</a> for more detailed instructions.
- <a href="https://support.dnsimple.com/articles/domain-apex-heroku/" target="_blank">DNSimple ALIAS</a> - Set up an dynamic ALIAS in DNSimple for your root domain.
- <a href="https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain/" target="_blank">Namecheap CNAME</a> - Set up an CNAME in Namecheap for your root domain.
- <a href="https://bunny.net/blog/how-aname-dns-records-affect-cdn-routing/" target="_blank">bunny.net</a> - Set up a ANAME in bunny.net for your root domain.

In contrast there are many nameservers that don't support CNAME flattening or dynamic ALIAS records -

- <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register-other-dns-service.html" target="_blank">AWS Route 53</a>
- <a href="https://support.hostinger.com/en/articles/1696789-how-to-change-nameservers-at-hostinger" target="_blank">Hostinger</a>
- <a href="https://www.godaddy.com/en-ca/help/edit-my-domain-nameservers-664" target="_blank">GoDaddy</a>
- <a href="https://www.namesilo.com/support/v2/articles/domain-manager/dns-manager" target="_blank">NameSilo</a>
- <a href="https://dns.he.net/" target="_blank">Hurricane Electric</a>
- <a href="https://support.squarespace.com/hc/en-us/articles/4404183898125-Nameservers-and-DNSSEC-for-Squarespace-managed-domains#toc-open-the-domain-s-advanced-settings" target="_blank">SquareSpace</a>

**Workaround - Changing your Domain's Nameservers**

If your DNS provider doesn't support CNAME Flattening or dynamic ALIAS records at the root, you can also change your domain's nameservers to point to Cloudflare's nameservers. This will allow you to use a CNAME record for the root domain. Follow the instructions listed on Cloudflare's documentation to <a href="https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/" target="_blank">change your nameservers</a>.

## Adding a Root Domain With www Subdomain to Cloudflare

If you want to add your root domain (e.g., mydomain.com) and the www. subdomain to Cloudflare and redirect all www. traffic to the root domain:

1. Create a Custom Domain in Railway for your root domain (e.g., mydomain.com). Copy the value field. This will be in the form: abc123.up.railway.app.
2. Add a CNAME DNS record to Cloudflare:
   - Name â†’ @.
   - Target â†’ the value field from Railway.
   - Proxy status â†’ on, should display an orange cloud.
   - Note: Due to domain flattening, Name will automatically update to your root domain (e.g., mydomain.com).
3. Add another CNAME DNS record to Cloudflare:
   - Name â†’ www.
   - Target â†’ @
   - Proxy status: â†’ on, should display an orange cloud.
   - Note: Cloudflare will automatically change the Target value to your root domain.
4. Enable Full SSL/TLS encryption in Cloudflare:
   - Go to your domain on Cloudflare.
   - Navigate to SSL/TLS -> Overview.
   - Select Full. **Not** Full (Strict) **Strict mode will not work as intended**.
5. Enable Universal SSL in Cloudflare:
   - Go to your domain on Cloudflare.
   - Navigate to SSL/TLS -> Edge Certificates.
   - Enable Universal SSL.
6. After doing this, you should see Cloudflare proxy detected on your Custom Domain in Railway with a green cloud.
7. Create a Bulk Redirect in Cloudflare:
   - Go to your Cloudflare dashboard.
   - Navigate to Bulk Redirects.
   - Click Create Bulk Redirect List.
   - Give it a name, e.g., www-redirect.
   - Click Or, manually add URL redirects.
   - Add a Source URL: https://www.mydomain.com.
   - Add Target URL: https://mydomain.com with status 301.
   - Tick all the parameter options: (Preserve query string, Include subdomains, Subpath matching, Preserve path suffix)
   - Click Next, then Save and Deploy.

**Note:** DNS changes may take some time to propagate. You may want to refresh your DNS cache by using commands like ipconfig /flushdns on Windows or dscacheutil -flushcache on macOS. Testing the URLs in an incognito window can also help verify changes.

## TCP Proxying

You can proxy TCP traffic to your service by creating a TCP proxy in the service settings. Enter the port that you want traffic proxied to, Railway will generate a domain and port for you to use. All traffic sent to domain:port will be proxied to your service. This is useful for services that don't support HTTP, such as databases.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743194081/docs/tcp-proxy_edctub.png"
alt="Screenshot of TCP proxy configuration"
layout="responsive"
width={1200} height={822} quality={100} />

Incoming traffic will be distributed across all replicas in the closest region using a random algorithm.

## Using HTTP and TCP Together

Railway does support exposing both HTTP and TCP over public networking, in a single service. Therefore, if you have a domain assigned, you will still see the option to enable TCP Proxy, and vice-versa.

If you have a usecase that requires exposing both HTTP and TCP over public networking, in one service, <a href="https://station.railway.com/feedback" target="_blank">let us know</a>!

## Let's Encrypt SSL Certificates

Once a custom domain has been correctly configured, Railway will automatically
generate and apply a Let's Encrypt certificate. This means that any custom
domain on Railway will automatically be accessible
via https://.

### External SSL Certificates

We currently do not support external SSL certificates since we provision one for you.

## Provider Specific Instructions

If you have proxying enabled on Cloudflare (the orange cloud), you MUST set your
SSL/TLS settings to **Full** -- Full (Strict) **will not work as intended**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917785/docs/cloudflare_zgeycj.png"
alt="Screenshot of Custom Domain"
layout="responsive"
width={1205} height={901} quality={80} />

If proxying is not enabled, Cloudflare will not associate the domain with your Railway project. In this case, you will encounter the following error message:

Also note that if proxying is enabled, you can NOT use a domain deeper than a first level subdomain without Cloudflare's Advanced Certificate Manager. For example, anything falling under \*.yourdomain.com can be proxied through Cloudflare without issue, however if you have a custom domain under \*.subdomain.yourdomain.com, you MUST disable Cloudflare Proxying and set the CNAME record to DNS Only (the grey cloud), unless you have Cloudflare's Advanced Certificate Manager.

## Support

Looking for the technical specs like timeouts, TLS information, rate limits etc? Check out the Public Networking reference page.

Having trouble connecting to your app from the internet? Check out the Fixing Common Errors guide or reach out on our <a href="https://discord.gg/railway" target="_blank">Discord</a>.

## Code Examples

# python web server
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

// node web server
const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`App listening on port: ${port}`);
});

ERR_TOO_MANY_REDIRECTS


# Private Networking
Source: https://docs.railway.com/guides/private-networking

Learn everything about private networking on Railway.

<Image src="https://res.cloudinary.com/railway/image/upload/v1686946888/docs/CleanShot_2023-06-16_at_16.21.08_2x_lgp9ne.png"
alt="Preview of What The Guide is Building"
layout="intrinsic"
width={1310} height={420} quality={100} />

By default, all projects have private networking enabled and services will get a new DNS name under the railway.internal domain. This DNS name will resolve to the internal IPv6 address of the services within a project.

## Communicating Over the Private Network

To communicate over the private network, there are some specific things to know to be successful.

### Listen on IPv6

Since the private network is an IPv6 only network, applications that will receive requests over the private network must be configured to listen on IPv6. On most web frameworks, you can do this by binding to the host ::.

Some examples are below -

#### Node / Express

Listen on :: to bind to both IPv4 and IPv6.

#### Node / Nest

Listen on :: to bind to both IPv4 and IPv6.

#### Node / Next

Update your start command to bind to both IPv4 and IPv6.

Or if you are using a custom server, set hostname to :: in the configuration object passed to the next() function.

If neither of these options are viable, you can set a HOSTNAME service variable with the value :: to listen on both IPv4 and IPv6.

#### Python / Gunicorn

Update your start command to bind to both IPv4 and IPv6.

#### Python / Hypercorn

Update your start command to bind to both IPv4 and IPv6.

#### Python / Uvicorn

Update your start command to bind to IPv6.

**Note:** If your application needs to be accessible over both private and public networks, your application server must support dual stack binding. Most servers handle this automatically when listening on ::, but some, like Uvicorn, do not.

### Use Internal Hostname and Port

For applications making requests to a service over the private network, you should use the internal DNS name of the service, plus the PORT on which the service is listening.

For example, if you have a service called api listening on port 3000, and you want to communicate with it from another service, you would use api.railway.internal as the hostname and specify the port -

Note that you should use http in the address.

#### Using Reference Variables

Using reference variables, you can accomplish the same end as the above example.

Let's say you are setting up your frontend service to talk to the api service. In the frontend service, set the following variable -

<div style={{ marginTop: '1.5em' }}><Banner variant="info">
api.PORT above refers to a service variable that must be set manually. It does not automatically resolve to the port the service is listening on, nor does it resolve to the PORT environment variable injected into the service at runtime.
</Banner></div>

Then in the frontend code, you will simply reference the BACKEND_URL environment variable -

### Private Network Context

The private network exists in the context of a project and environment and is not accessible over the public internet. In other words -

- A web application that makes client-side requests **cannot** communicate to another service over the private network.
- Services in one project/environment **cannot** communicate with services in another project/environment over the private network.

Check out the FAQ section for more information.

### Known Configuration Requirements for IPv6

Some libraries and components require you to be explicit when either listening or establishing a connection over IPv6.

<Collapse title="ioredis">

ioredis is a Redis client for node.js, commonly used for connecting to Redis from a node application.

When initializing a Redis client using ioredis, you must specify family=0 in the connection string to support connecting to both IPv6 and IPv4 endpoints:

<a href="https://www.npmjs.com/package/ioredis" target="_blank">ioredis docs</a>

</Collapse>

<Collapse title="bullmq">

bullmq is a message queue and batch processing library for node.js, commonly used for processing jobs in a queue.

When initializing a bullmq client, you must specify family: 0 in the connection object to support connecting to both IPv6 and IPv4 Redis endpoints:

<a href="https://docs.bullmq.io/" target="_blank">bullmq docs</a>

</Collapse>

<Collapse title="Mongo Docker image">

If you are creating a service using the official Mongo Docker image in Docker Hub and would like to connect to it over the private network, you must start the container with some options to instruct the Mongo instance to listen on IPv6. For example, this would be set in your Start Command:

**Note that the official template provided by Railway is already deployed with this Start Command.**

</Collapse>

<Collapse title="hot-shots">

hot-shots is a StatsD client for node.js, which can be used to ship metrics to a DataDog agent for example. When initializing a StatsD client using hot-shots, you must specify that it should connect over IPv6:

<a href="https://www.npmjs.com/package/hot-shots" target="_blank">hot-shots docs</a>

</Collapse>

<Collapse title="Go Fiber">

fiber is a web framework for Go. When configuring your Fiber app, you should set the Network field to tcp to have it listen on IPv6 as well as IPv4:

<a href="https://docs.gofiber.io/api/fiber#:~:text=json.Marshal-,Network,-string" target="_blank">Fiber docs</a>

</Collapse>

## Changing the Service Name for DNS

Within the service settings you can change the service name to which you refer, e.g. api-1.railway.internal -> api-2.railway.internal

The root of the domain, railway.internal, is static and **cannot** be changed.

## Caveats

During the feature development process we found a few caveats that you should be aware of:

- Private networking is not available during the build phase.
- You will need to bind to a IPv6 port to receive traffic on the private network.
- We don't support IPv4 private networking

## FAQ

<Collapse title="What is a client side app, a server side app, and what kind of app am I running?">

In the context of private networking, the key distinction between client- and server-side is from where requests are being made.

- In client-side applications, requests to other resources (like other Railway services) are made from a browser, which exists on the public network and outside the private network.
- In server-side applications, requests to other resources are made from the server hosting the application, which would exist within the private network (assuming the server hosting the app is in Railway).

One way to determine whether your application is making client- or server-side requests is by inspecting the request in the Network tab of DevTools. If the RequestURL is the resource to which the request is being made, e.g. a backend server, this is a good indication that the browser itself is making the request (client-side).

</Collapse>

<Collapse title="What if I am making a request server-side, but from Vercel?">

Since an application hosted on Vercel exists outside of the private network in Railway, requests coming from Vercel servers cannot be made over the private network.

</Collapse>

## Code Examples

const port = process.env.PORT || 3000;

app.listen(port, "::", () => {
  console.log(`Server listening on [::]${port}`);
});

const port = process.env.PORT || 3000;

async function bootstrap() {
  await app.listen(port, "::");
}

next start --hostname :: --port ${PORT-3000}

const port = process.env.PORT || 3000;

const app = next({
  // ...
  hostname: "::",
  port: port,
});

gunicorn app:app --bind [::]:${PORT-3000}

hypercorn app:app --bind [::]:${PORT-3000}

uvicorn app:app --host :: --port ${PORT-3000}

app.get("/fetch-secret", async (req, res) => {
  axios.get("http://api.railway.internal:3000/secret").then(response => {
    res.json(response.data);
  });
});

BACKEND_URL=http://${{api.RAILWAY_PRIVATE_DOMAIN}}:${{api.PORT}}

app.get("/fetch-secret", async (req, res) => {
  axios.get(`${process.env.BACKEND_URL}/secret`).then(response => {
    res.json(response.data);
  });
});

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL + "?family=0");

const ping = await redis.ping();

import { Queue } from "bullmq";

const redisURL = new URL(process.env.REDIS_URL);

const queue = new Queue("Queue", {
  connection: {
    family: 0,
    host: redisURL.hostname,
    port: redisURL.port,
    username: redisURL.username,
    password: redisURL.password,
  },
});

const jobs = await queue.getJobs();

console.log(jobs);

docker-entrypoint.sh mongod --ipv6 --bind_ip ::,0.0.0.0

const StatsD = require("hot-shots");

const statsdClient = new StatsD({
  host: process.env.AGENT_HOST,
  port: process.env.AGENT_PORT,
  protocol: "udp",
  cacheDns: true,
  udpSocketOptions: {
    type: "udp6",
    reuseAddr: true,
    ipv6Only: true,
  },
});

app := fiber.New(fiber.Config{
    Network:       "tcp",
    ServerHeader:  "Fiber",
    AppName: "Test App v1.0.1",
})


# Build Configuration
Source: https://docs.railway.com/guides/build-configuration

Learn how to configure Railpack, optimize build caching, and set up watchpaths.



## Railpack

Railway uses <a href="https://railpack.com" target="_blank">Railpack</a> to
build your code. It works with zero configuration, but can be customized using
environment variables or a config
file. Configuration options include:

- Language versions
- Build/install/start commands
- Mise and Apt packages to install
- Directories to cache

For a full list of configuration options, please view the <a
href="https://railpack.com/config/environment-variables"
target="_blank">Railpack docs</a>. You can find a complete list of languages we
support out of the box here.

## Nixpacks

<DeprecationBanner>
Nixpacks is deprecated and in maintenance mode. New services default to Railpack.
</DeprecationBanner>

Existing services will continue to work with Nixpacks. To migrate to Railpack, update your service settings or set "builder": "RAILPACK" in your railway.json file.

For services still using Nixpacks, it can be configured with environment variables. For a full list of options, view the <a href="https://nixpacks.com/docs/guides/configuring-builds" target="_blank">Nixpacks docs</a>.

You can find a complete list of languages we support out of the box here.

## Customize the Build Command

You can override the detected build command by setting a value in your service
settings. This is run after languages and packages have been installed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192207/docs/build-command_bwdprb.png"
alt="Screenshot of Railway Build Command"
layout="responsive"
width={1200} height={373} quality={80} />

## Set the Root Directory

The root directory defaults to / but can be changed for various use-cases like
monorepo projects.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/root-directory_nfzkfi.png"
alt="Screenshot of Root Directory"
layout="responsive"
width={1200} height={421} quality={80} />

When specified, all build and deploy
commands will operate within the defined root directory.

**Note:** The **Railway Config File** does not follow the **Root Directory** path. You have to specify the absolute path for the railway.json or railway.toml file.

## Configure Watch Paths

Watch paths are <a href="https://git-scm.com/docs/gitignore#_pattern_format" target="_blank">gitignore-style</a> patterns
that can be used to trigger a new deployment based on what file paths have
changed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/watch-paths_zv62py.png"
alt="Screenshot of Railway Watch Paths"
layout="responsive"
width={1200} height={456} quality={80} />

For example, a monorepo might want to only trigger builds if files are
changed in the /packages/backend directory.

When specified, any changes that
don't match the patterns will skip creating a new deployment. Multiple patterns
can be combined, one per line.

_Note, if a Root Directory is provided, patterns still operate from /. For a root directory of /app, /app/**.js would be used as a pattern to match files in the new root._

Here are a few examples of common use-cases:

_Note, negations will only work if you include files in a preceding rule._

## Install Specific Packages using Railpack

| Environment variable            | Description                                                    |
|---------------------------------|----------------------------------------------------------------|
| RAILPACK_PACKAGES             | A list of Mise packages to install    |
| RAILPACK_BUILD_APT_PACKAGES   | Install additional Apt packages during build                   |
| RAILPACK_DEPLOY_APT_PACKAGES  | Install additional Apt packages in the final image             |

See the Railpack docs for more information.

## Procfiles

Railpack automatically detects commands defined in
Procfiles. Although this is not
recommended and specifing the start command directly in your service settings is
preferred.

## Specify a Custom Install Command

You can override the install command by setting the RAILPACK_INSTALL_COMMAND
environment variable in your service settings.

## Disable Build Layer Caching

By default, Railway will cache build layers to provide faster build times. If
you have a need to disable this behavior, set the following environment variable
in your service:

## Why Isn't My Build Using Cache?

Since Railway's build system scales up and down in response to demand, cache hit
on builds is not guaranteed.

If you have a need for faster builds and rely on build cache to satisfy that
requirement, you should consider creating a pipeline to build your own image and
deploy your image directly.

## Code Examples

# Match all TypeScript files under src/
/src/**/*.ts

# Match Go files in the root, but not in subdirectories
/*.go

# Ignore all Markdown files
**
!/*.md

NO_CACHE=1


# Dockerfiles
Source: https://docs.railway.com/guides/dockerfiles

Learn Dockerfile configuration on Railway.

Railway notifies you when it's using the Dockerfile in the build process with the following message in the logs:

## Custom Dockerfile Path

By default, we look for a file named Dockerfile in the root directory. If you want to use a custom filename or path, you can set a variable defining the path.

In your service variables, set a variable named RAILWAY_DOCKERFILE_PATH to specify the path to the file.

For example, if your Dockerfile was called Dockerfile.origin, you would specify it like this:

If your Dockerfile is in another directory, specify it like this:

### Use Config as Code

You can also set your custom Dockerfile path using config as code.

## Using Variables at Build Time

If you need to use the environment variables that Railway injects at build time, which include variables that you define and Railway-provided variables, you must specify them in the Dockerfile using the ARG command.

For example:

Be sure to declare your environment variables in the stage they are required in:

## Cache Mounts

Railway supports cache mounts in your Dockerfile in the following format:

Replace <service id> with the id of the service. 

<Banner variant="info">
    Environment variables can't be used in cache mount IDs, since that is invalid syntax.
</Banner>

### Target Path

Unsure of what your target path should be? Refer to the <a href="https://github.com/railwayapp/nixpacks/tree/main" target="_blank">Nixpacks source code</a>. Within the providers directory, find the file that aligns with your respective language or runtime, and check for the variable that indicates the CACHE_DIR.

**Example**

As an example, within the <a href="https://github.com/railwayapp/nixpacks/blob/main/src/providers/python.rs#L24" target="_blank">python provider definition</a>, you can see the PIP_CACHE_DIR is /root/.cache/pip.

So the mount command is specified like this:

## Docker Compose

You can import services straight from your Docker Compose file! Just drag and drop your Compose file onto your project canvas, and your services (and any mounted volumes) will be auto-imported as staged changes. Itâ€™s like magic, but with YAML instead of wands. ðŸª„

A quick heads-up: we donâ€™t support every possible Compose config just yet (because Rome wasnâ€™t built in a day). But donâ€™t worry, weâ€™re on it!

## Code Examples

==========================
Using detected Dockerfile!
==========================

RAILWAY_DOCKERFILE_PATH=Dockerfile.origin

RAILWAY_DOCKERFILE_PATH=/build/Dockerfile

# Specify the variable you need
ARG RAILWAY_SERVICE_NAME
# Use the variable
RUN echo $RAILWAY_SERVICE_NAME

FROM node

ARG RAILWAY_ENVIRONMENT

--mount=type=cache,id=s/<service id>-<target path>,target=<target path>

--mount=type=cache,id=s/<service id>-/root/cache/pip,target=/root/.cache/pip


# Pre-Deploy Command
Source: https://docs.railway.com/guides/pre-deploy-command

Learn how to execute commands between building and deploying your application.

They execute within your private network and have access to your application's environment variables.

If your command fails, it will not be retried and the deployment will not proceed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736533539/docs/pre-deploy-command_sp1zqh.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={1494} height={644} quality={80} />

For pre-deploy commands to work correctly, ensure that:

- It exits with a status code of 0 to indicate success or non-zero to indicate failure.
- It runs in a reasonable amount of time. It will occupy a slot in your build queue.
- It does not rely on the application running.
- It has the dependencies it needs to run installed in the application image.
- It does not attempt to read or write data to the volume or filesystem, that should instead be done as part of the start command.

<Banner variant="warning">Pre-deploy commands execute in a separate container from your application. Changes to the filesystem are not persisted and volumes are not mounted.</Banner>


# Start Command
Source: https://docs.railway.com/guides/start-command

Learn how to set up a start command in your service to run your deployments on Railway.

Railway automatically configures the start command based on the code being
deployed, see Build and Start Commands for more details

## Configure the Start Command

When necessary, start commands may be overridden, like for advanced use-cases such as deploying multiple projects from a single monorepo.

When specifying a start command, the behavior depends on the type of deployment:

- **Dockerfile / Image**: the start command overrides the image's ENTRYPOINT in <a href="https://docs.docker.com/reference/dockerfile/#shell-and-exec-form" target="_blank">exec form</a>.

  If you need to use environment variables in the start command for services deployed from a Dockerfile or image you will need to wrap your command in a shell -

  This is because commands ran in exec form do not support variable expansion.

- **Nixpacks**: the start command is ran in a shell process.

  This supports the use of environment variables without needing to wrap your command in a shell.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

## Dockerfiles & Images

If your service deploys with a Dockerfile or from an image, the start command defaults to the ENTRYPOINT and / or CMD defined in the Dockerfile.

## Code Examples

/bin/sh -c "exec python main.py --port $PORT"


# Deployment Actions
Source: https://docs.railway.com/guides/deployment-actions

Explore the full range of actions available on the Service Deployments tab to manage your deployments.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645148376/docs/deployment-photo_q4q8in.png"
alt="Screenshot of Deploy View"
layout="responsive"
width={1103} height={523} quality={80} />

## Rollback

Rollback to previous deployments if mistakes were made. To perform a rollback, click the three dots at the end of a previous deployment, you will then be asked to confirm your rollback.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645149734/docs/rollback_mhww2u.png"
alt="Screenshot of Rollback Menu"
layout="responsive"
width={1518} height={502} quality={80} />

A deployment rollback will revert to the previously successful deployment. Both the Docker
image and custom variables are restored during the rollback process.

_Note: Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible._

## Redeploy

A successful, failed, or crashed deployment can be re-deployed by clicking the three dots at the end of a previous deployment.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1666380373/docs/redeploy_ghinkb.png"
alt="Screenshot of Redeploy Menu"
layout="responsive"
width={888} height={493} quality={100} />

This will create an new deployment with the exact same code and build/deploy configuration.

_Note: To trigger a deployment from the latest commit, use the Command Palette: CMD + K -> "Deploy Latest Commit". This will deploy the latest commit from the **Default** branch in GitHub._

_Currently, there is no way to force a deploy from a branch other than the Default without connecting it in your service settings._

## Cancel

Users can cancel deployments in progress by clicking the three dots at the end
of the deployment tab and select Abort deployment. This will cancel the
deployment in progress.

## Remove

If a deployment is completed, you can remove it by clicking the three dots
at the end of the deployment tab and select Remove. This will remove the
deployment and stop any further project usage.

## Restart a Crashed Deployment

When a Deployment is Crashed, it is no longer running because the underlying process exited with a non-zero exit code - if your deployment exits successfully (exit code 0), the status will remain Success.

Railway automatically restarts crashed Deployments up to 10 times (depending on your Restart Policy). After this limit is reached, your deployment status is changed to Crashed and notifying webhooks & emails are sent to the project's members.

Restart a Crashed Deployment by visiting your project and clicking on the "Restart" button that appears in-line on the Deployment:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1643239507/crash-ui_b2yig1.png"
alt="Screenshot of Deploy Options"
layout="responsive"
width={947} height={156} quality={80} />

Restarting a crashed Deployment restores the exact image containing the code & configuration of the original build. Once the Deployment is back online, its status will change back to Success.

You can also click within a deployment and using the Command Palette restart a deployment at any state.

## Deployment Dependencies - Startup Ordering

You can control the order your services start up with Reference Variables.
When one service references another, it will be deployed after the service it is referencing when applying a staged change or duplicating an environment.

Services that have circular dependencies will simply ignore them and deploy as normal.

For example, let's say you're deploying an API service that depends on a PostgreSQL database.

When you have services with reference variables like:

- API Service has DATABASE_URL=${{Postgres.DATABASE_URL}} which is defined on your Postgres Service in the same project.

Railway will:

1. Deploy the Postgres Service first
2. Then deploy the API Service (since it has a reference variable to Postgres)


# GitHub Autodeploys
Source: https://docs.railway.com/guides/github-autodeploys

Learn how to configure GitHub autodeployments.



## Configure the GitHub Branch for Deployment Triggers

To update the branch that triggers automatic deployments, go to your Service Settings and choose the appropriate trigger branch.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1713907838/docs/triggerBranch_tzf9q3.png"
alt="Screenshot of GitHub Integration"
layout="responsive"
width={903} height={523} quality={80} />

### Disable Automatic Deployments

To disable automatic deployment, simply hit Disconnect in the Service Settings menu.

_Note: To manually trigger a deployment from the latest commit, use the Command Palette: CMD + K -> "Deploy Latest Commit". This will deploy the latest commit from the **Default** branch in GitHub._

_Currently, there is no way to force a deploy from a branch other than the Default without connecting it in your service settings._

## Wait for CI

<Banner variant="info">
  Please make sure you have{" "}
  <a href="https://github.com/settings/installations" target="_blank">accepted our updated GitHub permissions</a>
  required for this feature to work.
</Banner>

To ensure Railway waits for your GitHub Actions to run successfully before triggering a new deployment, you should enable **Wait for CI**.

#### Requirements

- You must have a GitHub workflow defined in your repository.
- The GitHub workflow must contain a directive to run on push:

### Enabling Wait for CI

If your workflow satisfies the requirements above, you will see the Wait for CI flag in service settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1730324753/docs/deployments/waitforci_dkfsxy.png" alt="Check Suites Configuration" layout="responsive" width={1340} height={392} quality={80} />

Toggle this on to ensure Railway waits for your GitHub Actions to run successfully before triggering a new deployment.

When enabled, deployments will be moved to a WAITING state while your workflows are running.

If any workflow fails, the deployments will be SKIPPED.

When all workflows are successful, deployments will proceed as usual.

## Code Examples

on:
    push:
      branches:
        - main


# Optimize Performance
Source: https://docs.railway.com/guides/optimize-performance

Explore quick ways to optimize your app's performance on Railway.

Specifically, we offer the following features:

- Horizontal Scaling with Replicas where each individual replica can use the full resources your plan allows for. (Vertical scaling is done automatically)
- Regional Deployments

Continue reading for information on how to configure these.

## Configure Horizontal Scaling

Scale horizontally by manually increasing the number of replicas for a service.

Each replica has access to the full resources allocated by your plan. For instance, with the Pro plan, each of your replicas can utilize up to 32 vCPU and 32GB of memory, for example, if you had 2 replicas, your service would be able to utilize up to 64 vCPU and 64GB of memory split between the 2 replicas.

Railway's infrastructure spans multiple regions across the globe, and by default Railway deploys to your preferred region.

<Image 
    src="https://res.cloudinary.com/railway/image/upload/v1733386054/multi-region-replicas_zov7rv.png"
    alt="Multi-region replicas"
    layout="responsive"
    width={1370}
    height={934}
/>

To change the number of replicas per deploy within your service, go to the service settings view and look for the "Regions" field in the "Deploy" section. This will create multiple instances of your service and distribute traffic between them.

_Additional regions may be added in the future as Railway continues expanding its infrastructure footprint._

### Replica ID Environment Variable

Each replica will be deployed with a Railway-provided environment variable named RAILWAY_REPLICA_ID which can be used for logging and monitoring, for example.

### Replica Region Environment Variable

Each replica will be deployed with a Railway-provided environment variable named RAILWAY_REPLICA_REGION which can be used for logging and monitoring, for example.

### Load Balancing Between Replicas

If you are using multi-region replicas, Railway will automatically route public traffic to the nearest region and then randomly distribute requests to the replicas within that region.

If you are using a single region with multiple replicas, Railway will randomly distribute public traffic to the replicas of that region.

**Note:** For now Railway does not support sticky sessions nor report the usage of the individual replicas within the metrics view, all metrics are aggregated across all replicas in all regions.

### Set a Preferred Region

To set a default or preferred region, do so from your Workspace Settings.

### Impact of Region Changes

For information on the impact of changing a service's region, see the Regions reference guide.

## Singleton Deploys

By default, Railway maintains only one deploy per service.


# Healthchecks
Source: https://docs.railway.com/guides/healthchecks

Learn how to configure health checks to guarantee zero-downtime deployments of services on Railway.



## Configure The Healthcheck Path

A Healthcheck can be used to guarantee zero-downtime deployments of your web services by ensuring the new version is live and able to handle requests.

To configure a healthcheck:

1. Ensure your webserver has an endpoint (e.g. /health) that will return an HTTP status code of 200 when the application is live and ready.

2. Under your service settings, input your health endpoint. Railway will wait for this endpoint to serve a 200 status code before switching traffic to your new endpoint

**Note:** Railway does not monitor the healthcheck endpoint after the deployment has gone live.

## Configure The Healthcheck Port

Railway will inject a PORT environment variable that your application should listen on.

This variable's value is also used when performing health checks on your deployments.

If your application doesn't listen on the PORT variable, possibly due to using target ports, you can manually set a PORT variable to inform Railway of the port to use for health checks.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743469112/healthcheck-port_z0vj4o.png"
alt="Screenshot showing PORT service variable configuration"
layout="intrinsic"
width={1200} height={307} quality={100} />

Not listening on the PORT variable or omitting it when using target ports can result in your health check returning a service unavailable error.

### Healthcheck Timeout

The default timeout on healthchecks is by default 300 seconds (5 minutes) - if your application fails to serve a 200 status code during this allotted time, the deploy will be marked as failed.

<Image 
src="https://res.cloudinary.com/railway/image/upload/v1664564544/docs/healthcheck-timeout_lozkiv.png"
alt="Screenshot of Healthchecks Timeouts"
layout="intrinsic"
width={1188} height={348} quality={80} />

To increase the timeout, change the number of seconds on the service settings page, or with a RAILWAY_HEALTHCHECK_TIMEOUT_SEC service variable.

### Services with Attached Volumes

To prevent data corruption, we prevent multiple deployments from being active and mounted to the same service. This means that there will be a small amount of downtime when re-deploying a service that has a volume attached, even if there is a healthcheck endpoint configured.

### Healthcheck Hostname

Railway uses the hostname healthcheck.railway.app when performing healthchecks on your service. This is the domain from which the healthcheck requests will originate.

For applications that restrict incoming traffic based on the hostname, you'll need to add healthcheck.railway.app to your list of allowed hosts. This ensures that your application will accept healthcheck requests from Railway.

If your application does not permit requests from that hostname, you may encounter errors during the healthcheck process, such as "failed with service unavailable" or "failed with status 400".

### Continuous Healthchecks

The healthcheck endpoint is currently **_not used for continuous monitoring_** as it is only called at the start of the deployment, to ensure it is healthy prior to routing traffic to it.

If you are looking for a quick way to setup continuous monitoring of your service(s), check out the <a href="https://railway.com/template/p6dsil" target="_blank">Uptime Kuma template</a> in our template marketplace.


# Restart Policy
Source: https://docs.railway.com/guides/restart-policy

Learn how to configure the restart policy so that Railway can automatically restart your service if it crashes.

**Note:** For services with multiple replicas, a restart will only affect the replica that crashed, while the other replica(s) continue handling the workload until the restarted replica is back online.

The default is On Failure with a maximum of 10 restarts.

To configure a different restart policy, go to the Service settings and select a different policy from the dropdown.

#### What does each policy mean?

- Always: Railway will automatically restart your service every time it stops, regardless of the reason.

- On Failure: Railway will only restart your service if it stops due to an error (e.g., crashes, exits with a non-zero code).

- Never: Railway will never automatically restart your service, even if it crashes.

#### Plan limitations

Users on the Free plan and those trialing the platform have some limitations on the restart policy:

- Always Is not available.

- On Failure is limited to 10 restarts.

Users on paid plans can set any restart policy with any number of restarts.


# Deployment Teardown
Source: https://docs.railway.com/guides/deployment-teardown

Learn how to configure the deployment lifecycle to create graceful deploys with zero downtime.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1750178677/docs/deployment-teardown-guide/s5pqob0j8nreoojbo6dj.png"
alt="Screenshot of a teardown settings"
layout="responsive"
width={642} height={324} quality={80}/>

To learn more about the full deployment lifecycle, see the deploy reference.

#### Overlap Time

Once the new deployment is active, the previous deployment remains active for a configurable amount of time. You can control this via the "Settings" pane for the service. It can also be configured via code or the RAILWAY_DEPLOYMENT_OVERLAP_SECONDS service variable.

#### Draining Time

Once the new deployment is active, the previous deployment is sent a SIGTERM signal and given time to gracefully shutdown before being forcefully stopped with a SIGKILL. The time to gracefully shutdown can be controlled via the "Settings" pane. It can also be configured via code or the RAILWAY_DEPLOYMENT_DRAINING_SECONDS service variable.


# Monorepo
Source: https://docs.railway.com/guides/monorepo

Learn how to deploy monorepos on Railway.

1. **Isolated Monorepo** â†’ A repository that contains components that are completely isolated to the
   directory they are contained in (eg. JS frontend and Python backend)
1. **Shared Monorepo** â†’ A repository that contains components that share code or configuration from the root directory (eg. Yarn workspace or Lerna project). We support **automated import of Javascript monorepos** for pnpm, npm, yarn or bun monorepos.

For a full step by step walk through on deploying an isolated Monorepo see our <a href="/tutorials/deploying-a-monorepo" target="_blank">tutorial</a> on the subject.

## Deploying an Isolated Monorepo

The simplest form of a monorepo is a repository that contains two completely
isolated projects that do not share any code or configuration.

To deploy this type of monorepo on Railway, define a root directory for the service.

1. Select the service within the project canvas to open up the service view.
2. Click on the Settings tab.
3. Set the root directory option. Setting this means that Railway will only pull down files from that directory when creating new deployments.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798659/docs/root-directory_achzga.png"
alt="Screenshot of root directory configuration"
layout="intrinsic"
width={980} height={380} quality={80} />

**Note:** The **Railway Config File** does not follow the **Root Directory** path. You have to specify the absolute path for the railway.json or railway.toml file.

## Deploying a Shared Monorepo

Popular in the JavaScript ecosystem, shared monorepos contain multiple components that all share a common root directory.

By default, all components are built with a single command from the root directory (e.g. npm run build). However, if you are using Nixpacks, then you can override the build command in the service settings.

To deploy this type of monorepo in Railway, define a separate custom start
command in Service Settings for each project that references the monorepo
codebase.

1. Select the service within the project canvas to open the service view.
2. Click on the Settings tab.
3. Set the start command, e.g. npm run start:backend and npm run start:frontend

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

## Automatic Import for Javascript Monorepos

When you import a Javascript monorepo via the project creation page, we automatically detect if it's a monorepo and stage a service for each deployable package. This works for pnpm, npm, yarn and bun.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1758927698/docs/guides/monorepos/monorepo-import-new-page_izirrr.png"
alt="Importing a monorepo from /new"
layout="intrinsic"
width={905} height={642} quality={80} />

<Image
src="https://res.cloudinary.com/railway/image/upload/v1758927701/docs/guides/monorepos/monorepo-import-result_jbtccl.png"
alt="Staged monorepo services"
layout="intrinsic"
width={1369} height={714} quality={80} />

For each package detected, Railway automatically configures:

- **Service Name**: generated from the package name or directory
- **Start Command**: workspace-specific commands like pnpm --filter [package] start
- **Build Command**: workspace-specific commands like pnpm --filter [package] build
- **Watch Paths**: set to the package directory (e.g., /packages/backend/**)
- **Config as Code**: railway.json / railway.toml are detected at the root of the package directory

Railway filters out non-deployable packages such as configuration packages (eslint, prettier, tsconfig) and test packages.

## Watch paths

To prevent code changes in one service from triggering a rebuild of other services in your monorepo, you should configure watch paths.

Watch paths are <a href="https://git-scm.com/docs/gitignore#_pattern_format" target="_blank">gitignore-style</a> patterns that can be used to trigger a new deployment based on what file paths have changed.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192841/docs/watch-paths_zv62py.png"
alt="Screenshot of Railway Watch Paths"
layout="responsive"
width={1200} height={456} quality={80} />

A monorepo might want to only trigger builds if files are changed in the /packages/backend directory, for example.

## Using the CLI

When interacting with your services deployed from a monorepo using the CLI, always ensure you are "linked" to the appropriate service when executing commands.

To link to a specific service from the CLI, use railway link and follow the prompts.

## Code Examples

â”œâ”€â”€ frontend/
â”‚   â”œâ”€â”€ index.js
â”‚   â””â”€â”€ ...
â””â”€â”€ backend/
    â”œâ”€â”€ server.py
    â””â”€â”€ ...

â”œâ”€â”€ package.json
â””â”€â”€ packages
    â”œâ”€â”€ backend
    â”‚   â””â”€â”€ index.js
    â”œâ”€â”€ common
    â”‚   â””â”€â”€ index.js
    â””â”€â”€ frontend
        â””â”€â”€ index.jsx


# Cron Jobs
Source: https://docs.railway.com/guides/cron-jobs

Learn how to run cron jobs on Railway.

Services configured as cron jobs are expected to execute a task, and terminate as soon as that task is finished, leaving no open resources.

## Configuring a Cron Job

To configure a cron job -

1. Select a service and go to the Settings section.
2. Within "Cron Schedule", input a crontab expression.
3. Once the setting is saved, the service will run according to the cron schedule.

Find more information about cron jobs, including examples of cron expressions, in the reference page for Cron Jobs.

## Why Isn't My Cron Running as Scheduled?

An important requirement of a service that runs as a Cron, is that it terminates on completion and leaves no open resources. If the code that runs in your Cron service does not exit, subsequent executions of the Cron will be skipped.

If you see that a previous execution of your Cron service has a status of Active, the execution is still running and any new executions will not be run.

For more information on Service execution requirements, see the Service Execution Requirements section of the Cron Jobs reference.


# Optimize Usage
Source: https://docs.railway.com/guides/optimize-usage

Optimize your Railway projects for budget-friendly billing by setting limits and activating app sleep.



## Configuring Usage Limits

Usage Limits allow you to set a maximum limit on your usage for a billing cycle.

Visit the <a href="https://railway.com/workspace/usage" target="_blank">Workspace Usage page</a> to set the usage limits. Once you click the <kbd>Set Usage Limits</kbd> button, you will see a modal above where you can set a <kbd>Custom email alert</kbd> and a <kbd>Hard limit</kbd>.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743193518/docs/usage-limits_pqlot9.png" alt="Usage Limits Modal" layout="responsive" width={1200} height={1075} />

#### Setting Limits for Teams

If you want to set a usage limit for your team, use the account switcher in the top left corner of your dashboard to access the team's usage page.

### Custom Email Alert

Configure a soft limit by setting a threshold in Custom email alert. When your resource usage reaches the specified amount, we will email you that this threshold has been met and resources continue running.

### Hard Limit

Configure a hard limit to take resources offline once usage meets the specified threshold.

Multiple emails will be sent as your usage approaches your hard limit:

1. When your usage reaches 75% of your hard limit
2. When your usage reaches 90% of your hard limit
3. When your usage reaches 100% of your hard limit and workloads have been taken down.

<Banner variant="danger">Setting a hard limit is a possibly destructive action as you're risking having all your resources shut down once your usage crosses the specified amount.</Banner>

Find more information about Usage Limits in the reference page.

## Use Private Networking

Using Private Networking when communicating with other services (such as databases) within your Railway project will help you avoid unnecessary Network Egress costs.

### With Databases

Communicate with your Railway database over private networking by using the DATABASE_URL environment variable, instead of DATABASE_PUBLIC_URL:

### With Other Services

If your Railway services need to communicate with each other, you can find the service's private URL in the service settings:

<Image src="https://res.cloudinary.com/railway/image/upload/v1743193518/docs/private-networking_nycfyk.png" alt="Private Network URL" layout="responsive" width={1558} height={1156} />

Learn more about Railway's Private Networking here.

## Enabling Serverless

Enabling Serverless on a service tells Railway to stop a service when it is inactive, effectively reducing the overall cost to run it.

To enable Serverless, toggle the feature on within the service configuration pane in your project:

<Image src="https://res.cloudinary.com/railway/image/upload/v1696548703/docs/scale-to-zero/appSleep_ksaewp.png"
alt="Enable App Sleep"
layout="intrinsic"
width={700} height={460} quality={100} />

1. Navigate to your service's settings > Deploy > Serverless
2. Toggle "Enable Serverless"
3. To _disable_ Serverless, toggle the setting again

Read more about how Serverless works in the Serverless Reference page.

## Resource Limits

Resource limits are a way to limit the maximum amount of resources available to a service.

To toggle resource limits, navigate to your service's settings > Deploy > Resource Limits.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1721917970/resource-limits.png"
  alt="Resource Limits setting"
  layout="intrinsic"
  width={1298}
  height={658}
  quality={80}
/>

### Use Resource Limits

<Banner variant="warning">
Setting resource limits too low will cause your service to crash.
</Banner>

Using resource limits makes sense in scenarios where:

1. You don't want to risk a high bill due to unexpected spikes in usage
2. You are okay with the service crashing if it exceeds the limit


# Build a Database Service
Source: https://docs.railway.com/guides/build-a-database-service

Learn how to build a database service on Railway.

For the purpose of this guide, we will use the official <a href="https://hub.docker.com/_/postgres" target="_blank">Postgres image</a> as an example.

## Service Source

As discussed in the Services guide, a crucial step in creating a service is defining a source from which to deploy.

To deploy the official Postgres image, we'll simply enter postgres into the Source Image field:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464166/docs/databases/CleanShot_2023-12-01_at_14.54.35_2x_aa5gwt.png"
alt="Screenshot of a Docker image source"
layout="responsive"
width={559} height={168} quality={80} />

## Volumes

Attach a volume to any service, to keep your data safe between deployments. For the Postgres image, the default mount path is /var/lib/postgresql/data.

Just attach a volume to the service you created, at the mount path:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464411/docs/databases/mountpath_lajfam.png"
alt="Screenshot of a mount path"
layout="responsive"
width={519} height={168} quality={80} />

## Environment Variables

Now, all you need to do is configure the appropriate <a href="https://hub.docker.com/_/postgres#environment-variables:~:text=have%20found%20useful.-,Environment%20Variables,-The%20PostgreSQL%20image" target="_blank">environment variables</a> to let the Postgres image know how to run:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1701464670/docs/databases/envvars_aow79p.png"
alt="Screenshot of environment variables"
layout="responsive"
width={460} height={458} quality={80} />

Note the DATABASE_URL is configured with TCP Proxy variables, but you can also connect to the database service over the private network. More information below.

## Connecting

### Private Network

To connect to your database service from other services in your project, you can use the private network. For a postgres database service listening on port 5432, you can use a connection string like this -

### TCP Proxy

If you'd like to expose the database over the public network, you'll need to set up a TCP Proxy, to proxy public traffic to the Postgres port 5432:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743194081/docs/tcp-proxy_edctub.png"
alt="Screenshot of TCP proxy configuration"
layout="responsive"
width={1200} height={822} quality={100} />

## Conclusion

That's all it takes to spin up a Postgres service in Railway directly from the official Postgres image. Hopefully this gives you enough direction to feel comfortable exploring other database images to deploy.

Remember you can also deploy from a Dockerfile which would generally involve the same features and steps. For an example of a Dockerfile that builds a custom image with the official Postgres image as base, take a look at <a href="https://github.com/railwayapp-templates/postgres-ssl" target="_blank">Railway's SSL-enabled Postgres image repo</a>.

### Template Marketplace

Need inspiration or looking for a specific database? Our <a href="https://railway.com/templates" target="_blank">Template Marketplace</a> already includes solutions for many different database services. You might even find a template for the database you need!

Here are some suggestions to check out -

- <a href="https://railway.com/template/SMKOEA" target="_blank">Minio</a>
- <a href="https://railway.com/template/clickhouse" target="_blank">ClickHouse</a>
- <a href="https://railway.com/template/dragonfly" target="_blank">Dragonfly</a>
- <a href="https://railway.com/template/kbvIRV" target="_blank">Chroma</a>
- <a href="https://railway.com/template/elasticsearch" target="_blank">Elastic Search</a>

## Code Examples

postgresql://postgres:password@postgres.railway.internal:5432/railway


# PostgreSQL
Source: https://docs.railway.com/guides/postgresql

Learn how to deploy a PostgreSQL database on Railway.



## Deploy

Add a PostgreSQL database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed Service

Upon deployment, you will have a PostgreSQL service running in your project, deployed from Railway's SSL-enabled Postgres image, which uses the official Postgres image from Docker Hub as its base.

### Connect

Connect to the PostgreSQL server from another service in your project by referencing the environment variables made available in the PostgreSQL service:

- PGHOST
- PGPORT
- PGUSER
- PGPASSWORD
- PGDATABASE
- DATABASE_URL

_Note, Many libraries will automatically look for the DATABASE_URL variable and use
it to connect to PostgreSQL but you can use these variables in whatever way works for you._

#### Connecting Externally

It is possible to connect to PostgreSQL externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the Deployment

Since the deployed container is based on an image built from the official PostgreSQL image in Docker hub, you can modify the deployment based on the instructions in Docker hub.

We also encourage you to fork the Railway postgres-ssl repository to customize it to your needs, or feel free to open a PR in the repo!

## Backups and Observability

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out our native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your databases. If you're not already running an observability stack, check out these templates to help you get started building one:
  - Prometheus
  - Grafana
  - PostgreSQL Exporter

## Extensions

In an effort to maintain simplicity in the default templates, we do not plan to add extensions to the PostgreSQL templates covered in this guide.

For some of the most popular extensions, like PostGIS and Timescale, there are several options in the template marketplace.

- <a href="https://railway.com/template/VSbF5V" target="_blank">TimescaleDB</a>
- <a href="https://railway.com/template/postgis" target="_blank">PostGIS</a>
- <a href="https://railway.com/template/timescaledb-postgis" target="_blank">TimescaleDB + PostGIS</a>
- <a href="https://railway.com/template/3jJFCA" target="_blank">pgvector</a>

## Modifying The Postgres Configuration

You can modify the Postgres configuration by using the ALTER SYSTEM command.

After running the SQL, you will need to restart the deployment for the changes to take effect.

You can restart the deployment by clicking the Restart button in the deployment's 3-dot menu.

## Increasing the SHM Size

The SHM Size is the maximum amount of shared memory available to the container.

By default it is set to 64MB.

You would need to change the SHM Size if you are experiencing the following error -

You can modify the SHM Size by setting the RAILWAY_SHM_SIZE_BYTES variable in your service variables.

This variable is a number in bytes, so you would need to convert the size you want to use.

For example, to increase the SHM Size to 500MB, you would set the variable to 524288000.

## Additional Resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- PostgreSQL Documentation
- PostgreSQL High Availability Documentation
- Repmgr Documentation
- Pgpool-II Documentation

## Code Examples

ALTER SYSTEM SET shared_buffers = '2GB';
ALTER SYSTEM SET effective_cache_size = '6GB';
ALTER SYSTEM SET maintenance_work_mem = '512MB';
ALTER SYSTEM SET work_mem = '32MB';
ALTER SYSTEM SET max_worker_processes = '8';
ALTER SYSTEM SET max_parallel_workers_per_gather = '4';
ALTER SYSTEM SET max_parallel_workers = '8';

-- Reload the configuration to save the changes
SELECT pg_reload_conf();

ERROR: could not resize shared memory segment "PostgreSQL.1590182853" to 182853 bytes: no space left on device


# MySQL
Source: https://docs.railway.com/guides/mysql

Learn how to deploy a MySQL database on Railway.

### Deploy

Add a MySQL database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed Service

Upon deployment, you will have a MySQL service running in your project, deployed directly from the mysql Docker image.

### Connect

Connect to MySQL from another service in your project by referencing the environment variables made available in the MySQL service:

- MYSQLHOST
- MYSQLPORT
- MYSQLUSER
- MYSQLPASSWORD
- MYSQLDATABASE
- MYSQL_URL

#### Connecting Externally

It is possible to connect to MySQL externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the Deployment

Since the deployed container is pulled from the official MySQL image in Docker hub, you can modify the deployment based on the instructions in Docker hub.

## Backups and Observability

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out our native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your databases. If you're not already running an observability stack, check out these templates to help you get started building one:
  - Prometheus
  - Grafana

## Additional Resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- MySQL Documentation
- MySQL InnoDB Cluster Documentation
- MySQL Router Documentation


# Redis
Source: https://docs.railway.com/guides/redis

Learn how to deploy a Redis database on Railway.



## Deploy

Add a Redis database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed Service

Upon deployment, you will have a Redis service running in your project, deployed from the redis Docker image.

### Connect

Connect to the Redis server from another service in your project by referencing the environment variables made available in the Redis service:

- REDISHOST
- REDISUSER
- REDISPORT
- REDISPASSWORD
- REDIS_URL

#### Connecting Externally

It is possible to connect to Redis externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the Deployment

Since the deployed container is pulled from the redis image in Docker Hub, you can modify the deployment based on the instructions in Docker Hub.

## Backup and Monitoring

Especially for production environments, performing backups and monitoring the health of your data is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out our native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your Redis cluster. You can integrate a Redis exporter for Prometheus, although we do not provide a specific template at this time.

## Additional Resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- Redis Documentation
- Redis Replication
- High Availability with Redis Sentinel
- Understanding Sentinels


# MongoDB
Source: https://docs.railway.com/guides/mongodb

Learn how to deploy a MongoDB database on Railway.



## Deploy

Add a MongoDB database to your project via the ctrl / cmd + k menu or by clicking the + New button on the Project Canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695934218/docs/databases/addDB_qxyctn.gif"
alt="GIF of the Adding Database"
layout="responsive"
width={450} height={396} quality={100} />

You can also deploy it via the template from the template marketplace.

#### Deployed Service

Upon deployment, you will have a MongoDB service running in your project, deployed from the official mongo Docker image.

#### Custom Start Command

The MongoDB database service starts with the following Start Command to enable communication over Private Network: mongod --ipv6 --bind_ip ::,0.0.0.0  --setParameter diagnosticDataCollectionEnabled=false

## Connect

Connect to MongoDB from another service in your project by referencing the environment variables made available in the Mongo service:

- MONGOHOST
- MONGOPORT
- MONGOUSER
- MONGOPASSWORD
- MONGO_URL

#### Connecting Externally

It is possible to connect to MongoDB externally (from outside of the project in which it is deployed), by using the TCP Proxy which is enabled by default.

_Keep in mind that you will be billed for Network Egress when using the TCP Proxy._

### Modify the Deployment

Since the deployed container is pulled from the official MongoDB image in Docker Hub, you can modify the deployment based on the instructions in Docker Hub.

## Backup and Monitoring

Especially for production environments, performing regular backups and monitoring the health of your database is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out our native Backups feature.

- **Observability**: Implement monitoring for insights into performance and health of your database. Check out the tutorial which covers setting up observability on a Mongo replica set.

## Additional Resources

While these templates are available for your convenience, they are considered unmanaged, meaning you have total control over their configuration and maintenance.

We _strongly encourage you_ to refer to the source documentation to gain deeper understanding of their functionality and how to use them effectively. Here are some links to help you get started:

- Mongo Documentation
- Replication in Mongo


# Database View
Source: https://docs.railway.com/guides/database-view

Learn how to read, insert and edit data via the database view on Railway.



## SQL Interfaces

<Image src="https://res.cloudinary.com/railway/image/upload/v1701904581/docs/databases/dataTab_vtj7me.png"
alt="Screenshot of Postgres Service Panel"
layout="intrinsic"
width={995} height={528} quality={80} />

For MySQL and Postgres, Railway displays the tables contained within an instance by default; this is called the Table View.

Shift-clicking on one or multiple tables exposes additional options such as the ability to delete the table(s).

### Creating a Table

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/table_create_kuvnjg.png"
alt="Screenshot of Create Table interface"
layout="intrinsic"
width={928} height={396} quality={80} />

Under the Table View, clicking the Create Table button at the bottom right of the interface navigates users to the Create Table interface.

For each column a user wants to add to the database, the interface accepts a name, type, default_value and constraints. Depending on the SQL database that is used, valid types and constraints may vary.

### Viewing and Editing Entries

When a table is clicked, the interface navigates into the Entries View.

Under the Entries View, selecting an existing entry exposes the ability to edit the entry. When button that allows one to add entries to the table.

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/edit_row_tobmdh.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={803} height={457} quality={80} />

### Add SQL Column

Selecting the add column in the entries view opens a modal that prompts you to add a new column to the table.

## NoSQL Interfaces

For non-structured data, Railway has interfaces that permit users to add and edit data within the service.

### Redis View

<Image src="https://res.cloudinary.com/railway/image/upload/v1636426105/docs/redis_view_jna8ho.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={732} height={419} quality={80} />

With Redis, Railway displays the keys contained within a database instance by default.

### MongoDB Document View

With MongoDB, Railway displays a list of document collections. Users can add additional collections or add/edit documents within the collection.

### Adding MongoDB Databases

<Image src="https://res.cloudinary.com/railway/image/upload/v1636424673/docs/add_mongo_db_ujjcgr.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={552} height={516} quality={80} />

Within the Collections View, clicking the plus icon next to the top dropdown allows you to create a new Database.

## Credentials Tab

The Credentials tab allows you to safely regenerate your database password while keeping the database and environment variables synchronized, avoiding manual variable edits that can cause authentication mismatches.

It's important to manually redeploy any service that depends on the updated password variable (or the derived database URL).

<Image src="https://res.cloudinary.com/railway/image/upload/t_crop/v1756840714/Database_Credentials_ctbwqb.png"
alt="Screenshot of Credentials Data UI Tab"
layout="intrinsic"
width={542} height={422} quality={80} />

## Extensions Tab for Postgres

The Extensions tab enables postgres extensions management. You can view, install and uninstall extensions that are available in our Postgres image.

Extensions that aren't available need to be deployed from templates, since they require additional features in the database's image, like pgvector.

<Image src="https://res.cloudinary.com/railway/image/upload/t_crop/v1756840713/Database_Extensions_flszw9.png"
alt="Screenshot of Extensions Data UI Tab"
layout="intrinsic"
width={540} height={422} quality={80} />


# Logs
Source: https://docs.railway.com/guides/logs

Learn how to view and filter build, deployment, environment, and HTTP logs on Railway.

There are three ways to view logs in Railway.

- **Build/Deploy Panel** â†’ Click on a deployment in the dashboard
- **Log Explorer** â†’ Click on the Observability tab in the top navigation
- **CLI** â†’ Run the railway logs command

## Build / Deploy Panel

Logs for a specific deployment can be viewed by clicking on the deployment in the service window, useful when debugging application failures.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1722993852/docs/CleanShot_2023-09-08_at_10.55.06_2x_co6ztr.png"
alt="deploy logs for a specific deployment"
layout="responsive"
width={1365} height={790} quality={80} />

Similarly, logs for a specific build can be viewed by clicking on the **Build Logs** tab once you have a deployment open.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1722993947/docs/build_logs_og7uec.png"
alt="deploy logs for a specific deployment"
layout="responsive"
width={1365} height={790} quality={80} />

## Log Explorer

Logs for the entire environment can be viewed together by clicking the "Observability" button in the top navigation. The Log Explorer is useful for debugging more general problems that may span multiple services.

The log explorer also has additional features like selecting a date range or toggling the visibility of specific columns.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1694194133/docs/log-explorer_nrlong.png"
alt="Railway Log Explorer"
layout="responsive"
width={1166} height={650} quality={80} />

## Command Line

Deployment logs can also be viewed from the command line to quickly check the current status of the latest deployment. Use railway logs to view them.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1694195563/docs/CleanShot_2023-09-08_at_10.52.12_2x_yv1d7f.png"
alt="Viewing logs using the command line interface"
layout="responsive"
width={1489} height={591} quality={80} />

## Filtering Logs

Railway supports a custom filter syntax that can be used to query logs.

Filter syntax is available for all log types, but some log types have specific attributes.

### Deployment Logs

- "<search term>" â†’ Filter for a partial substring match

- replica:<replica_id> â†’ Filter by a specific replica's UUID

- @attribute:value â†’ Filter by custom attribute (see structured logs below)

**Examples:**

Find logs that contain the word request.

Find logs that contain the substring POST /api.

Find logs with an error level.

Find logs with a warning level.

Find logs with an error level that contain specific text.

Find logs with a specific custom attribute.

Find logs with a specific array attribute.

### Environment Logs

Environment logs allow you to query for logs from the environment they were emitted in.

This means that you can search for logs emitted by all services in an environment at the same time, all in one central location.

In addition to the filters available for deployment logs, an additional filter is available for environment logs:

- @service:<service_id> â†’ Filter by a specific service's UUID

**Examples:**

Filter out logs from the Postgres database service.

Filter logs from the Postgres database service and the Redis cache service.

Show only logs from the Postgres database and Redis cache services.

### HTTP Logs

HTTP logs use the same filter syntax, but have a specific set of attributes for HTTP-specific data.

Some commonly used filters for HTTP logs are:

- @requestId:<request_id> â†’ Filter by request ID

- @timestamp:<timestamp> â†’ Filter by timestamp (Formatted in RFC3339)

- @method:<method> â†’ Filter by method

- @path:<path> â†’ Filter by path

- @host:<host> â†’ Filter by host

- @httpStatus:<status_code> â†’ Filter by HTTP status code

- @responseDetails:<details> â†’ Filter by response details (Only populated when the application fails to respond)

- @clientUa:<user_agent> â†’ Filter by a specific client's user agent

- @srcIp:<ip> â†’ Filter by source IP (The client's IP address that made the request)

- @edgeRegion:<region> â†’ Filter by edge region (The region of the edge node that handled the request)

**Examples:**

Find logs for a specific path.

Find logs for a specific path that returned a 500 error.

Find logs for a specific path that returned a 500 or 501 error.

Find all non-200 responses.

Find all requests that originated from or around Europe.

Find all requests that originated from a specific IP address.

## View In Context

When searching for logs, it is often useful to see surrounding logs. To view a log in context:
right-click any log, then select the "View in Context" option from the dropdown menu.

## Structured Logs

Structured logs are logs emitted in a structured JSON format, useful if you want
to attach custom metadata to logs or preserve multi-line logs like stack traces.

Structured logs are best generated with a library for your language. For example, the default <a href="https://github.com/winstonjs/winston" target="_blank">Winston</a>. JSON format emits logs in the correct structure by default.

Logs with a level field will be coloured accordingly in the log explorer.

Logs emitted to stderr will be converted to level.error and coloured red.

### Examples

Here are a few examples of structured logs.

**Note:** The entire JSON log must be emitted on a single line to be parsed correctly.

### Normalization Strategy

In order to ensure a consistent query format across Railway services, incoming logs are normalized to the above format automatically.

- Non-structured logs are converted to {"message":"...","level":"..."}

- log.msg converted to log.message

- log.level converted to log.severity

- Logs from stderr are converted to level.error

- Logs from stdout are converted to level.info

- Levels are lowercased and matched to the closest of debug, info, warn, error

## Code Examples

request

"POST /api"

@level:error

@level:warn

@level:error AND "failed to send batch"

@customAttribute:value

@arrayAttribute[i]:value

-@service:<postgres_service_id>

-@service:<postgres_service_id> AND -@service:<redis_service_id>

@service:<postgres_service_id> OR @service:<redis_service_id>

@path:/api/v1/users

@path:/api/v1/users AND @httpStatus:500

@path:/api/v1/users AND (@httpStatus:500 OR @httpStatus:501)

-@httpStatus:200

@edgeRegion:europe-west4-drams3a

@srcIp:66.33.22.11

console.log(
  JSON.stringify({
    message: "A minimal structured log", // (required) The content of the log
    level: "info", // Severity of the log (debug, info, warn, error)
    customAttribute: "value", // Custom attributes (query via @name:value)
  }),
);

{ "level": "info", "message": "A minimal structured log" }

{ "level": "error", "message": "Something bad happened" }

{ "level": "info", "message": "New purchase!", "productId": 123, "userId": 456 }

{
  "level": "info",
  "message": "User roles updated",
  "roles": ["editor", "viewer"],
  "userId": 123
}


# Observability
Source: https://docs.railway.com/guides/observability

Explore the built-in observability dashboard on Railway.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1717179720/Wholescreenshot_vc5l5e.png"
alt="Screenshot of the Observability Dashboard"
layout="responsive"
width={1111} height={649} quality={80} />

Shape the future of this dashboard! We are actively collecting feedback on usecases and bugs you may encounter.

## Navigating to the Observability Dashboard

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743129656/docs/observability_hsja97.png"
alt="Screenshot of the Updated Project Navigation"
layout="responsive"
width={1200} height={260} quality={80} />

_Users may notice that the project navigation is updated with the feature._

1. Navigate to the Observability tab from the main project top bar.
2. Ensure you are in the correct environment (e.g., production).

The Observability Dashboard is uniquely scoped to each project environment as services may differ between each environment.

### Getting Started

By default the Observability Dashboard starts with no configured widgets.

- When you first access a new environment, you will be prompted to "Start with a simple dashboard" or "Add new item".
- Click on "Start with a simple dashboard" to create your initial layout, Railway will autogenerate graphs and widgets with spend, service metrics and logs.

## Creating Widgets

Clicking "New" in the top right corner of the dashboard will open the Widget creation modal. Widget types depend on the data source provided, where they can be a graph, displayed data, or logs.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1717179725/erroronly_xdfscq.png"
alt="Screenshot of the Widget Creation Flow"
layout="responsive"
width={1101} height={830} quality={80} />

Widgets have a name and a description attached to them. By default Railway will provide a suggested name for the widget upon creation and display a preview of the content that is to be displayed on the dashboard.

### Available Data Sources

On the top right, you can select a data source to display within a widget.

- CPU Usage: Track the CPU usage for various services over time.
- Memory Usage: Monitor the memory consumption for your services.
- Network In/Out: Keep track of network traffic.
- Disk Usage: Observe disk usage trends.
- Logs: Select logs from a single service or multiple services with filtering
- Project Usage: report the spend of your project and track the overall resource usage of your project.

### Filtering Widget Information

When creating a widget, you can use Railway's filtering syntax to select services, select data, and perform logical negations to define rules.

- <keyword> or "key phrase" â†’ Filter by exact text
- @key:value â†’ Filter by key/value pair
  - Valid keys are replica, deployment, service, plugin
- @attribute:value â†’ Filter by custom attribute (see structured logs below)

Any of the above expressions can be combined with boolean operators AND,
OR, and - (negation).

## Arranging the Dashboard

The Dashboard is customizable in content and layout. Widgets can be stacked, repositioned and resized.

Clicking the "Edit" button on the top right corner of the dashboard will transition the dashboard into edit mode, the dashboard then allows the ability to resize and reposition your widgets using the provided handle on each widget. To persist your changes, select "Save".

<Image
src="https://res.cloudinary.com/railway/image/upload/v1717179246/dragandmoveob_xg6qfz.gif"
alt="Screenshot of Widget Interaction"
layout="responsive"
width={800} height={491} quality={80} />

Resizing and Moving Widgets:

- Drag and drop items to rearrange them on the grid by dragging the arrow handle.
- Resize widgets by dragging the bottom right corner handle

_Note for Small Screens: On smaller screens, items stack vertically and respect their configured height to ensure readability and usability. Editing is disabled at smaller visual breakpoints._

## Editing/Deleting Widgets

Under Edit mode, each widget will have a three dot menu at the upper right corner at the bounding box of the widget. Clicking into this menu will allow you to edit the data source or delete the widget.

To persist your changes, make sure you press Save at the top right corner.


# Metrics
Source: https://docs.railway.com/guides/metrics

Discover resource usage for your services on Railway via the Metrics tab.



## Accessing Service Metrics

Access a service's metrics by clicking on a service in the project canvas, and going to the "Metrics" tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1758559063/docs/metrics-sum_tvdwlc.png"
alt="Screenshot of Metrics Page"
layout="intrinsic"
width={1576} height={1100} quality={80} />

The following metrics are provided -

- CPU
- Memory
- Disk Usage
- Network

## Understanding the Metrics Graphs

Graphs include dotted lines to indicate when new deployments began. Up to 30 days of data is available for each project.

<Image src="https://res.cloudinary.com/railway/image/upload/v1645223703/docs/usage-commit_fkvbqj.png"
alt="Screenshot of Metric Timeseries Commit Information"
layout="responsive"
width={904} height={726} quality={80} />

Projects maintain a continuous time-series for all deployments within a service, not just the latest one. Deployments appear on the graph so users can see which commit may have caused a spike in resources.

If a service has multiple replicas, you can view metrics as a combined sum or per replica. Learn more in the Metrics Reference.


# Webhooks
Source: https://docs.railway.com/guides/webhooks

Learn how to set up webhooks on Railway to receive real-time updates for deployments and events.



## Setup a Webhook

<Image src="https://res.cloudinary.com/railway/image/upload/v1743196876/docs/new-webhook_lrfxxa.png"
alt="New Webhook"
layout="responsive"
width={1200} height={754} quality={80} />

Complete the following steps to setup a webhook:

1. Open an existing Project on Railway.
1. Click on the Settings button in the top right-hand corner.
1. Navigate to the Webhooks tab.
1. Input your desired webhook URL.
1. Optional: specify which events to receive notifications for.
1. Click Save Webhook.

The URL you provide will receive a webhook payload when any service's deployment status changes or an alert is triggered. This will be executed across all environments in the project.

#### Example Payload

#### Testing Webhooks

The Test Webhook button will send a test payload to the specified webhook URL.

Note: For security reasons, test webhooks are sent from the frontend client, which may result in Cross-Origin Resource Sharing (CORS) restrictions. This typically presents as a delivery failure when using the test webhook functionality.

## Muxers: Provider-specific Webhooks

For certain webhook URLs, Railway will automatically transform the payload to match the destination (we call the Muxers). This makes it easy to use webhooks without having to write your own middleware to format the request body. Below are the currently supported providers:

- Discord
- Slack

### Setting Up a Webhook for Discord

Discord supports integrating directly with webhooks. To enable this on a server you will need to be an admin or otherwise have the appropriate permissions.

1. On Discord, open the settings for a server text channel. This menu can be accessed via the cogwheel/gear icon where the channel is listed on the server.
2. Click on the integrations tab.
3. Click on the webhooks option.
4. You will see an option to create a new webhook, click this button and fill out your preferred bot name and channel.
5. Once created, you will have the option to copy the new webhook URL. Copy that URL.
6. Back in Railway, open the project you wish to integrate with.
7. Click on the project's deployments menu.
8. Navigate to the settings tab.
9. Input the copied webhook URL into the input under "Build and Deploy Webhooks".
10. Click the checkmark to the right of the input to save.

At this point, the Discord Muxer will identify the URL and change the payload to accommodate the Discord integration. You can see this if you expand the payload preview panel.

You are now done! When your project deploys again, that Discord channel will get updates on the deployment!

### Setting Up a Webhook for Slack

Slack supports integrating directly with webhooks.

1. Enable incoming webhooks for your Slack instance (Tutorial <a href="https://api.slack.com/messaging/webhooks#enable_webhooks" target="_blank">here</a>)
1. Generate a hooks.slack.com webhook URL for your channel (Tutorial <a href="https://api.slack.com/messaging/webhooks#create_a_webhook" target="_blank">here</a>)
1. Open up Railway, navigate to your project's Webhook tab.
1. Paste the url from slack

<Image
src="https://res.cloudinary.com/railway/image/upload/v1737947755/docs/webhooks/wo4tuyv9dy7gjgiq2j7j.png"
alt="Slack Webhook"
layout="responsive"
width={1466} height={810} quality={80} />

## Code Examples

{
  "type": "DEPLOY",
  "timestamp": "2025-02-01T00:00:00.000Z",
  "project": {
    "id": "[project ID]",
    "name": "[project name]",
    "description": "...",
    "createdAt": "2025-02-01T00:00:00.000Z"
  },
  "environment": {
    "id": "[environment ID]",
    "name": "[environment name]"
  },
  "deployment": {
    "id": "[deploy ID]",
    "creator": {
      "id": "[user id]",
      "name": "...",
      "avatar": "..."
    },
    "meta": {}
  }
}


# Create
Source: https://docs.railway.com/guides/create

Learn how to create reusable templates on Railway to enable effortless one-click deploys.

By defining services, environment configuration, network settings, etc., you lay the foundation for others to deploy the same software stack with the click of a button.

If you publish your template to the <a href="https://railway.com/templates" target="_blank">marketplace</a>, you can even <a href="https://railway.com/open-source-kickback" target="_blank">collect a kickback</a> from the usage of it!

## How to Create a Template

You can either create a template from scratch or base it off of an existing project.

### Starting from Scratch

To create a template from scratch, head over to your <a href="https://railway.com/workspace/templates" target="_blank">Templates</a> page within your workspace settings and click on the New Template button.

- Add a service by clicking the Add New button in the top right-hand corner, or through the command palette (CMD + K -> + New Service)
- Select the service source (GitHub repo or Docker Image)
- Configure the service variables and settings

  <Image src="https://res.cloudinary.com/railway/image/upload/v1715724184/docs/templates-v2/composer_aix1x8.gif"
  alt="Template Editor"
  layout="intrinsic"
  width={900} height={1120} quality={80} />

- Once you've added your services, click Create Template
- You will be taken to your templates page where you can copy the template URL to share with others

Note that your template will not be available on the template marketplace, nor will be eligible for a kickback, until you publish it.

### Private Repo Support

It's now possible to specify a private GitHub repo when creating a template.

This feature is intended for use among Teams and Organizations. Users supporting a subscriber base may also find this feature helpful to distribute closed-source code.

To deploy a template that includes a private repo, look for the GitHub panel in the Account Integrations section of General Settings. Then select the Edit Scope option to grant Railway access to the desired private repos.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1721350229/docs/github-private-repo_m46wxu.png"
alt="Create a template from a private GitHub repositories"
layout="intrinsic"
width={1599}
height={899}
quality={80}
/>

If you do not see the Edit Scope option, you may still need to connect GitHub to your Railway account.

### Convert a Project Into a Template

You can also convert an existing project into a ready-made Template for other users.

- From your project page, click Settings in the right-hand corner of the canvas
- Scroll down until you see **Generate Template from Project**
- Click Create Template

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743198969/docs/create-template_ml13wy.png"
alt="Generate template from project"
layout="intrinsic"
width={1200}
height={380}
quality={80}
/>

- You will be taken to the template composer page, where you should confirm the settings and finalize the template creation

## Configuring Services

Configuring services using the template composer is very similar to building a live project in the canvas.

Once you add a new service and select the source, you can configure the following to enable successful deploys for template users:

- **Variables tab**
  - Add required Variables.
    _Use reference variables where possible for a better quality template_
- **Settings tab**
  - Add a Root Directory (Helpful for monorepos)
  - Enable Public Networking with TCP Proxy or HTTP
  - Set a custom Start command
  - Add a Healthcheck Path
- **Add a volume**
  - To add a volume to a service, right-click on the service, select Attach Volume, and specify the Volume mount path

### Specifying a Branch

To specify a particular GitHub branch to deploy, simply enter the full URL to the desired branch in the Source Repo configuration. For example -

- This will deploy the main branch: https://github.com/railwayapp-templates/postgres-ssl
- This will deploy the new branch: https://github.com/railwayapp-templates/postgres-ssl/tree/new

### Template Variable Functions

Template variable functions allow you to dynamically generate variables (or parts of a variable) on demand when the template is deployed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743198983/docs/template-variables_dp5pg5.png"
alt="Template Variable Functions"
layout="intrinsic"
width={1200} height={428} quality={100} />

When a template is deployed, all template variable functions are executed and the result replaces the ${{ ... }} in the variable.

Use template variables to generate a random password for a database, or to generate a random string for a secret.

The current template variable functions are:

1. secret(length?: number, alphabet?: string): Generates a random secret (32 chars by default).

   **Tip:** You can generate Hex or Base64 secrets by constructing the appropriate alphabet and length.

   - openssl rand -base64 16 â†’ ${{secret(22, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}==
   - openssl rand -base64 32 â†’ ${{secret(43, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}=
   - openssl rand -base64 64 â†’ ${{secret(86, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/")}}==
   - openssl rand -hex 16 â†’ ${{secret(32, "abcdef0123456789")}}
   - openssl rand -hex 32 â†’ ${{secret(64, "abcdef0123456789")}}
   - openssl rand -hex 64 â†’ ${{secret(128, "abcdef0123456789")}}

   Or even generate a UUIDv4 string -

   ${{secret(8, "0123456789abcdef")}}-${{secret(4, "0123456789abcdef")}}-4${{secret(3, "0123456789abcdef")}}-${{secret(1, "89ab")}}${{secret(3, "0123456789abcdef")}}-${{secret(12, "0123456789abcdef")}}

2. randomInt(min?: number, max?: number): Generates a random integer between min and max (defaults to 0 and 100)

## Managing Your Templates

You can see all of your templates on your <a href="https://railway.com/workspace/templates" target="_blank">Workspace's Template page</a>. Templates are separated into Personal and Published templates.

You can edit, publish/unpublish and delete templates.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743199089/docs/templates_xyphou.png"
 alt="Account templates page"
 layout="intrinsic"
 width={1200}
 height={668}
 quality={80}
/>


# Best Practices
Source: https://docs.railway.com/guides/templates-best-practices

Learn the best practices for template creation.



## Checklist

Depending on the type of template, there are different things to consider:

- Template and Service Icons
- Naming Conventions
- Private Networking
- Environment Variables
- Health Checks
- Persistent Storage
- Authentication
- Dry Code
- Workspace Naming
- Overview

## Template and Service Icons

Template and service icons are important for branding and recognition, as they give the template a more professional look and feel.

Always use 1:1 aspect ratio icons or logos with transparent backgrounds for both the template itself and the services the template includes.

Transparent backgrounds ensure logos integrate seamlessly with Railway's interface and provide a more polished, professional appearance.

## Naming Conventions

Naming conventions are important for readability and consistency; using proper names enhances the overall quality and credibility of your template.

Always follow the naming conventions for the software that the template is made for.

Example, if the template is for ClickHouse, the service and template name should be named ClickHouse with a capital C and H, since that is how the brand name is spelled.

For anything else, such as custom software:

- Use capital case.
- Avoid using special characters or dashes, space-delimited is the way to go.
- Prefer shorter names over longer names for better readability.
- Keep names concise while maintaining clarity.

## Private Networking

Private networking provides faster, free communication between services and reduces costs compared to routing traffic through the public internet.

Always configure service-to-service communication (such as backend to database connections) to use private network hostnames rather than public domains.

For more details, see the private networking guide and reference documentation.

## Environment Variables

Properly set up environment variables are a great way to increase the usability of your template.

When using environment variables:

- Always include a description of what the variable is for.

- If a variable is optional, include a description explaining its purpose and what to set it to or where to find its value.

- For any secrets, passwords, keys, etc., use template variable functions to generate them, avoid hardcoding default credentials at all costs.

- Use reference variables when possible for dynamic service configuration.

- When referencing a hostname, use the private network hostname rather than the public domain, e.g., RAILWAY_PRIVATE_DOMAIN rather than RAILWAY_PUBLIC_DOMAIN.

- Include helpful pre-built variables that the user may need, such as database connection strings, API keys, hostnames, ports, and so on.

## Health Checks

Health checks are important for ensuring that the service is running properly, before traffic is routed to it.

Although a health check might not be needed for all software, such as Discord bots, when it is applicable, it is a good idea to include a health check.

A readiness endpoint is the best option; if that's not possible, then a liveness endpoint should be used.

For more details, see the healthchecks guide and reference documentation.

## Persistent Storage

Persistent storage is essential for templates that include databases, file servers, or other stateful services that need to retain data across deployments.

Always include a volume for these services.

Without persistent storage, data will be lost between redeployments, leading to unrecoverable data loss for template users.

When configuring the service, ensure the volume is mounted to the correct path. An incorrect mount path will prevent data from being stored in the volume.

Some examples of software that require persistent storage:

- **Databases:** PostgreSQL, MySQL, MongoDB, etc.
- **File servers:** Nextcloud, ownCloud, etc.
- **Other services:** Redis, RabbitMQ, etc.

The volume mount location depends entirely on where the software expects it to be mounted. Refer to the software's documentation for the correct mount path.

For more details, see the volumes guide and reference documentation.

## Authentication

Authentication is a common feature for many software applications, and it is crucial to properly configure it to prevent unauthorized access.

If the software provides a way to configure authentication, such as a username and password, or an API key, you should always configure it in the template.

For example, ClickHouse can operate without authentication, but authentication should always be configured so as not to leave the database open and unauthenticated to the public.

Passwords, API keys, etc. should be generated using template variable functions, and not hardcoded.

## Dry Code

This is most applicable to templates that deploy from GitHub.

When creating templates that deploy from GitHub, include only the essential files needed for deployment. Avoid unnecessary documentation, example files, or unused code and configurations that don't contribute to the core functionality.

A clean, minimal repository helps users quickly understand the template's structure and make customizations when needed.

## Workspace Naming

When users deploy a template, the template author appears as the name of the <a href="/reference/teams" target="_blank">workspace</a> that created and published it.

Since the author is publicly visible and shown with the template to the users, it is important to make sure the workspace name is professional and **accurately represents your relationship to the software**.

**Important:** Only use a company or organization name as your workspace name if you are officially authorized to represent that entity. Misrepresenting your affiliation is misleading to users and violates trust.

**If you are officially affiliated** with the software (e.g., you work for ClickHouse and are creating a ClickHouse template), then using the official company name "ClickHouse, Inc." is appropriate and helpful for users to identify official templates.

**If you are not officially affiliated** with the software, always use your own professional name as the workspace name.

**Note:** To transfer a template from one workspace to another, <a href="https://station.railway.com/" target="_blank">contact support</a>.

## Overview

The overview is the first thing users will see when they click on the template, so it is important to make it count.

The overview should include the following:

- **H1: Deploy and Host [X] with Railway**

  What is X? Your description in roughly ~ 50 words.

- **H2: About Hosting [X]**

  Roughly 100 word description what's involved in hosting/deploying X

- **H2: Common Use Cases**

  In 3-5 bullets, what are the most common use cases for [X]?

- **H2: Dependencies for [X] Hosting**

  In bullet form, what other technologies are incorporated in using this template besides [X]?

- **H3: Deployment Dependencies**

  Include any external links relevant to the template.

- **H3: Implementation Details (Optional)**

  Include any code snippets or implementation details. This section is optional. Exclude if nothing to add.

- **H3: Why Deploy [X] on Railway?**

  Railway is a singular platform to deploy your infrastructure stack. Railway will host your infrastructure so you don't have to deal with configuration, while allowing you to vertically and horizontally scale it.

  By deploying [X] on Railway, you are one step closer to supporting a complete full-stack application with minimal burden. Host your servers, databases, AI agents, and more on Railway.


# Publish and Share
Source: https://docs.railway.com/guides/publish-and-share

Learn how to publish and share your Railway templates.



## Publishing a Template

After you create your template, simply click the publish button and fill out the form to publish your template.

<Image src="https://res.cloudinary.com/railway/image/upload/v1753243835/docs/reference/templates/mockup-1753242978376_skjt7w.png"
  alt="Template publishing form"
  layout="intrinsic"
  width={2004}
  height={3834}
  quality={80}
/>

You can always publish your template by going to the <a href="https://railway.com/workspace/templates" target="_blank">Templates page in your Workspace settings</a> and choose Publish next to the template you'd like to publish.

Optionally, you can add a demo project to your template. This will be used to showcase your template in a working project, and can be accessed by clicking on the Live Demo button in the template's overview page.

## Sharing your Templates

After you create your template, you may want to share your work with the public and let others clone your project. You are provided with the Template URL where your template can be found and deployed.

### Deploy on Railway Button

To complement your template, we also provide a Deploy on Railway button which you can include in your README or embed it into a website.

<Image src="https://res.cloudinary.com/railway/image/upload/v1676438967/docs/deploy-on-railway-readme_iwcjjw.png" width={714} height={467} alt="Example README with Deploy on Railway button" />

!https://railway.com/button.svg
The button is located at https://railway.com/button.svg.

#### Markdown

To render the button in Markdown, copy the following code and replace the template code with your desired template. If you'd like to help us attribute traffic to your template, replace utm_campaign=generic in the URL with your template name.

#### HTML

To render the button in HTML, copy the following code and replace the template code with your desired template. If you'd like to help us attribute traffic to your template, replace utm_campaign=generic in the URL with your template name.

### Examples

Here are some example templates from the <a href="https://railway.com/templates" target="_blank">template marketplace</a> in button form:
|Icon|Template|Button|
|:--:|:------:|:----:|
|<img src="https://devicons.railway.com/i/nodejs.svg" alt="Node" width="25" height="25" />|Node|![Deploy on Railway](https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=node)|
|<img src="https://devicons.railway.com/i/deno.svg" alt="Deno" width="25" height="25" />|Deno|![Deploy on Railway](https://railway.com/new/template/LsaSsU?utm_medium=integration&utm_source=button&utm_campaign=deno)|
|<img src="https://devicons.railway.com/i/bun.svg" alt="Bun" width="25" height="25" />|Bun|![Deploy on Railway](https://railway.com/new/template/gxxk5g?utm_medium=integration&utm_source=button&utm_campaign=bun)|
|<img src="https://devicons.railway.com/i/go.svg" alt="Gin" width="25" height="25" />|Gin|![Deploy on Railway](https://railway.com/new/template/dTvvSf?utm_medium=integration&utm_source=button&utm_campaign=gin)|
|<img src="https://devicons.railway.com/i/flask-dark.svg" alt="Flask" width="25" height="25" />|Flask|![Deploy on Railway](https://railway.com/new/template/zUcpux?utm_medium=integration&utm_source=button&utm_campaign=flask)|

## Kickback Program

If your published template is deployed into other users' projects, you are immediately eligible for a 50% kickback, in the form of Railway credits or cash. Refer to the template reference page for more information.

## Template Verification

Templates are verified when the creator and maintainer of the technology becomes a partner and reviews the template.

If you are or have a relationship with the creator, please reach out to us by submitting the form on our partners page.

## Code Examples

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=generic)

<a
  href="https://railway.com/new/template/ZweBXA?utm_medium=integration&utm_source=button&utm_campaign=generic"
  ><img src="https://railway.com/button.svg" alt="Deploy on Railway"
/></a>


# Deploy
Source: https://docs.railway.com/guides/deploy

Learn how to deploy Railway templates.

connected to infrastructure.

You can find featured templates on our <a href="https://railway.com/templates" target="_blank">template marketplace</a>.

## Template Deployment Flow

To deploy a template -

- Find a template from the marketplace and click Deploy Now
- If necessary, configure the required variables, and click Deploy
- Upon deploy, you will be taken to your new project containing the template service(s)
  - Services are deployed directly from the defined source in the template configuration
  - After deploy, you can find the service source by going to the service's settings tab
  - Should you need to make changes to the source code, you will need to eject from the template repo to create your own copy. See next section for more detail.

_Note: You can also deploy templates into existing projects, by clicking + New from your project canvas and selecting Template._

## Eject from Template Repository

<Banner variant="info">
As of March 2024, the default behavior for deploying templates, is to attach to and deploy directly from the template repository.  Therefore, you will not automatically get a copy of the repository on deploy.  Follow the steps below to create a repository for yourself.
</Banner>

By default, services deployed from a template are attached to and deployed directly from the template repository. In some cases, you may want to have your own copy of the template repository.

Follow these steps to eject from the template repository and create a mirror in your own GitHub account.

1. In the service settings, under Source, find the **Upstream Repo** setting
2. Click the Eject button
3. Select the appropriate GitHub organization to create the new repository
4. Click Eject service

## Updatable Templates

When you deploy any services from a template based on a GitHub repo, every time you visit the project in Railway, we will check to see if the project it is based on has been updated by its creator.

If it has received an upstream update, we will create a branch on the GitHub repo that was created when deploying the template, allowing for you to test it out within a PR deploy.

If you are happy with the changes, you can merge the pull request, and we will automatically deploy it to your production environment.

If you're curious, you can read more about how we built updatable templates in this <a href="https://blog.railway.com/p/updatable-starters" target="_blank">blog post</a>

_Note: This feature only works for services based on GitHub repositories. At this time, we do not have a mechanism to check for updates to Docker images from which services may be sourced._


# Manage Projects
Source: https://docs.railway.com/guides/manage-projects

Learn how to manage projects via the public GraphQL API.

### Fetch All Your Projects

The query below will fetch all your personal projects along with all the services and environments for them.

### Delete a Project

<Banner variant="danger">This is a destructive action</Banner>

The mutation below will delete the project with the specified id.

## Code Examples

query me {
  me {
    projects {
      edges {
        node {
          id
          name
          services {
            edges {
              node {
                id
                name
              }
            }
          }
          environments {
            edges {
              node {
                id
                name
              }
            }
          }
        }
      }
    }
  }
}

mutation projectDelete {
  projectDelete(id: "5e594338-0faa-415f-b2a7-2b5f2d4ec11a")
}


# Manage Services
Source: https://docs.railway.com/guides/manage-services

Learn how to create services via the public GraphQL API.

### Create a New Service With a GitHub Repo

The mutation below will create a new service with the specified GitHub repo attached. The response will contain the newly created service.

<Banner variant="info">You can also use image inside the source to attach a Docker image to the service.</Banner>

## Code Examples

mutation serviceCreate {
  serviceCreate(
    input: {
      projectId: "8df3b1d6-2317-4400-b267-56c4a42eed06"
      source: { repo: "railwayapp-templates/django" }
    }
  ) {
    id
  }
}


# Manage Deployments
Source: https://docs.railway.com/guides/manage-deployments

Learn how to manage deployments via the public GraphQL API.

### Fetch Latest Active Deployment

The query below will fetch the latest active deployment for a service for a specific environment.

### Restarting a Deployment

The query below will restart the deployment with the specified id.

## Code Examples

query deployments {
  deployments(
    first: 1
    input: {
      projectId: "8df3b1d6-2317-4400-b267-56c4a42eed06"
      environmentId: "9fb4baf0-809a-40ec-af32-751f50890802"
      serviceId: "4bd252dc-c4ac-4c2e-a52f-051804292035"
    }
  ) {
    edges {
      node {
        id
        staticUrl
      }
    }
  }
}

mutation deploymentRestart {
  deploymentRestart(id: "9d5b1306-e22e-4357-9b3f-cc3b97ed8240")
}


# Manage Variables
Source: https://docs.railway.com/guides/manage-variables

Learn how to manage variables via the public GraphQL API.

### Fetch Variables For a Service

The query below will fetch all the variables for a service for a specific environment. The response will contain all the variables in a key/value object.

<Banner variant="info">You can omit the serviceId from this query to fetch the shared variables for the environment.</Banner>

### Upsert Variable For a Service

The mutation below will upsert a new variable for the specified service within the specified environment. You can use this to both create and update variables.

<Banner variant="info">You can omit the serviceId from this mutation to create a shared variable.</Banner>

## Code Examples

query variables {
  variables(
    projectId: "8df3b1d6-2317-4400-b267-56c4a42eed06"
    environmentId: "9fb4baf0-809a-40ec-af32-751f50890802"
    serviceId: "4bd252dc-c4ac-4c2e-a52f-051804292035"
  )
}

mutation variableUpsert {
  variableUpsert(
    input: {
      projectId: "8df3b1d6-2317-4400-b267-56c4a42eed06"
      environmentId: "9fb4baf0-809a-40ec-af32-751f50890802"
      serviceId: "4bd252dc-c4ac-4c2e-a52f-051804292035"
      name: "NEW_VARIABLE"
      value: "SECRET_VALUE"
    }
  )
}


# Config as Code
Source: https://docs.railway.com/guides/config-as-code

Learn how to manage and deploy apps on Railway using config as code with toml and json files.

alongside your code in a railway.toml or railway.json file.

Everything in the build and deploy sections of the service settings page can be specified in this configuration file.

The settings in the dashboard will not be updated with the settings defined in
code. Configuration defined in code will always override values from the
dashboard.

## Toml vs Json

The format you use for your config-as-code (toml or json) file is entirely dependent on preference, and the resulting behavior in Railway is the same no matter which you choose.

For example, these configuration definitions are equivalent:

<div style={{ display: 'flex', flexDirection: 'row', gap: '5px', fontSize: '0.9em', alignItems: 'stretch' }}>
    <div style={{ flex: '1 1 50%', overflow: 'auto', minWidth: '200px', maxWidth: '350px' }}>
        
        <p style={{ marginTop: '-0.2em', fontSize: '0.8em', opacity: '0.6' }}>A railway.toml file</p>
    </div>
    <div style={{ flex: '1 1 50%', overflow: 'auto', minWidth: '200px', maxWidth: '350px' }}>
        
        <p style={{ marginTop: '-0.2em', fontSize: '0.8em', opacity: '0.6' }}>A railway.json file</p>
    </div>

</div>

## JSON Schema

You can find an always up-to-date JSON schema at railway.com/railway.schema.json.

If you include it in your railway.json file, many editors (e.g. VSCode) will provide autocomplete and documentation.

## Understanding Config Source

On a service's deployment details page, all the settings that a deployment went out with are shown.

For settings that come from a configuration file, there is a file icon. Hovering over the icon will show exactly what part of the file the values originated from.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743195106/docs/configuration_emrjth.png"
alt="Screenshot of Deployment Details Pane"
layout="responsive"
width={1200} height={631} quality={100} />

## Using a Custom Config as Code File

You can use a custom config file by setting it on the service settings page. The file is relative to your app source.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743195631/docs/config-file_f1wf32.png"
alt="Screenshot of Rollback Menu"
layout="responsive"
width={1200} height={374} quality={100} />

## Configurable Settings

Find a list of all of the configurable settings in the config as code reference page.

## Code Examples

[build]
        builder = "nixpacks"
        buildCommand = "echo building!"

        [deploy]
        preDeployCommand = ["npm run db:migrate"]
        startCommand = "echo starting!"
        healthcheckPath = "/"
        healthcheckTimeout = 100
        restartPolicyType = "never"





        --

{
          "$schema": "https://railway.com/railway.schema.json",
          "build": {
            "builder": "NIXPACKS",
            "buildCommand": "echo building!"
            },
          "deploy": {
            "preDeployCommand": ["npm run db:migrate"],
            "startCommand": "echo starting!",
            "healthcheckPath": "/",
            "healthcheckTimeout": 100,
            "restartPolicyType": "never"
            }
        }

{
  "$schema": "https://railway.com/railway.schema.json"
}


# Node.js SIGTERM
Source: https://docs.railway.com/guides/nodejs-sigterm

SIGTERM might sometimes fail to process on shutdown. Here's why.

When you start your app with NPM, Yarn, or PNPM, the package manager becomes the main process, not your app.
Because the signal has been intercepted, the service will eventually be force quit which is displayed as a sudden "crash".

The fix is simple: start Node directly.

Head to your service's Settings tab. From there scroll to the "Deploy" section and change "Custom Start Command".

Instead of this:


Use this:


With this change, your app will receive SIGTERM directly and can handle shutdown cleanly.

## Code Examples

npm run start

node index.js



# Tutorials
Source: https://docs.railway.com/tutorials

# Getting Started
Source: https://docs.railway.com/tutorials/getting-started

Discover tutorials to help you get the most out of Railway."

Explore the pages in this section to learn or get inspired!

Also checkout our Quick Start Tutorial to deploy an app in minutes.

### Contributing

Pull requests are welcome. If you make a quality tutorial for other Railway users, we would really love to include it!

If there is a tutorial you hope to see, please create a post in <a href="https://station.railway.com/" target="_blank">Forums</a>!


# Set Up a Datadog Agent
Source: https://docs.railway.com/tutorials/set-up-a-datadog-agent

Learn how to set up a Datadog agent in Railway.

While Railway has a native, centralized logging mechanism, you may have a need to ship this data to another location, to view it alongside data collected from systems outside of Railway.

**Objectives**

In this tutorial you will learn how to -

- Deploy a Datadog agent in Railway - listening for metrics, logs, and traces.
- Configure an application to send metrics, logs, and traces to the agent.

If you are looking for a quicker way to get started, you can also deploy this project from a <a href="https://railway.com/template/saGmYG" target="_blank">template</a>.

**Prerequisites**

To be successful, you should already have -

- Railway CLI installed
- Datadog API key and site value

**Caveats**

Keep in mind that the Datadog agent sends data to Datadog over the Internet, meaning you will see an increase in egress cost. If this is a concern, you may be interested in exploring self-hosted solutions, and we encourage you to check out the OpenTelemetry Tutorial.

## 1. Create the Project Structure

First we'll create the project structure.

From your local machine -

- Create a folder for your project called railway-project.
- Create two folders inside of railway-project called agent and expressapi.

You project structure should look like this

## 2. Set Up the Datadog Agent

Now we'll add files to the agent folder, which will build the Datadog Agent image.

- Inside of the agent folder, create three files -
  - Dockerfile
  - syslog.yaml
  - datadog.yaml

#### Define the Dockerfile

Let's define the Dockerfile.

- Within your Dockerfile, add the following contents.

#### Define the syslog.yaml file

The syslog.yaml file is used to instruct the agent to listen for syslogs to be forwarded on the configured port.

- Within the syslog.yaml file, add the following contents -

#### Define the datadog.yaml file

The datadog.yaml file is used to instruct the agent to send logs to Datadog over http instead of the default tcp.

- Within the datadog.yaml file, add the following contents -

## 3. Set Up the Node Express App

Now let's build a Node Express App that will send logs and metrics to the Datadog Agent over the Private Network.

- Create an app.js file inside of the expressapi folder you created in Step 1.
- Use npm (or your preferred package manager) to install the required dependencies -

#### Define the app.js file

The app.js file defines your express server. This is where we will import the DataDog tracer and initialize the StatsD client and the Winston logger, which will send traces, metrics, and logs, respectively, to the Datadog agent.

- Within the app.js file, add the following contents -

#### Winston and hot-shots

In this example app, we are using Winston as the logger and hot-shots as the StatsD client.

- Winston is configured using winston-syslog to transport **logs** to the Datadog agent via Syslog over udp6.
- hot-shots is configured to send **metrics** to the Datadog agent over udp6.

## 4. Set Up the Railway Project

Now let's create the project using the CLI, then create the services and variables from within the project in Railway.

You will need your **Datadog API key** and **Site** value in this step.

If you have not already done so, please install the CLI and authenticate.

#### Create a Project

- In your terminal, run the following command to create a new project -

- Name your project datadog-project when prompted (you can change this later).

- Open your project in Railway by running the following -

#### Create the Services

- In Railway, create an Empty Service by clicking + New button in the top right-hand corner and choosing Empty Service in the prompt.
- Right click on the service that is created, select Update Info and name it datadog-agent.
- Repeat the above steps to create a second service, but name the second service expressapi.

#### Add the Variables

Each service requires unique variables listed below. For each service, follow the steps to add the variables required for the service.

datadog-agent Variables -

expressapi Variables -

- Click on the service card
- Click on the Variables tab
- Click on Raw Editor
- Paste the required variables (be sure to update the Datadog API key and site with your own values)
- Click Update Variables and Deploy

## 5. Deploy to Railway

Now we're ready to deploy our services. We will use the CLI to push code from our local machine to Railway.

#### Railway Up

Follow these steps for each service -

- In your local terminal, change directory into the agent folder.
- Link to datadog-project by running the following command -
  
- Follow the prompts, selecting the datadog-project and production environment.
- Link to the datadog-agent service by running the following command -
  
- Follow the prompt, selecting the datadog-agent service.
- Deploy the agent by running the following command -
  
- Change directory into your expressapi folder and repeat the steps above, but for the expressapi service.

#### Create a Domain for the Express App

The express app will send logs and metrics to the Datadog agent upon navigation to either of its two routes. So let's give it a domain -

- Ensure that you are linked to the datadog-project and expressapi service (refer to the steps above)
- Assign the expressapi a domain by running the following command -
  

## 6. Test and Confirm

Test that your Datadog Agent is receiving and forwarding data to Datadog by navigating to the routes in the Express app -

- /
- /test

Generate some traffic to these two routes and verify in your Datadog instance that the data is there.

_Note: it can take a few minutes to see the data in Datadog, check the Datadog Agent's logs in Railway_

## Bonus - Add a Python service

Once you have your agent setup and working with a node app. It's easy to add more services and configure the agent to accept data from them. In this bonus section, we'll quickly cover a Python implementation.

In the following example, we are using the <a href="https://fastapi.tiangolo.com/" target="_blank">FastAPI Python framework</a>.

**In the main.py file we have configured both metrics and logs to be sent over StatsD and SysLog respectively -**

```python
import logging.handlers
from fastapi import FastAPI
from datadog import initialize, statsd, DogStatsd
import logging
import random
import os
import json_log_formatter

## Configuration for sending logs

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.handlers.SysLogHandler(address=(os.getenv("DD_AGENT"), os.getenv("DD_AGENT_SYSLOG_PORT")))
json_handler.setFormatter(formatter)

logger = logging.getLogger('python-app')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


# Configuration for sending metrics
config = {
    "api_key": os.getenv("DD_API_KEY"),
    "statsd_host": os.getenv("DD_AGENT_HOST"),
    "statsd_port": os.getenv("DD_AGENT_STATSD_PORT"),
    "statsd_constant_tags": ["env:prod"],
}

initialize(**config)

app = FastAPI()

# Use DogStatsd client for more custom metrics
dog_statsd = DogStatsd()

@app.get("/")
async def root():
    # Increment a simple counter
    statsd.increment('example_app.page.views')

    # Record a random gauge value
    gauge_value = random.uniform(1, 100)
    statsd.gauge('example_app.random_value', gauge_value)

    # Log a message
    logger.info(f"Page viewed, gauge value: {gauge_value}")

    # Custom metric using DogStatsd
    dog_statsd.histogram('example_app.response_time', random.uniform(50, 300))

    return {"message": "Hello World"}

# Additional route for testing
@app.get("/test")
async def test():
    # Custom metrics and logging
    statsd.increment('example_app.test.endpoint.hits')
    test_value = random.randint(1, 10)
    dog_statsd.gauge('example_app.test.value', test_value)
    logger.info(f"Test endpoint hit, value: {test_value}")

    return {"test_value": test_value}

plaintext
logs:
  - type: udp
    port: 514
    service: "node-app"
    source: syslog
  - type: udp
    port: 515
    service: "python-app"
    source: syslog
```

## Conclusion

Congratulations! You have deployed a Datadog Agent and a Node Express app (and maybe a Python service) that sends logs and metrics to Datadog.

This is a _very_ basic implementation, and you should refer to the <a href="https://docs.datadoghq.com/" target="_blank">Datadog documentation</a> for information on how to customize the data you send.

## Code Examples

railway-project/
â”œâ”€â”€ agent/
â””â”€â”€ expressapi/

FROM datadog/agent:7

  # Set environment variables
  ENV DD_LOGS_ENABLED=true
  ENV DD_APM_ENABLED=true
  ENV DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL=true
  ENV DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true
  ENV DD_APM_NON_LOCAL_TRAFFIC=true
  ENV DD_BIND_HOST=::1

  # Reference Variables defined in Railway
  ARG DD_API_KEY
  ARG DD_HOSTNAME
  ARG DD_SITE

  # Copy datadog.yaml into the container
  COPY datadog.yaml /etc/datadog-agent/datadog.yaml

  # Copy syslog configuration file
  COPY syslog.yaml /etc/datadog-agent/conf.d/syslog.d/

  # DogStatsD port, APM port, and the syslog port
  EXPOSE 8125/udp
  EXPOSE 8126
  EXPOSE 514/udp

logs:
    - type: udp
      port: 514
      service: "node-app"
      source: syslog

logs_config:
    force_use_http: true

npm i express winston winston-syslog dd-trace

// ** it is important to import the tracer before anything else **
  const tracer = require("dd-trace").init();

  const express = require("express");
  const app = express();

  const StatsD = require("hot-shots");
  const { createLogger, format, transports } = require("winston");
  require("winston-syslog").Syslog;
  const port = process.env.PORT || 3000;

  // Configure the StatsD client
  const statsdClient = new StatsD({
    host: process.env.DD_AGENT_HOST,
    port: process.env.DD_AGENT_STATSD_PORT,
    protocol: "udp",
    cacheDns: true,
    udpSocketOptions: {
      type: "udp6",
      reuseAddr: true,
      ipv6Only: true,
    },
  });

  // Configure Winston logger
  const logger = createLogger({
    level: "info",
    exitOnError: false,
    format: format.json(),
    transports: [
      new transports.Syslog({
        host: process.env.DD_AGENT_HOST,
        port: process.env.DD_AGENT_SYSLOG_PORT,
        protocol: "udp6",
        format: format.json(),
        app_name: "node-app",
      }),
    ],
  });

  app.get("/", (req, res) => {
    // Increment a counter for the root path
    statsdClient.increment("data_dog_example.homepage.hits");
    statsdClient.gauge("data_dog_example.homepage.hits", 124);

    // forward logs from root path
    logger.info("Root route was accessed");

    res.send("Hello World!");
  });

  app.get("/test", (req, res) => {
    // Increment a counter for the test path
    statsdClient.increment("data_dog_example.testpage.hits");

    // forward logs from test path
    logger.info("Test route was accessed");

    res.send("This is the test endpoint!");
  });

  app.listen(port, () => {
    console.log(`Example app listening at port ${port}`);
  });

railway init

railway open

DD_API_KEY=<YOUR_API_KEY>
DD_HOSTNAME=${{RAILWAY_PRIVATE_DOMAIN}}
DD_SITE=<YOUR_DATADOG_SITE>

DD_AGENT_HOST=${{datadog-agent.DD_HOSTNAME}}
DD_AGENT_STATSD_PORT=8125
DD_AGENT_SYSLOG_PORT=514
DD_TRACE_AGENT_PORT=8126

railway link

railway service

railway up -d

railway domain

import logging.handlers
from fastapi import FastAPI
from datadog import initialize, statsd, DogStatsd
import logging
import random
import os
import json_log_formatter

## Configuration for sending logs
formatter = json_log_formatter.JSONFormatter()

json_handler = logging.handlers.SysLogHandler(address=(os.getenv("DD_AGENT"), os.getenv("DD_AGENT_SYSLOG_PORT")))
json_handler.setFormatter(formatter)

logger = logging.getLogger('python-app')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


# Configuration for sending metrics
config = {
    "api_key": os.getenv("DD_API_KEY"),
    "statsd_host": os.getenv("DD_AGENT_HOST"),
    "statsd_port": os.getenv("DD_AGENT_STATSD_PORT"),
    "statsd_constant_tags": ["env:prod"],
}

initialize(**config)

app = FastAPI()

# Use DogStatsd client for more custom metrics
dog_statsd = DogStatsd()

@app.get("/")
async def root():
    # Increment a simple counter
    statsd.increment('example_app.page.views')

    # Record a random gauge value
    gauge_value = random.uniform(1, 100)
    statsd.gauge('example_app.random_value', gauge_value)

    # Log a message
    logger.info(f"Page viewed, gauge value: {gauge_value}")

    # Custom metric using DogStatsd
    dog_statsd.histogram('example_app.response_time', random.uniform(50, 300))

    return {"message": "Hello World"}

# Additional route for testing
@app.get("/test")
async def test():
    # Custom metrics and logging
    statsd.increment('example_app.test.endpoint.hits')
    test_value = random.randint(1, 10)
    dog_statsd.gauge('example_app.test.value', test_value)
    logger.info(f"Test endpoint hit, value: {test_value}")

    return {"test_value": test_value}

logs:
  - type: udp
    port: 514
    service: "node-app"
    source: syslog
  - type: udp
    port: 515
    service: "python-app"
    source: syslog


# Deploy an Otel Collector Stack
Source: https://docs.railway.com/tutorials/deploy-an-otel-collector-stack

Monitor and trace your applications by deploying an OpenTelemetry Collector and backend on Railway.

> OpenTelemetry is an Observability framework and toolkit designed to create and manage telemetry data such as traces, metrics, and logs. Crucially, OpenTelemetry is vendor- and tool-agnostic, meaning that it can be used with a broad variety of Observability backends, including open source tools like Jaeger and Prometheus, as well as commercial offerings.

## About this Tutorial

There is an overwhelming number of options for applying OpenTelemetry in your software stack. This tutorial uses the libraries and tools endorsed and/or maintained by the OpenTelemetry community.

OpenTelemetry is commonly referred to simply as "Otel". You will see both terms used throughout this tutorial.

**Objectives**

In this tutorial you will learn how to -

- Deploy the <a href="https://opentelemetry.io/docs/collector/" target="_blank">OpenTelemetry Collector</a>, listening for traces, metrics, and logs.
- Deploy a backend stack (Jaeger, Zipkin, and Prometheus) to receive the traces, metrics, and logs from the collector
- Build and instrument an <a href="https://expressjs.com/" target="_blank">Express</a> application to send data to the collector.

**Prerequisites**

To be successful using this tutorial, you should already have -

- Latest version of Railway CLI installed
- A GitHub account

**OpenTelemetry Collector Template and Demo**

If you are looking for a quicker way to get started, you can deploy the collector and backend stack from a template by clicking the button below.
<a href="https://railway.com/template/7KNDff" target="_blank"><img src="https://railway.com/button.svg" alt="Deploy on Railway" /></a>

We also have a live demo of the project you will build in this tutorial <a href="https://classy-writing-production.up.railway.app/" target="_blank">here</a>, and you can access the code repository <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack" target="_blank">here in Github</a>. You can find some example apps, including the one we will build in this tutorial, in the <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack/tree/main/exampleApps" target="_blank">exampleApps folder</a>.

**Let's get started!**

## 1. Deploy the Backend Services

First, we will deploy the backend services:

- <a href="https://www.jaegertracing.io/" target="_blank">Jaeger</a> - an open-source, distributed tracing system that will receive telemetry data from the collector
- <a href="https://zipkin.io/" target="_blank">Zipkin</a> - also an open-source, distributed tracing system that will receive telemetry data from the collector
- <a href="https://prometheus.io/" target="_blank">Prometheus</a> - an open-souce, systems monitoring and alerting toolkit that will receive telemetry data from the collector

_Jaeger and Zipkin offer similar functionality, and it is not necessary to run both. The intent is to give you different examples of backend services._

Each of the following steps should be completed in the same Railway project.

### Add Jaeger Service

- Add a New service by clicking + New
- Select Docker Image as the Source
- Add jaegertracing/all-in-one as the image name and hit Enter
- Add the following variable to the service
  
  _This is the port that serves the UI. Setting this variable allows you to access the Jaeger UI from your browser_
- In the Settings tab, rename the service Jaeger
- Click Deploy to apply and deploy the service
- In the Settings tab, under Networking, click Generate Domain

You should be able to access the Jaeger UI by clicking on the service domain.

### Add Zipkin Service

- Add a New service by clicking + New
- Select Docker Image as the Source
- Add openzipkin/zipkin as the image name and hit Enter
- Add the following variable to the service
  
  _This is the port that serves the UI. Setting this variable allows you to access the Zipkin UI from your browser_
- In the Settings tab, rename the service Zipkin
- Click Deploy to apply and deploy the service
- In the Settings tab, under Networking, click Generate Domain

You should be able to access the Zipkin UI by clicking on the service domain.

### Add Prometheus Service

- Add a New service by clicking + New
- Select Template as the Source
- Type Prometheus and select the Prometheus template (be sure to select this one)
- Click Deploy to apply and deploy the service

_The template deploys with the proper UI port already configured to enable accessing the Prometheus UI from your browser_

You should be able to access the Prometheus UI by clicking on the service domain.

## 2. Deploy the OpenTelemetry Collector

The OpenTelemetry Collector is a vendor-agnostic service that receives, processes, and exports telemetry data.

It is not strictly necessary to run a collector when implementing OpenTelemetry, but it is recommended by the OpenTelemetry community. More information on the subject can be found <a href="https://opentelemetry.io/docs/collector/#when-to-use-a-collector" target="_blank">here</a>.

### Fork the Open Telemetry Collector repository

- Navigate to the <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack" target="_blank">Open Telemetry Collector repository</a> in GitHub
- Click Fork then Create fork

### Add the Open Telemetry Service

In the Railway project -

- Add a New service by clicking + New
- Select GitHub Repo as the Source
- Select the opentelemetry-collector-stack repository (if you renamed the repo in the previous step, yours will be named differently)
- Add the following variable to the service
  
  _This is the port that serves the collector's debugging UI. Setting this variable allows you to access the UI from your browser_
- In the Settings tab, rename the service OpenTelemetry Collector
- Click Deploy to apply and deploy the service
- In the Settings tab, under Networking, click Generate Domain

The Collector's debugging UI is enabled by default and accessible from the browser. This is controlled by the inclusion of the <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack/blob/main/otel-collector-config.yaml#L31" target="_blank">zpages extension in the collector's configuration yaml</a>. You can read more about the UI and the available routes, in the collector's <a href="https://github.com/open-telemetry/opentelemetry-collector/blob/main/extension/zpagesextension/README.md" target="_blank">source repo</a>.

---

## Checkpoint

Congrats! You should now have a working OpenTelemetry Collector along with a backend stack to which the collector will forward data. Your project in Railway should look something like this -

<Image src="https://res.cloudinary.com/railway/image/upload/v1709927450/docs/tutorials/otel/CleanShot_2024-03-08_at_13.47.12_2x_iuhawv.png"
alt="Screenshot of Project Canvas"
layout="responsive"
width={1177} height={823} quality={100} />

Be sure to familiarize yourself with the Otel Collector's <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack/blob/main/otel-collector-config.yaml" target="_blank">configuration file</a>. The documentation on the format and structure of the file can be found <a href="https://opentelemetry.io/docs/collector/configuration/" target="_blank">here in Otel's official docs</a>.

---

## 3. Build and Instrument an Express App

Now that the collector stack is up, let's build and instrument an application!

_Note: The full source code for the <a href="https://github.com/railwayapp-templates/opentelemetry-collector-stack/tree/main/exampleApp" target="_blank">express app</a> that we will build is available in the Open Telemetry Collector repository that you forked in the previous steps._

### Create and initialize the project

From your local machine -

- Create a folder for your project called otel-example-app
- Use npm (or your preferred package manager) to install the required dependencies -

### Build the App

- In the otel-example-app folder, create an app.js file and add the following code -

- Create the dice.js file in the project folder and add the following code -

  We encourage you to refer to the OpenTelemetry documentation to gain a richer understanding of this code. The code you see above can be found <a href="https://opentelemetry.io/docs/languages/js/instrumentation/" target="_blank">here</a>.

### Build the Instrumentation SDK

- In the otel-example-app folder, create an instrumentation.js file and add the following code -

  This code will wrap your application code and capture the telemetry data. In the steps that follow, you will see how to start your application in Railway with a custom start command that utilizes this SDK.

  We encourage you to refer to the OpenTelemetry documentation to gain a richer understanding of this code. The code you see above can be found <a href="https://opentelemetry.io/docs/languages/js/instrumentation/" target="_blank">here</a>.

## 4. Deploy the Express App

### Create an Empty Service and Configure the Environment

In the same Railway project -

- Add a New service by clicking + New
- Select Empty Service
- Add the following variable to the service
  
  _This is used by the Express app to connect to the OpenTelemetry Collector_
- In the service Settings, add the following Custom Start Command:
  
  _This wraps the Express app on startup with the instrumentation SDK you created above._
- In the service Settings, rename the service to Express App
- Click Deploy to apply and create the empty service
- In the Settings tab, under Networking, click Generate Domain

### Deploy from the Railway CLI

_This step assumes you have the latest version of the Railway CLI installed._

On your local machine -

- Open your terminal and change directory to the otel-example-app folder
- Link to the Railway project and service by running the following command -

  Follow the prompts selecting the correct project name and environment (click <a href="https://res.cloudinary.com/railway/image/upload/v1709917423/docs/tutorials/otel/CleanShot_2024-03-08_at_10.58.55_2x_kacssj.png" target="_blank">here</a> for a reference), and choose the Express App service.

- Deploy the Express App by running the following command -
  

## 5. Test and Confirm

Test that everything is working by generating some traffic to your Express App. There is a single route, /rolldice, that takes a rolls query string -

- <YOUR_SERVICE_DOMAIN>/rolldice?rolls=10

Generate some traffic to this route, updating the number of rolls to different numbers, and verify that you see traces and spans in Jaeger and Zipkin.

<div style={{ display: 'flex', flexDirection: 'row', gap: '5px', fontSize: '0.9em', alignItems: 'stretch' }}>
    <div style={{ flex: '1 1 50%', overflow: 'auto', minWidth: '200px', maxWidth: '350px' }}>
        <Image src="https://res.cloudinary.com/railway/image/upload/v1709927026/docs/tutorials/otel/CleanShot_2024-03-08_at_13.42.44_2x_ym2ojg.png"
        alt="Screenshot of Jaeger UI"
        layout="responsive"
        width={1177} height={823} quality={100} />
        <p style={{ marginTop: '-0.2em', fontSize: '1em'}}>Jaeger</p>
    </div>
    <div style={{ flex: '1 1 50%', overflow: 'auto', minWidth: '200px', maxWidth: '350px' }}>
        <Image src="https://res.cloudinary.com/railway/image/upload/v1709926920/docs/tutorials/otel/CleanShot_2024-03-08_at_13.39.53_2x_zd69mq.png"
        alt="Screenshot of Zipkin Ui"
        layout="responsive"
        width={1177} height={823} quality={100} />
        <p style={{ marginTop: '-0.2em', fontSize: '1em'}}>Zipkin</p>
    </div>
</div>

## Bonus - NextJS

This tutorial was born out of an exploration into instrumenting some of our applications with <a href="https://nextjs.org/docs/pages/building-your-application/optimizing/open-telemetry#custom-exporters" target="_blank">NextJS's Otel library</a>. This means that you can use this Otel collector stack to capture telemetry data from your NextJS app!

### Send Telemetry Data from NextJS

Assuming you've followed the docs mentioned above to instrument your NextJS app, you can configure it to send requests to your collector in Railway by setting the required environment variable in the NextJS application.

_If your Next App is deployed in the **same Railway project as the collector**, you can use the private network -_

_If your Next App is deployed in **another Railway project, or outside of Railway entirely**, you can use the public network -_

- Note: If you use the public domain, you will need to update the PORT environment variable in your Otel Collector service to PORT=4318

#### Debugging in NextJS

Another helpful environment variable, specific to Node, is the debug directive -

## Helpful Resources

The OpenTelemetry Documentation is complete and easy to follow. We encourage you to spend time getting familiar with the docs, but here are some sections that we found especially helpful -

- OpenTelemetry Components
- OTLP Spec
- Collector Docs
- Collector Configuration Tool OTelBin
- Supported Languages
- Vendors with Native OTLP Support (explore this list for different backend options)

## Conclusion

Congratulations! You have deployed an OpenTelemetry Collector and a Node Express app that sends data to the collector which then sends it to Jaeger, Prometheus, and Zipkin.

This is a _very_ basic implementation, and you should refer to the <a href="https://opentelemetry.io/docs/" target="_blank">OpenTelemetry documentation</a> for information on how to customize your implementation.

## Code Examples

PORT=16686

PORT=9411

PORT=55679

npm i express @opentelemetry/api @opentelemetry/auto-instrumentations-node @opentelemetry/exporter-metrics-otlp-proto @opentelemetry/exporter-trace-otlp-proto @opentelemetry/resources @opentelemetry/sdk-metrics @opentelemetry/sdk-node @opentelemetry/semantic-conventions

// app.js //
  const express = require("express");
  const { rollTheDice } = require("./dice.js");

  const PORT = parseInt(process.env.PORT || "8080");
  const app = express();

  app.get("/rolldice", (req, res) => {
    const rolls = req.query.rolls ? parseInt(req.query.rolls.toString()) : NaN;
    if (isNaN(rolls)) {
      res
        .status(400)
        .send("Request parameter 'rolls' is missing or not a number.");
      return;
    }
    res.send(JSON.stringify(rollTheDice(rolls, 1, 6)));
  });

  app.listen(PORT, () => {
    console.log(`Listening for requests on http://localhost:${PORT}`);
  });

// Otel Docs Reference - https://opentelemetry.io/docs/languages/js/instrumentation/
  const { trace } = require("@opentelemetry/api");

  // obtain a trace
  const tracer = trace.getTracer("dice-lib");

  function rollOnce(i, min, max) {
    // start a span
    return tracer.startActiveSpan(`rollOnce:${i}`, span => {
      const result = Math.floor(Math.random() * (max - min) + min);

      // Add an attribute to the span
      span.setAttribute("dicelib.rolled", result.toString());

      // end the span
      span.end();
      return result;
    });
  }

  function rollTheDice(rolls, min, max) {
    // Create a span. A span must be closed.
    return tracer.startActiveSpan("rollTheDice", parentSpan => {
      const result = [];
      for (let i = 0; i < rolls; i++) {
        result.push(rollOnce(i, min, max));
      }
      // Be sure to end the span!
      parentSpan.end();
      return result;
    });
  }

  module.exports = { rollTheDice };

// Otel Docs Reference - https://opentelemetry.io/docs/languages/js/instrumentation
  const { NodeSDK } = require("@opentelemetry/sdk-node");
  const {
    getNodeAutoInstrumentations,
  } = require("@opentelemetry/auto-instrumentations-node");
  const {
    OTLPTraceExporter,
  } = require("@opentelemetry/exporter-trace-otlp-proto");
  const { Resource } = require("@opentelemetry/resources");
  const {
    SEMRESATTRS_SERVICE_NAME,
    SEMRESATTRS_SERVICE_VERSION,
  } = require("@opentelemetry/semantic-conventions");
  const {
    OTLPMetricExporter,
  } = require("@opentelemetry/exporter-metrics-otlp-proto");
  const {
    PeriodicExportingMetricReader,
  } = require("@opentelemetry/sdk-metrics");

  const sdk = new NodeSDK({
    resource: new Resource({
      [SEMRESATTRS_SERVICE_NAME]: "dice-server",
      [SEMRESATTRS_SERVICE_VERSION]: "0.1.0",
    }),
    traceExporter: new OTLPTraceExporter({
      url: `http://${process.env.OTEL_EXPORTER_OTLP_ENDPOINT}/v1/traces`,
    }),
    metricReader: new PeriodicExportingMetricReader({
      exporter: new OTLPMetricExporter({
        url: `http://${process.env.OTEL_EXPORTER_OTLP_ENDPOINT}/v1/metrics`,
      }),
    }),
    instrumentations: [getNodeAutoInstrumentations()],
  });

  sdk.start();

OTEL_EXPORTER_OTLP_ENDPOINT=${{OpenTelemetry Collector.RAILWAY_PRIVATE_DOMAIN}}:4318

node --require ./instrumentation.js app.js

railway link

railway up -d

OTEL_EXPORTER_OTLP_ENDPOINT=http://${{otel-collector.RAILWAY_PRIVATE_DOMAIN}}:4318

OTEL_EXPORTER_OTLP_ENDPOINT=https://<PUBLIC DOMAIN OF THE COLLECTOR IN RAILWAY>

OTEL_LOG_LEVEL=debug


# Add a CDN using CloudFront
Source: https://docs.railway.com/tutorials/add-a-cdn-using-cloudfront

Learn how to integrate Amazon CloudFront as a CDN for your Fastify app in this step-by-step guide.

> A CDN improves efficiency [of web applications] by introducing intermedeiary servers between the client and the server. [These CDN servers] decrease web traffic to the web server, reduce bandwidth consumption, and improve the user experience of your applications.

_Source: What is a CDN?_

## About this Tutorial

We know that performance of your web applications is critical to your business, and one way to achieve higher performance is by implementing a CDN to serve data from servers closest to your users.

Many CDN options are available (list from G2), but in this tutorial, we will cover step-by-step how to implement a CDN using Amazon CloudFront.

**Objectives**

In this tutorial, you will learn how to -

- Deploy a simple Fastify server to Railway
- Create a CloudFront distribution in AWS and connect it to the Fastify server
- _(Optional)_ Setup SSL and DNS for a custom domain managed in Namecheap

**Prerequisites**

To be successful using this tutorial, you should already have -

- Latest version of the Railway CLI installed
- An AWS account with permissions to create new resources
- Latest version of the AWS CLI installed and authenticated to your AWS account
- Latest version of the AWS CDK installed
- _(Optional)_ A Namecheap account to connect a custom domain

**Let's get started!**

## 1. Create and Deploy a Fastify Server

First, let's create and deploy a simple Fastify server using the Railway CLI

- On your local machine, create a folder called "fastify"
- Inside of the folder, create a file called "server.js"
- Run the following commands to initialize the project and install the required packages using npm
  
- Add the following code to the "server.js" file

- Run the following command to initialize a new project in Railway
  
- Follow the prompts and name your project "fastify-cdn"
- Run the following command to deploy your Fastify server
  
- Run the following command to generate a domain for the Fastify service
  
- Run the following command to open your Railway project in your browser
  

### Checkpoint

Nice! You now have a Fastify server running in Railway serving three routes, which will serve to demonstrate a few different concepts related to caching:

- /static - the static route serves a static message which never changes, unless the code is updated
- /dynamic - the dynamic route servers a dynamic message which changes when the route is accessed and the Date() function runs
- /staticEtag - the staticEtag route demonstrates how you can manually set an HTTP Etag on a route

  _Note: The Fastify server code above implements Fastify's eTag plugin._

#### Observe Route Behavior with no CDN

To observe the behavior without a CDN in place, navigate to any of the routes above from the Railway-provided domain, your request will always go directly to the service running in Railway.

One way you can visualize this, is by navigating to the /static route in your browser, opening up Network Tools, and observing that each request always receives a **HTTP 200** status code:

<Image src="https://res.cloudinary.com/railway/image/upload/v1719001891/docs/tutorials/CDN/CleanShot_2024-06-21_at_15.28.36_2x_em6o5s.png"
alt="Screenshot of DevTools no CDN"
layout="responsive"
width={1477} height={623} quality={100} />

Since the data for the route has not been cached on a CDN, the server receives every request, generates a new timestamp, and sends it back with a 200 status code.

Once we setup the CloudFront CDN, we will see how this behavior changes.

## 2. Create a CloudFront Distribution in AWS

_This step assumes you have already configured the AWS CLI to connect to your AWS account._

Now let's create a CloudFront distribution using the AWS CDK.

- In your "fastify" folder, create a new folder called "cloudfront"
- Within the "cloudfront" folder, run the following command to initialize a new CDK project in TypeScript
  
- Run the following command to install the CDK packages for CloudFront
  
- Replace the contents of the "/bin/cloudfront.ts" file with the following code.

  _When you run cdk bootstrap in the following steps, the account and region environment variables should be added for you._

- Replace the contents of the "/lib/cloudfront-stack.ts" file with the following code

  **IMPORTANT: Be sure to replace the HttpOrigin in the code above with the Railway-provided domain (e.g. _fastify-server.up.railway.app_)**

- Run the following command to bootstrap the environment for the CDK
  
- Run the following command to deploy the CloudFront distribution
  

_If you experience any problems with the AWS utilities used in this step, you can create and configure the CloudFront distribution manually using the AWS Management Console, using the same settings defined in the "cloudfront-stack.ts" file._

### Checkpoint 2

Great job! You should now have a CloudFront distribution pointed to your Fastify service in Railway. Your distribution will be assigned a domain similar to the one below:

- https://d1a23bcdefg.cloudfront.net

Now let's see how the behavior for the /dynamic route has changed when accessing the server from the CloudFront distribution domain.

<Image src="https://res.cloudinary.com/railway/image/upload/v1719001866/docs/tutorials/CDN/CleanShot_2024-06-21_at_15.24.47_2x_knqo9f.png"
alt="Screenshot of DevTools with CDN"
layout="responsive"
width={1477} height={623} quality={100} />

Notice how the first request was served an **HTTP 200** from the server with the dynamically generated data, but subsequent requests were served a **HTTP 304 Not Modified** code.

This is the CloudFront CDN in action!

If you inspect the route definition for /dynamic, you'll see that the headers include a cache-control parameter:

This cache control definition tells CloudFront to revalidate the data at the route after 60s.

#### Cache Behavior

When the initial request is made to the route, CloudFront retrieves the data from the server, then stores it. For 60s after the initial request, CloudFront will serve the cached response with **HTTP 304**, and after 60s, it will check the server for new data.

#### Faster Response Time

In the screenshot above, take note of the Size and Time columns.

When CloudFront serves the cached data, it takes significantly less time to resolve the route, and, probably due to less headers, the Size of the message is also smaller.

## 3. Connect a Custom Domain with SSL enabled

Now that the CloudFront distribution is up and running, you may want to connect a custom domain and ensure SSL is enabled.

This step will _quickly_ cover how to generate a SSL certificate in AWS and configure the custom domain in Namecheap and CloudFront.

Let's first generate an SSL certificate -

- In AWS Management Console, navigate to your CloudFront distribution
- Under the General tab, click the Edit button
- Under _Custom SSL certificate_, click the _"Request certificate"_ link below the input field. This will take you to AWS Certificate Manager.
- Click the Next button to request a public certificate
- Enter your fully qualified domain name, e.g. www.railway.com
  - If you'd like the cert to include the apex domain, click Add another name to this certificate and enter it, e.g. railway.com
- Click the Next button to generate the certificate
- In **Namecheap**, in the Advanced DNS section for the domain, add the host record(s).
  - If you set up the certificate for both www and the apex domain, you will add two **CNAME** records
  - The CNAME name value provided by AWS, should be used as the **Host** value in Namecheap.
  - The CNAME name value provided by AWS, includes the domain name, but in Namecheap, you should add everything except the domain, e.g.
    - if your CNAME name is _6cf3abcd1234abcd1234aabb11cc22.www.railway.com
    - you should add _6cf3abcd1234abcd1234aabb11cc22.www to the **Host** value in Namecheap
- Once you add the DNS records in Namecheap, refresh the Certificate status page in AWS to confirm the Status shows **Success**

Now, we'll add the certificate in the CloudFront distribution settings and finish setting up the custom domain -

- Return the the CloudFront distribution settings
- Under _Custom SSL certificate_, choose the certificate you just created from the drop down menu
- Under _Alternate domain name (CNAME)_, add your custom domain.
  - If you want both www and apex domain, be sure to add both
- At the bottom, click the Save changes button
- In **Namecheap**, in the Advanced DNS section for the domain, add the host record(s)
  - If you are setting up both www and the apex domain, you will add two **ALIAS** records
  - The record value should be your Cloudfront distribution domain, e.g. d1a23bcdefg.cloudfront.net
  - The **Host** value should be @ for the apex domain and www for the www subdomain.

That's it! You should now be able to navigate to the three routes in the Fastify service from your custom domain.

## Conclusion

Congratulations! You have deployed a Fastify app to Railway, created a CloudFront distribution in AWS connected to the Railway service, and (optionally) connected your custom domain in Namecheap to the CloudFront distribution with SSL enabled.

#### Additional Resources

This is a _very_ simple tutorial covering the most basic steps to implement CloudFront CDN in your stack. There are many, many more concepts you should explore related to CDNs and caching in general, to take full advantage of the technology and tailor it to your specific needs.

We recommend checking out these resources to start:

- What is a CDN?
- What is caching?
- CDN vs Caching

## Code Examples

npm init -y
  npm i fastify @fastify/etag

const Fastify = require("fastify");
  const fastifyEtag = require("@fastify/etag");

  const fastify = Fastify();
  fastify.register(fastifyEtag);

  fastify.get("/dynamic", async (request, reply) => {
    console.log("Received request on dynamic route");

    const staticContent = {
      message: "This is some dynamic content",
      timestamp: new Date().toISOString(),
    };

    reply.type("application/json");
    reply.headers({
      "cache-control": "must-revalidate, max-age=60",
    });

    reply.send(staticContent);
  });

  fastify.get("/static", async (request, reply) => {
    console.log("Received request on static route");

    const staticContent = {
      message: "This is some static content",
    };

    reply.type("application/json");
    reply.headers({
      "cache-control": "must-revalidate, max-age=60",
    });

    reply.send(staticContent);
  });

  fastify.get("/staticEtag", async (request, reply) => {
    console.log("Received request on staticEtag route");

    const staticContent = {
      message: "This will serve a static etag",
    };

    reply.type("application/json");

    reply.headers({
      "cache-control": "must-revalidate, max-age=60",
    });

    reply.header("etag", '"foobar"');
    reply.send(staticContent);
  });

  const start = async () => {
    try {
      await fastify.listen({
        port: Number(process.env.PORT) || 3000,
        host: "0.0.0.0",
      });
      console.log(
        `Server is running at PORT:${Number(process.env.PORT) || 3000}`,
      );
    } catch (err) {
      fastify.log.error(err);
      process.exit(1);
    }
  };

  start();

railway init

railway up -d

railway domain

railway open

cdk init app --language typescript

npm install @aws-cdk/aws-cloudfront @aws-cdk aws-cloudfront-origins @aws-cdk/core

#!/usr/bin/env node
  import "source-map-support/register";
  import * as cdk from "@aws-cdk/core";
  import { CloudfrontCdkStack } from "../lib/cloudfront-stack";

  const app = new cdk.App();
  new CloudfrontCdkStack(app, "CloudfrontCdkStack", {
    env: {
      account: process.env.CDK_DEFAULT_ACCOUNT,
      region: process.env.CDK_DEFAULT_REGION,
    },
  });

import * as cdk from "@aws-cdk/core";
  import * as cloudfront from "@aws-cdk/aws-cloudfront";
  import * as origins from "@aws-cdk/aws-cloudfront-origins";

  export class CloudfrontCdkStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
      super(scope, id, props);

      // Replace with the Domain provided by Railway
      const origin = new origins.HttpOrigin("RAILWAY PROVIDED DOMAIN");

      // Custom Cache Policy
      const cachePolicy = new cloudfront.CachePolicy(
        this,
        "CustomCachePolicy",
        {
          cachePolicyName: "CustomCachePolicy",
          minTtl: cdk.Duration.seconds(0),
          maxTtl: cdk.Duration.seconds(86400),
          defaultTtl: cdk.Duration.seconds(60),
          cookieBehavior: cloudfront.CacheCookieBehavior.all(),
          queryStringBehavior: cloudfront.CacheQueryStringBehavior.all(),
          headerBehavior: cloudfront.CacheHeaderBehavior.allowList(
            "CloudFront-Viewer-Country",
            "CloudFront-Is-Mobile-Viewer",
          ),
        },
      );

      // CloudFront distribution
      const distribution = new cloudfront.Distribution(this, "Distribution", {
        defaultBehavior: {
          origin,
          cachePolicy: cachePolicy,
          viewerProtocolPolicy:
            cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
        },
      });
    }
  }

cdk bootstrap

cdk deploy

reply.headers({
        'cache-control': 'must-revalidate, max-age=60'
    });


# Deploying a Monorepo
Source: https://docs.railway.com/tutorials/deploying-a-monorepo

Learn how to deploy a monorepo to Railway.

A monorepo is a project directory structure in which multiple, co-dependent codebases (such as a frontend and a backend) are maintained within the same repository, and in some cases, share common packages.

## About This Tutorial

Deploying a monorepo in Railway requires some extra configuration to get the applications up and running.

This tutorial aims to provide a simple step-by-step on how to deploy a frontend and backend from an isolated monorepo, one of the most commonly deployed types of monorepo.

The procedure outlined in this tutorial can easily be adapted to deploy different apps that are contained within a isolated monorepo as well.

For more information on deploying a shared monorepo check out our <a href="/guides/monorepo#deploying-a-shared-monorepo" target="_blank">guide</a> that explains some of the specific configurations you would need. If you are importing a JS monorepo, check out our <a href="/guides/monorepo#automatic-import-for-javascript-monorepos" target="_blank">guide</a> for automatic import.

**Objectives**

In this tutorial, you will learn how to -

- Create an empty project.
- Rename a project.
- Create empty services.
- Rename services.
- Generate domains for services.
- Set variables on a service.
- Connect a GitHub repo to a service.

**Prerequisites**

For the sake of this tutorial, we have a simple example monorepo with a frontend and a backend service. In practice, your monorepo is probably a lot more complicated, but the principles here will enable you to wire up each of your applications in your monorepo to a service and network those services together.

The frontend is built with React and Vite, and the static files are served with Caddy.

The backend, built with Go, will stream quotes that will be displayed on the frontend.

Before you start:

1. Fork the repo: https://github.com/railwayapp-templates/monorepo-example
2. Connect your GitHub to Railway. This will enable you to deploy any of your repositories to Railway in the future as well!

**Let's get started!**

## 1. Create a New Empty Project

- From your dashboard click + New Project or âŒ˜ k

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269034/docs/tutorials/monorepo/dashboard_zojmjg.png"
alt="Screenshot of dashboard"
layout="responsive"
width={1280} height={511} quality={100} />

- Choose Empty project

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269027/docs/tutorials/monorepo/new_project_hxiif2.png"
alt="Screenshot of new project page"
layout="responsive"
width={345.5} height={388} quality={100} />

**Note:** We chose an empty project instead of deploying from a GitHub repo since we want to set up the project before deploying.

## 2. Project Setup

- You'll notice Railway automatically named the project, but we want something more recognizable. Open the Settings tab to Update the name of your project. You'll also notice the Danger tab here, when you want to delete your project after you're done with the tutorial.

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269026/docs/tutorials/monorepo/project_settings_ym1vul.png"
alt="Screenshot of project settings"
layout="responsive"
width={1381} height={731} quality={100} />

- Click Update

## 3. Service Creation

- Add **two** new **empty** services from the + Create button in the top right of the project canvas.

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269020/docs/tutorials/monorepo/create_menu_gtpxtb.png"
alt="Screenshot of create menu"
layout="responsive"
width={735} height={510} quality={100} />

**Note:** We chose an empty service instead of deploying from a GitHub repo since we want to configure the service before deploying.

The result will look like this -

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269019/docs/tutorials/monorepo/two_services_unamed_nmwimm.png"
alt="Screenshot of project canvas with two empty services"
layout="responsive"
width={766} height={450} quality={100} />

- Give them both applicable names.

  **Note:** This can be done easiest via the right-click context menu.

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269022/docs/tutorials/monorepo/naming_a_service_qy7sg5.png"
alt="Screenshot of naming a service"
layout="responsive"
width={766} height={450} quality={100} />

In the case of this tutorial, they will be named Frontend and Backend

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269024/docs/tutorials/monorepo/deploy_button_gmnqf8.png"
alt="Screenshot showing the deploy button"
layout="responsive"
width={766} height={450} quality={100} />

- Click the Deploy button or â‡§ Enter to create these two services.

## 4. Directory Setup

Both of our apps deploy from subdirectories of our monorepo, so we need to tell Railway where they are located.

- Open the Frontend service to its service settings and you will see a **Root Directory** option, in this case, we will set it to /frontend

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269052/docs/tutorials/monorepo/frontend_root_dir_e52vkz.png"
alt="Screenshot showing the frontend root directory"
layout="responsive"
width={1386} height={760} quality={100} />

- Open the Backend service settings and we will set its root directory to /backend

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269046/docs/tutorials/monorepo/backend_root_dir_misneo.png"
alt="Screenshot showing the backend root directory"
layout="responsive"
width={1386} height={760} quality={100} />

- Click the Deploy button or â‡§ Enter to save these changes.

## 5. Connecting the Repo

Now we need to configure the source of the service where the code is deployed.

- Open the service settings for each service and connect your monorepo.

Frontend

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269039/docs/tutorials/monorepo/frontend_repo_connect_llgsmf.png"
alt="Screenshot showing the frontend repo connected"
layout="responsive"
width={1386} height={760} quality={100} />

Backend

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269044/docs/tutorials/monorepo/backend_repo_connect_evt8v3.png"
alt="Screenshot showing the backend repo connected"
layout="responsive"
width={1386} height={760} quality={100} />

- Click the Deploy button or â‡§ Enter to deploy your applications

**Your services will now build and deploy.**

## 6. Domain Setup

Even though the services are now running, the frontend and backend aren't networked together yet. So let's setup domains for each service.

Both the Vite Frontend and the Go Backend are already configured so that Railway will âœ¨automagically detect the port they're running on. Railway does this by detecting the env.$PORT variable that the service is binding. For simplicity's sake, we will connect these two services over their public domain so you can get a handle on the basics. In practice, you may need to configure your networking a bit differently. You can read more about networking in the docs.

Let's add public domains to both services.

- Click on the service and then open the Settings tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269032/docs/tutorials/monorepo/service_settings_networking_ckrss1.png"
alt="Screenshot showing the service settings"
layout="responsive"
width={1381} height={760} quality={100} />

- Click on Generate Domain. Railway will âœ¨automagically assign the port based on the deployed service.

- Do these steps for both services, so that they both have public domains.

**Notes:**

- **Setting a Custom $PORT:** Adding the domain after the service is deployed allows Railway to detect the bound env.$PORT. You could instead decide to manually set the $PORT variable on the Variables tab, and set the Domain to use that custom port instead.

## 7. Variable Setup

For our example monorepo the Frontend service needs a VITE_BACKEND_HOST variable, and our backend needs an ALLOWED_ORIGINS variable.

Let's add the Frontend variable first.

- Click on Frontend service, then the Variables tab

- Add the required variable -

  It should look like this once added:

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269049/docs/tutorials/monorepo/adding_frontend_variables_jqn4rf.png"
alt="Screenshot showing the frontend service variables"
layout="responsive"
width={1386} height={760} quality={100} />

Now let's add the Backend variable.

- Click on the Backend service, then the Variables tab

- Add the required variable -

It should look like this once added:

<Image src="https://res.cloudinary.com/railway/image/upload/v1721269042/docs/tutorials/monorepo/adding_backend_variables_aplgej.png"
alt="Screenshot showing the backend service variables"
layout="responsive"
width={1386} height={760} quality={100} />

- Click the Deploy button or â‡§ Enter to save these changes.

- Your services should be deployed and available now! Click on your frontend service on the Deployment tab and you can click your domain to see the webapp.

**Notes:**

- The variables used here are reference variables, learn more about them here.

- Both the Frontend and Backend variables reference each other's public domains. The RAILWAY_PUBLIC_DOMAIN variable will be automatically updated whenever you deploy or re-deploy a service.

- See a list of additional variables here.

## Conclusion

Congratulations! You have setup a project, setup services, added variables and deployed your monorepo project to Railway. The Frontend service should be accessible on its public domain to access the deployed website.

## Code Examples

VITE_BACKEND_HOST=${{Backend.RAILWAY_PUBLIC_DOMAIN}}

ALLOWED_ORIGINS=${{Frontend.RAILWAY_PUBLIC_DOMAIN}}


# Proximity Steering
Source: https://docs.railway.com/tutorials/proximity-steering

Learn how to set up proximity steering using Cloudflare in this step-by-step tutorial.

> Proximity steering routes visitors ... to the closest physical data center.

_Source: <a href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/" target="_blank">Proximity steering</a>_

Sometimes also referred to as Geo-Load Balancing.

## About this Tutorial

As Railway does not offer native Proximity Steering at this time, we instead need to place Cloudflare in front of our services to do this for us.

This tutorial aims to provide a simple step-by-step guide on setting everything up on Cloudflare to ensure Proximity Steering works flawlessly!

**Objectives**

In this tutorial, you will learn how to do the following in Cloudflare -

- Create a Health monitor.
- Create pools for each region.
- Set up the Proximity Load Balancer.

**Prerequisites**

**In Railway -**

- Have two or more identical services deployed in two or more different regions in Railway.

  Duplicating a service can be done by right clicking and selecting **Duplicate**, opening its service settings and changing the region, then clicking **Deploy**.

  The services should be configured with a Railway-generated domain, do not assign a custom domain. It is also helpful to indicate the region in the domain.

  It's recommended to use shared variables or reference variables for duplicated services to keep variables in sync.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015743/docs/tutorials/proximity-load-balancing/region_services_u10ukp.png"
alt="screenshot of two railway services in different regions"
layout="responsive"
width={890} height={435} quality={100} />

- Have a /health or similar endpoint in the services deployed to Railway, which should return a 200 status code when queried.

  This allows Cloudflare to check the health of our Railway services so they can handle region failover. As a bonus this can also be used on Railway to achieve zero-downtime deployments.

**In Cloudflare -**

- Have your desired domain setup with Cloudflare's nameservers, they have a general guide for that here.

- Have **SSL/TLS** mode set to **Full**.

  **SSL/TLS â†’ Overview â†’ Full**

- Have **Always Use HTTPS** enabled.
  **SSL/TLS â†’ Edge Certificates â†’ Always Use HTTPS**
  This ensures that Railway avoids managing the insecure redirect, which would otherwise lead to an incorrect redirection to an upstream endpoint.

## 1. Creating a Health Monitor

- Open the Load Balancing page.

  **Traffic â†’ Load Balancing**

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015860/docs/tutorials/proximity-load-balancing/load_balancing_page_yn5bm8.png"
alt="screenshot of the load balancing page"
layout="responsive"
width={1060} height={555} quality={100} />

- Click **Manage Monitors** and then **Create**.

- Enter your desired name for this health monitor.

- Choose **HTTPS** as the type.

- Enter your health endpoint path

  Example - /health

- Leave Port 443 as the default.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015787/docs/tutorials/proximity-load-balancing/health_monitor_oty6pd.png"
alt="screenshot of the cloudflare health monitor"
layout="responsive"
width={1060} height={315} quality={100} />

- Click **Save**.

## 2. Creating the Pools

- Go back to the Load Balancing page.

- Click **Manage Pools** and then **Create**.

- Fill out the name and description and leave **Endpoint Steering** as its default of **Random**, it will not be used with only a single endpoint.

- Enter the endpoint name, using the service name is ideal.

- For the **Endpoint Address** we use the Railway generated domain.

  Example - my-service-us-west2.up.railway.app

  This should only be the domain, excluding both the scheme and trailing slash.

- For the weight option we will use a value of **1**.

- Click **Add host header** and enter the same value as used for the Endpoint Address.

  This step is important since Railway uses host-based routing and requires the host header to know how to route the incoming requests from Cloudflare.

- Remove the second empty endpoint.

  Our pool only needs to contain a single endpoint as Railway handles single region replicas for us.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015878/docs/tutorials/proximity-load-balancing/pool_settings_config_qh5s1k.png"
alt="screenshot of end endpoint settings in the pool creator"
layout="responsive"
width={1060} height={600} quality={100} />

- Click **Configure coordinates for Proximity Steering** and enter the latitude and longitude for your service region.

  | Region    |  Latitude |   Longitude |
  | --------- | --------: | ----------: |
  | US East   | 39.005111 |  -77.491333 |
  | US West   | 37.353111 | -121.936278 |
  | EU West   | 52.379139 |    4.900278 |
  | Singapore |  1.307222 |  103.790583 |

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015901/docs/tutorials/proximity-load-balancing/pool_settings_proximity_rybg2r.png"
alt="screenshot of the proximity settings in the pool creator"
layout="responsive"
width={1060} height={600} quality={100} />

- Select the Monitor dropdown and add our **Health** monitor that we created earlier.

- Choose the applicable health check region according to the region where the Railway service was deployed.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015844/docs/tutorials/proximity-load-balancing/pool_settings_health_ydlzvo.png"
alt="screenshot of the health settings in the pool creator"
layout="responsive"
width={1060} height={375} quality={100} />

- Click **Save**.

- Create another pool for your other services that are deployed in your desired regions, and follow the same procedure.

This should be the end result, two or more pools -

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015821/docs/tutorials/proximity-load-balancing/pools_w1gext.png"
alt="screenshot of adding pools in the load balancer creator"
layout="responsive"
width={1060} height={435} quality={100} />

## 3. Creating the Load Balancer

- Go back to the Load Balancing page.

- Click **Create Load Balancer**.

- Enter the desired hostname or leave as the default for the root hostname.

  You may need to remove the leading period from the default hostname.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722016030/docs/tutorials/proximity-load-balancing/load_balancer_hostname_pfeolj.png"
alt="screenshot of the hostname in the load balancer creator"
layout="responsive"
width={1060} height={315} quality={100} />

- Click **Next**.

- Add all the pools that were previously setup.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722016015/docs/tutorials/proximity-load-balancing/load_balancer_pools_egolib.png"
alt="screenshot of selected pools in the load balancer creator"
layout="responsive"
width={1060} height={585} quality={100} />

- Select the appropriate fallback pool.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015976/docs/tutorials/proximity-load-balancing/load_balancer_fallback_pool_krelrk.png"
alt="screenshot of fallback pool in the load balancer creator"
layout="responsive"
width={1060} height={260} quality={100} />

- Click **Next**.

- Monitors have already been setup on both pools, Click **Next**.

- Choose **Proximity steering**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015998/docs/tutorials/proximity-load-balancing/load_balancer_traffic_steering_bv3kwm.png"
alt="screenshot of traffic steering options in the load balancer creator"
layout="responsive"
width={1060} height={585} quality={100} />

- Click **Next**.

- If needed, create Custom Rules, otherwise click **Next**.

- Review the Load Balancing setup, if all looks good click **Save and Deploy**.

## Conclusion

After that process you should see something like the following -

<Image src="https://res.cloudinary.com/railway/image/upload/v1722015766/docs/tutorials/proximity-load-balancing/load_balancer_exgakv.png"
alt="screenshot of the finished load balancer"
layout="responsive"
width={1060} height={585} quality={100} />

That's all for the setup! You can now open your domain and Cloudflare will automatically route your requests to the Railway service you are in closest proximity to.

**Additional Resources**

This tutorial covers setting up a Proximity Load Balancer on Cloudflare but does not cover all the settings and configurations Cloudflare offers.

We recommend checking out these resources from Cloudflare:

- What is load balancing?
- Proximity steering
- Components of a load balancer
- Monitors and health checks
- Session affinity
- Override HTTP Host headers


# Set up a Tailscale Subnet Router
Source: https://docs.railway.com/tutorials/set-up-a-tailscale-subnet-router

Learn how to access a private network on Railway by using a Tailscale Subnet Router.

> A subnet router is a device within your tailnet that you use as a gateway that advertises routes for other devices that you want to connect to your tailnet without installing the Tailscale client.

_Source: <a href="https://tailscale.com/kb/1019/subnets" target="_blank">Subnet routers</a> Via Tailscale's Documentation_

In the context of Railway, The "other devices" are the services within a project.

## About this Tutorial

This tutorial will help you connect to your database via the private network without you having to use public endpoints.

Since Railway doesn't currently offer a native way to access the <a href="https://docs.railway.com/reference/private-networking" target="_blank">private network</a> from our local environment, we can use a Tailscale Subnet Router to accomplish this.

Deploying Tailscale as a subnet router into our project means that we can access the railway.internal private domains from any device connected to our tailnet.

This tutorial aims to provide a simple step-by-step guide on setting up everything needed so that we can access the private domains of our services.

**Objectives**

In this tutorial, you'll learn how to do the following: -

- Generate an Auth Key.
- Set up split DNS.
- Deploy the Tailscale Subnet Router template.
- Approve the private network subnet.
- (Bonus) Connect to Postgres locally via the private domain.

**Prerequisites**

This guide assumes you are familiar with the concepts of Private Network, for a quick explainer check out our <a href="/guides/private-networking" target="_blank">guide</a> and <a href="/reference/private-networking" target="_blank">reference</a> page.

**In Railway -**

- Have all the services you plan on connecting to via the tailnet, listening on IPv6.

  This is necessary because the Tailscale tunnel will communicate with your services over Railway's IPv6-only private network.

  All database services already do this but for information on configuring your service to listen on IPv6, see here.

**In Tailscale -**

- Have an account.

  You can sign up <a href="https://login.tailscale.com/start" target="_blank">here</a> - For what this template achieves you do not need a paid plan.

- Have the Tailscale app installed on your computer.

  You can find the downloads for your OS <a href="https://tailscale.com/download" target="_blank">here</a>.

## 1. Getting an Auth Key

The Auth key will authenticate the Tailscale machine that we'll deploy into our Railway project in a later step.

- Head over to the Keys page located within the settings menu on the Tailscale dashboard.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349121/docs/tutorials/tailscale-subnet-router/keys_page_vohahp.png"
alt="screenshot of the tailscale settings page"
layout="intrinsic"
width={1261} height={772} quality={100} />

- Click **Generate auth key**.

  Put in a description and leave all other settings as the default.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349121/docs/tutorials/tailscale-subnet-router/generate_auth_key_oxqr8m.png"
alt="screenshot of the generate auth key modal in tailscale"
layout="intrinsic"
width={602} height={855} quality={100} />

- Click **Generate key**.

  Tailscale will now show you the newly generated auth key, **be sure to copy it down**.

- Click **Done**.

## 2. Configure Split DNS

Properly configuring our nameserver in Tailscale is essential for enabling local DNS lookups for our private domains.

- Open the <a href="https://login.tailscale.com/admin/dns" target="_blank">DNS</a> page.

- Under the **Nameservers** Header, click **Add Nameserver** â†’ Click **Custom**.

  This is where we'll tell Tailscale how to route the DNS lookups for our railway.internal domains.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349122/docs/tutorials/tailscale-subnet-router/tailscale_nameservers_en8oma.png"
alt="screenshot of the nameservers dropdown in tailscale"
layout="intrinsic"
width={813} height={683} quality={100} />

- Enter fd12::10 as the Nameserver.

  This DNS nameserver is used across all private networks in every environment and will handle our DNS queries for private domains.

- Enable the **Restrict to domain** option, AKA Split DNS.

- Enter in railway.internal as our domain.

  This makes sure only DNS lookups for our private domain are forwarded to the private DNS resolver.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349120/docs/tutorials/tailscale-subnet-router/add_nameserver_mlkk5y.png"
alt="screenshot of the add nameserver modal in tailscale"
layout="intrinsic"
width={602} height={572} quality={100} />

- Click **Save**.

## 3. Deploy the Tailscale Subnet Router

This will be the gateway into our environment's private network.

- Open the project that contains the services you want to access privately.

  For this tutorial, we will deploy the Subnet Router into a project with a Postgres database service.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349122/docs/tutorials/tailscale-subnet-router/project_with_postgres_x19ggr.png"
alt="screenshot of a project canvas on railway showing a single postgres service"
layout="intrinsic"
width={1363} height={817} quality={100} />

- In the top right of the project canvas, click **Create** â†’ Choose **Template**.

- Search for the <a href="https://railway.com/template/tailscale" target="_blank">Tailscale Subnet Router</a> template.

  Choose the result that is published by **Railway Templates**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471191/docs/template-tailscale_ryph2o.png"
alt="screenshot of the choose a template modal showing the tailscale template within railway"
layout="intrinsic"
width={1200} height={634} quality={100} />

- A ghost service will appear, Paste in your Auth Key from earlier.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349120/docs/tutorials/tailscale-subnet-router/tailscale_subnet_router_ghost_jjyt2s.png"
alt="screenshot of the tailscale template asking for the auth key"
layout="intrinsic"
width={1363} height={817} quality={100} />

- Click **Deploy Template**

This template will start to deploy and once deployed it will register itself as a machine in your tailnet with the name automatically derived from the project's name and environment name.

## 4. Approve the Subnet

Our subnet router will advertise the private network's CIDR range but we will need to manually approve it.

- Head back over to our Machines dashboard.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349122/docs/tutorials/tailscale-subnet-router/tailscale_machines_d3qcey.png"
alt="screenshot of the machine's dashboard in tailscale that is showing a subnet needs approving"
layout="intrinsic"
width={1261} height={560} quality={100} />

You will see your newly deployed machine with its name that was previously derived from the project and environment.

<div style={{'display': "inline-flex", 'align-items': "center"}}>
    <span style={{ "marginRight": "8px" }}>Notice the</span><strong style={{ "marginRight": "3px" }}>Subnets</strong>
    <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.75" stroke-linecap="round" stroke-linejoin="round" class="ml-1"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
    <span style={{ "marginLeft": "6px" }}>Info box under the machine name.</span>
</div>

- Click on the machine's 3-dot menu â†’ **Edit route settings**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349121/docs/tutorials/tailscale-subnet-router/machine_3_dot_menu_ygqktw.png"
alt="screenshot of the machines page in tailscale with the 3-dot menu open and edit route settings selected"
layout="intrinsic"
width={1320} height={593} quality={100} />

- Click the radio button on the fd12::/16 to accept it.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349120/docs/tutorials/tailscale-subnet-router/edit_route_settings_tyna0n.png"
alt="screenshot of the edit route settings in tailscale showing our route being accepted"
layout="intrinsic"
width={602} height={526} quality={100} />

    This route covers the entire private networking range allowing us to access all services within the project.

- Click **Save**.

- Ensure that the **Use Tailscale subnets** option is enabled in your Tailscale client's Settings or Preferences menu.

**That is it for all the configurations needed, you can now call any service via its private domain and port just as if you were another service within the private network!**

## 5. Connecting To a Service On the Private Network (Bonus)

During this tutorial we have used Postgres as an example service, so let's finally connect to it via its private domain and port!

You can use any database GUI tool you prefer, or none at all, since our setup allows you to connect to the database over the private network using any software.

Example: Your prisma migrate deploy or python manage.py migrate commands will now work locally without the need to use the public host and port for the database.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349120/docs/tutorials/tailscale-subnet-router/dbgate_priv_net_mdjnlh.png"
alt="screenshot of dbgate showing that we have successfully connected to our database"
layout="intrinsic"
width={1316} height={506} quality={100} />

_Note the use of our private domain and port in the database URL._

**Additional Resources**

This tutorial explains how to set up a Tailscale Subnet router on Railway but does not delve into all the terminology and settings related to Tailscale.

We recommend reviewing the following Tailscale documentation:

- Subnet router
- Auth keys
- Machine names
- DNS
- Tailscale FAQ


# Bridge Railway to RDS with Tailscale
Source: https://docs.railway.com/tutorials/bridge-railway-to-rds-with-tailscale

Learn how to securely access your AWS RDS database from Railway using a Tailscale subnet router.

In this tutorial, you will set up a Tailscale bridge to AWS RDS. This creates a secure tunnel between your Railway services and your AWS RDS database instances. This allows you to connect to your RDS databases privately without exposing traffic to the public internet.

### Objectives

In this tutorial, you will:

1. Deploy a Tailscale subnet router EC2 instance
1. Set up split DNS for domain resolution
1. Verify and test connectivity to your RDS instance
1. Route traffic from Railway to RDS using Railtail

This tutorial is in depth, so if it's your first time using Tailscale or setting up a bridge to your RDS instance, we'll cover every detail!

### Prerequisites

1. You will need an AWS IAM access key or IAM Role to stand up resources with Terraform or OpenTofu.

   **NOTE:** While you can just put these secrets in a ~/.aws folder or a terraform.tfvars file, it's a good practice to avoid putting secrets on disk unencrypted. If you have 1Password, you can use 1Password Secret References so that your secrets are never stored permanently on disk. This is especially important to prevent AI tools from reading your keys and as an extra layer of protection from committing secrets to your git repositories.

2. You'll need to install Terraform or OpenTofu.

3. You will need to generate a new ssh key that we can use to provision the AWS Instance.

4. You will need a Tailscale account and have Tailscale installed on your local machine. The free tier is generous and sufficient for this tutorial.

5. You will need to generate, store, and reference a Tailscale Auth Key

### Generate a Tailscale Auth Key

- Head over to the Keys page located within the settings menu on the Tailscale dashboard.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349121/docs/tutorials/tailscale-subnet-router/keys_page_vohahp.png"
alt="screenshot of the tailscale settings page"
layout="intrinsic"
width={1261} height={772} quality={100} />

- Click **Generate auth key**.

  Put in a description like "AWS RDS Subnet Router" and leave all other settings as the default.

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349121/docs/tutorials/tailscale-subnet-router/generate_auth_key_oxqr8m.png"
alt="screenshot of the generate auth key modal in tailscale"
layout="intrinsic"
width={602} height={855} quality={100} />

- Click **Generate key**.

  Tailscale will now show you the newly generated auth key. **Be sure to copy it down, and store it in secret store (like 1Password)**.

- Click **Done**.

## git clone the example project

We've prepared an example project built in Terraform (or OpenTofu if you prefer) to stand up all the AWS resources you'll need to test out connectivity to RDS.

### Create terraform.tfvars

Create a terraform.tfvars file to store your variables:

**!IMPORTANT**: Make sure you update your userlist.txt password to the same password as your new rds_password.

### Deploy

Initialize and apply the Terraform configuration:

Review the changes and type yes to confirm deployment.

When the deployment completes, you'll see outputs including instructions for configuring split DNS and how to run the test script to verify your deployment.

## Configure Split DNS in Tailscale

Split DNS allows Tailscale to resolve AWS RDS domain names using AWS DNS servers, which is required for RDS connectivity.

- Go to the Tailscale Admin Console DNS settings
- Click **Add Nameserver** â†’ Choose **Custom**

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349122/docs/tutorials/tailscale-subnet-router/tailscale_nameservers_en8oma.png"
alt="screenshot of the nameservers dropdown in tailscale"
layout="intrinsic"
width={813} height={683} quality={100} />

- Enter the VPC DNS server IP: 172.16.0.2 (VPC CIDR base + 2)
- Enable **Restrict to domains**
- Enter: us-west-2.rds.amazonaws.com (replace us-west-2 with your AWS region)

<Image src="https://res.cloudinary.com/railway/image/upload/v1724349120/docs/tutorials/tailscale-subnet-router/add_nameserver_mlkk5y.png"
alt="screenshot of the add nameserver modal in tailscale"
layout="intrinsic"
width={602} height={572} quality={100} />

- Click **Save**

## Approve Advertised Subnet Routes and/or Enable Route Acceptance on Your Devices

For devices you can't install Tailscale on, you need to approve the routes in the Tailscale admin UI.

- You will see a Subnets ! badge on the machine you set up. This indicates it is advertising routes but hasn't been approved.
- Click the ... next to the machine
- Click the checkbox and click save.
- Now the ! will be removed from the Subnets badge, indicating that the advertised routes are approved.

For your local devices to access the subnet routes advertised by the subnet router, you can also enable route acceptance via the CLI:

## Verify Connectivity

Run the verification script:

The endpoint and other details can be found in the Terraform outputs after deployment.

If you're running into issues at this point, head down to the Troubleshooting section to help figure out what might be wrong.

## Connect to Your RDS Instance

Once the verification passes, you can connect to your RDS instance directly from your local machine using standard PostgreSQL tools or any database client:

If you've never used Tailscale before, take a moment to familiarize yourself with the tailscale CLI and wrap your head around what's happening here. This is fantastic! We're routing traffic privately to our RDS instance from our local machine!

Similarly, you can now use this subnet router to route traffic from other devices in your Tailnet, including as a way to create a bridge between networks. Now we're ready to connect our Railway services! Let's do that next.

## Deploy Railtail into your project

Railtail is a project that will forward SOCK5 traffic for us RDS, because right now Railway containers don't allow privilege escalation. This way we can use private IPv6 networking to Railtail and forward our traffic privately to our AWS Subnet Router, which will then route to RDS.

- In a project where you want to bridge services privately to RDS, click the Create button in the upper right corner. Then select Template -> Type in RailTail.

You will need four variables to deploy Railtail and start bridging traffic to your RDS instance:

- **LISTEN_PORT**: This is the port that Railtail listens on to forward traffic. We like 41641, which is Tailscale's default UDP port for making peer-to-peer connections.
- **TARGET_ADDR**: The target address that Railtail will forward traffic to. In our case it should be tailscale-test-db.<subnet>.<region>.rds.amazonaws.com. You can grab this from the output of the terraform run we did earlier, or in the AWS console.
- **TS_AUTH_KEY**: The tailscale auth key we set up earlier. In the format: tskey-auth-0123456789
- **TS_HOSTNAME**: The friendly DNS name you can reference in your Tailnet. You can name this whatever you want. railtail or railtail-project-name is a good name here.

Click **Deploy Template**.

## Bridge Traffic to RDS

Now you can connect any service to your RDS backend. Add a variable to your connecting Service like: DATABASE_URL="postgresql://USERNAME:PASSWORD@${{railtail.RAILWAY_PRIVATE_DOMAIN}}:${{railtail.LISTEN_PORT}}/postgres"

That's it! Now you're bridging traffic privately from Railway to RDS.

<Image src="https://res.cloudinary.com/railway/image/upload/v1747163544/docs/tutorials/tailscale-subnet-router/railtail-to-rds_g10rrq.png"
alt="screenshot of railtail"
layout="intrinsic"
width={1544} height={533} quality={100} />

## Cleanup

When you're done with the tutorial, and so that AWS doesn't charge you money while your instances sit idle, you can destroy the resources you created automatically with:

## Troubleshooting

If you encounter issues with connectivity check the verify_tailscale_routing script included with the repository. You may be encountering:

1. **DNS Resolution**:

- Verify split DNS configuration in Tailscale.
- Check that the correct AWS DNS server IP is being used.

2. **Route Acceptance**:

- Ensure subnet routes are being advertised by the subnet router and that you've approve those routes in the Tailscale Admin Console.
- Verify your client is accepting routes with tailscale status.

3. **Database Connection Failures**:

- Check security group rules to ensure the subnet router can access RDS.
- Confirm you're using the correct credentials. (!IMPORTANT manage_master_user_password = false must be set or else the RDS module will ignore using your set password)

4. **Subnet Router Issues**:

- Check that IP forwarding on is enabled with cat /proc/sys/net/ipv4/ip_forward.
- Verify Tailscale is running with sudo systemctl status tailscaled.

## Additional Resources

- Tailscale: Subnet Routers
- Tailscale: AWS RDS
- Tailscale: High Availability
- AWS RDS PostgreSQL
- PgBouncer Documentation
- RDS Parameter List
- Terraform AWS VPC Provider
- Terraform AWS RDS Module Provider
- Tailscale Site-to-Site VPN Example (Terraform)
- Set Up a Tailscale Subnet Router on Railway

## Code Examples

# Set your AWS credentials
export AWS_ACCESS_KEY_ID=my-access-key
export AWS_SECRET_ACCESS_KEY=my-secret-key
# or with 1Password
export AWS_ACCESS_KEY_ID=$(op read op://vault-name/aws-personal-access-key/access_key_id)
export AWS_SECRET_ACCESS_KEY=$(op read op://vault-name/aws-personal-access-key/secret_access_key)

# Generate an SSH key for the EC2 instance if you don't have one
ssh-keygen -t rsa -b 2048 -f ~/.ssh/tailscale-rds

# Set your TailScale Auth Key
# terraform.tfvars
#...
tailscale_auth_key = "tskey-auth-1234567890"
# or with 1Password
tailscale_auth_key = $(op read op://vault-name/tailscale-auth-key/credential)

git clone git@github.com:echohack/rds-tailscale.git

aws_account = "your-aws-account-id"
rds_password = "your-secure-rds-password"
tailscale_auth_key = "tskey-your-tailscale-auth-key"

terraform init
terraform plan
terraform apply

tailscale set --accept-routes=true

./verify_tailscale_routing.sh <rds_endpoint> postgres <password> rds-tailscale

psql -h <rds_endpoint> -U postgres -d tailscale_test_db

terraform destroy -auto-approve


# Post-Deploy
Source: https://docs.railway.com/tutorials/github-actions-post-deploy

Learn how to use GitHub Actions to run post-deployment commands.

At Railway, we've set up Github triggers for automatic deployments when you push to a selected branch, and with Github Actions, you can automate several parts of your development workflow. Recently, within our Discord and Slack, we've had a couple of users ask us how they'd go about running commands or webhooks after their app is deployed so we thought it'd be a good idea to publish a short tutorial doing just that, with Github Actions.

## The Action

Since Railway makes the deployment status available to Github, we'll be using the deployment_status event to trigger our action. This event is triggered when a deployment status changes, and we'll be using the success state to trigger our action.

Make a new file in your repository called .github/workflows/post-deploy.yml and add the following -

If you have your repository deploying to multiple services, you can modify the if condition to check for the service you want to run the command for -

You can also see what github.event contains and build your own conditions from there.

Information on how to find the Service ID and Environment IDs as needed can be found here.

It's that simple! You can now customize the final run step to execute any commands or send webhooks using Curl or other methods of your choice.

## Conclusion

We hope this tutorial has been helpful and that you'll find it useful for your own projects. If you have any questions or feedback, please feel free to reach out to us on Discord, Slack or the Central Station. Happy coding!

## Code Examples

name: Post-Deployment Actions

on:
  deployment_status:
    states: [success]

jobs:
  post-deploy:
    runs-on: ubuntu-latest
    if: github.event.deployment_status.state == 'success'
    steps:
      - name: Debug - Print github.event object
        run: |
          echo "github.event context:"
          echo '${{ toJSON(github.event) }}'

      # Only run if this is a production environment deployment that succeeded
      - name: Run post-deploy actions
        if: github.event.deployment.environment == 'production'
        run: |
          echo "Production deployment succeeded"

if: github.event.deployment.environment == 'production' && github.event.deployment.payload.serviceId == '<service-id>'


# PR Environment
Source: https://docs.railway.com/tutorials/github-actions-pr-environment

Learn how to use the CLI in a GitHub Action to create environments for PRs

This can be useful if you need to create a branch on a Neon database, allowing you to automatically inject the correct database url.

## The Action

Make a new file in your repository called .github/workflows/railway-pr-envs.yml and add the following -

**Note:** if you are using a team project, you need to ensure that the token specified is scoped to your account, not a workspace.

This can very easily be modified to run commands in order to find variables and values, and can simply be passed as flags to the railway environment create command.

## Conclusion

We hope this tutorial has been helpful and that you'll find it useful for your own projects. If you have any questions or feedback, please feel free to reach out to us on Discord, Slack or the Central Station. Happy coding!

## Code Examples

# NOTE
# if you have 2fa on your account, the pr close part of the action will hang (due to 2fa not being supported non-interactively)

name: Manage PR environments (Railway)

on:
  pull_request:
    types: [opened, closed]

env:
  RAILWAY_API_TOKEN: "" # get this in account settings (make sure this is NOT a project token), and scope it to your account (not a workspace)
  SERVICE_ID: "" # service ID to inject database variable into
  ENV_NAME: "" # the environment variable name to inject (e.g DATABASE_URL)
  ENV_VALUE: "" # the value to inject
  DUPLICATE_FROM_ID: "" # railway environment to duplicate from
  LINK_PROJECT_ID: "" # project ID
  # TEAM_ID: "" if you are linking to a project in team, uncomment this

jobs:
  pr_opened:
    if: github.event.action == 'opened'
    runs-on: ubuntu-latest
    container: ghcr.io/railwayapp/cli:latest
    steps:
      - name: Link to project
        run: railway link --project ${{ env.LINK_PROJECT_ID }} --environment ${{ env.DUPLICATE_FROM_ID }} # --team ${{ env.TEAM_ID }} # uncomment this if you are linking to a team project
      - name: Create Railway Environment for PR
        run: railway environment new pr-${{ github.event.pull_request.number }} --copy ${{ env.DUPLICATE_FROM_ID }} --service-variable ${{ env.SERVICE_ID }} "${{ env.ENV_NAME }}=${{ env.ENV_VALUE }}"

  pr_closed:
    if: github.event.action == 'closed'
    runs-on: ubuntu-latest
    container: ghcr.io/railwayapp/cli:latest
    steps:
      - name: Link to project
        run: railway link --project ${{ env.LINK_PROJECT_ID }} --environment ${{ env.DUPLICATE_FROM_ID }} # --team ${{ env.TEAM_ID }} # uncomment this if you are linking to a team project
      - name: Delete Railway Environment for PR
        run: railway environment delete pr-${{ github.event.pull_request.number }} || true


# Self Hosted Runners
Source: https://docs.railway.com/tutorials/github-actions-runners

Learn how to deploy your own scalable self hosted GitHub Actions Runners on Railway. Build your own fleet of runners for your Enterprise and then scale your self-hosted runners with Railway replicas for blazing fast builds.

"
alt="screenshot of a deployment of a self hosted GitHub Actions runner on Railway"
layout="responsive"
width={1211} height={820} quality={100} />

Deploying GitHub Actions Self Hosted Runners on Railway is an excellent way to run your own CI infrastructure because you only pay for what you use. With self-hosted runners, you also unlock the ability to cache expensive and time-consuming dependencies (node_modules, cargo, etc.) or large git repositories. Best of all, Railway's built-in replicas means you can scale your runners horizontally, or even distribute them to different regions with just a click and redeploy. You'll save build times and costs over using standard runners, _AND_ you'll unlock more sophistocated workflows to streamline building your app.

In this guide you'll learn:

1. The basics to deploy a GitHub Actions Self Hosted Runner on Railway.
1. How to authenticate self-hosted runners on Railway with your GitHub Organization or Enterprise.
1. How to scale up replicas to serve bigger Actions workloads.
1. Best Practices for configuring your self-hosted runners on Railway.

**Quickstart:** Deploy your self-hosted Runners with our Railway template.

## Deploy a GitHub self-hosted runner on Railway

1. Navigate to the GitHub Actions self-hosted Runner Template. You'll notice the template requires an ACCESS_TOKEN. This token, along with our RUNNER_SCOPE will determine _where_ our self-hosted runners get registered on GitHub. Thankfully, this template supports self registration of your runners -- which means you can dynamically scale up or down the number of runners you have just by adjusting your replicas!

2. Set your RUNNER_SCOPE to org. We want to set up our self-hosted runners to register with a GitHub Organization, so any repositories within our organization can use the same pool of runners. This is super useful because you don't have to set up permissions for every single repository!

If you have a GitHub Enterprise, you can similarly set up your runners using an ACCESS_TOKEN, you just need to set your RUNNER_SCOPE as ent instead.

If you need additional configuration, then you can simply add a variable to your Service.

## Setup a GitHub ACCESS_TOKEN

For this guide, we will create a new GitHub Fine-Grained Personal Access Token. These are modern personal access tokens that obey the principle of least privilege, making them easy to secure, revoke, and audit!

**Note:** You need to have Admin access to the organization for which you are making the ACCESS_TOKEN.

<Image src="https://res.cloudinary.com/railway/image/upload/v1746477254/docs/github-actions/g9uzz9dksi80zsazlohk.png
"
alt="screenshot of a GitHub Fine Grained Access Token"
layout="responsive"
width={1131} height={702} quality={100} />

1. Create a new fine-grained personal access token. Navigate to your Settings -> Developer Settings -> Personal Access Token -> Fine-grained tokens -> Generate New Token
1. Set the Resource owner as your Organization. Alternatively, if you are using a ent RUNNER_SCOPE, select your Enterprise.
1. Set Expiration
1. Under Permissions, Select Organization Permissions -> Self Hosted Runners -> Read and Write (If Enterprise, select Enterprise instead).
1. Click Generate. Save your ACCESS_TOKEN in a safe place! You won't see it again. (Save it in a Password Vault as an API Key!)
1. DONE. You don't need any other permissions!

## Scaling up your Railway Self Hosted Runners

<Image src="https://res.cloudinary.com/railway/image/upload/v1746476747/docs/github-actions/edwass7m7pn35zx8xqw9.png
"
alt="screenshot of scaling up your Railway self hosted Runners with Railway Replicas"
layout="responsive"
width={1328} height={690} quality={100} />

1. Navigate to the Settings tab of your Service to the Region area.
1. Change the number next to your region from 1 to your desired number of replicas.
1. Click Deploy.
1. Done! Your new replicas will automatically spin up and register themselves with GitHub.

## View Your Registered Self Hosted Runners

<Image src="https://res.cloudinary.com/railway/image/upload/v1746477028/docs/github-actions/g0twzm5fhqrgjhtltrec.png
"
alt="screenshot of viewing your Registered self hosted runners"
layout="responsive"
width={1271} height={776} quality={100} />

You can view all your runners by navigating to your organization's Actions -> Runners page at https://github.com/organizations/(your-organization-name)/settings/actions/runners?page=1

## Routing Actions Jobs

You can route jobs by simply changing the LABELS variable. By default, we include the railway label on runners you make through the Template. LABELS is a comma (no spaces) delimited list of all the labels you want to appear on that runner. This enables you to route jobs with the specificity that your workflows need, while still allowing you to make runners available for your entire Organization.

## Setting up GitHub Actions workflows for Pull Requests

GitHub Actions uses workflow files located in .github/workflows/<workflow>.yml. You can easily incorporate pre-built steps to get up-and-running quickly.

- When you want to run a workflow every time a pull request is opened, set the on key to pull_request in your .github/workflows/<workflow>.yml.

- Set the runs-on key when you want to route your workflow job to a particular runner. Use a comma delimited list for greater specificity. For example, a [self-hosted, linux, x86, railway] workflow needs to match all labels to an appropriate runner in order to route the job correctly.

## Example GitHub Actions Workflow

If you've never made a workflow before, here is a basic out-of-the-box example of a NuxtJS project using Bun to execute an eslint check.

## Best Practices

1. **Only use private repositories and disable forks:** Make sure when using self-hosted runners, that you only attach them to private repositories. A known attack vector is for a malicious actor to fork a public repository and then exfiltrate your private keys from your self-hosted runners by executing workflows on them. Disabling forks can also mitigate this attack, and it's a good idea in general for locking down security on your repositories!

1. **Seal your ACCESS_KEY:** While all variables are encrypted on Railway, you can prevent prying eyes (including your future self) from ever viewing your API Key. Navigate to the Variables tab and next to the ACCESS_KEY variable click the three-dots-menu ... -> Seal. Make sure your ACCESS_KEY is stored in a secure Password Vault before doing this!

1. **Security Harden your self-hosted Runners:** Security Hardening will make your runners robust and prevent any concerns about your build infrastructure. GitHub's detailed guide can help you secure secrets, authentication, auditing, and managing your runners. Similarly dduzgun-security and Wiz both have excellent guides to securing your runners that are worth your time.

### Known Limitations

- Because Railway containers are non-privileged, GitHub Workflows that build-and-then-mount containers on the same host (i.e. Docker-in-Docker) will fail.

- Using the Serverless Setting on this Service is _not_ recommended and will result in idle runners disconnecting from GitHub and needing to reauthenticate. GitHub Runners have a 50 second HTTP longpoll which keeps them alive. While the runners in this template can automatically reauth with an ACCESS_TOKEN it will result in unnecessary offline / abandoned runners. If you want your runners to deauthenticate and spin down, consider using ephemeral runners instead.

### Troubleshooting self-hosted runner communication

> A self-hosted runner connects to GitHub to receive job assignments and to download new versions of the runner application. The self-hosted runner uses an HTTPS long poll that opens a connection to GitHub for 50 seconds, and if no response is received, it then times out and creates a new long poll. The application must be running on the machine to accept and run GitHub Actions jobs.

GitHub's documentation details all of the different endpoints your self-hosted runner needs to communicate with. If you are operating in a GitHub Allow List environment you must add your self-hosted runners IP Address to this allow list for communication to work.

If you are using a proxy server, refer to GitHub's documentation on configuring your self-hosted runner. You can simply add the required environment variables by adding them to the Variables tab of your Service.

### Cost Comparison

On Railway you only pay for what you use, so you'll find your GitHub workflows are significantly cheaper. For this guide we tested over ~2,300 1 minute builds on Railway self-hosted runners and our usage costs were $1.80 compared to GitHub's Estimated Hosted Runner cost of $18.40 for the same workload. Even better? We had 10x Railway replicas with 32 vCPU and 32GB RAM for this test, meaning that our actions workflows would never slow down.

On other platforms you pay for the _maximum available_ vCPUs and Memory. On Railway, you're only paying for usage, or in the below screenshot, the filled in purple area. This enables your workloads to still burst up to the _maximum available_ resources you have configured, with no tradeoffs on cost.

<Image src="https://res.cloudinary.com/railway/image/upload/v1746386242/docs/github-actions/urc6rirvsb3folwoqoml.png"
alt="screenshot of Railway's Observability dashboard demonstrating burstable usage of Memory"
layout="responsive"
width={1604} height={800} quality={100} />

## Code Examples

name: eslint check

on:
  pull_request:
    branches:
      - main

permissions:
  contents: read

jobs:
  build:
    name: Check
    runs-on: [self-hosted, railway]

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Install bun
        uses: oven-sh/setup-bun@v2

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Cache Files
        uses: actions/cache@v4
        with:
          path: |
            ~/.bun/install/cache
            path: ${{ github.workspace }}/**/node_modules
            path: ${{ github.workspace }}/**/.nuxt
          key: ${{ runner.os }}-bun-${{ hashFiles('**/bun.lock', 'nuxt.config.ts', 'app.config.ts', 'app.vue') }}

      - name: Install packages
        run: bun install --prefer-offline

      - name: Lint
        run: bun run lint



# Reference
Source: https://docs.railway.com/reference

# Application Failed to Respond
Source: https://docs.railway.com/reference/errors/application-failed-to-respond

Learn how to troubleshoot and fix the 'Application Failed to Respond' error.

alt="Screenshot of application failed to respond error"
layout="intrinsic"
width={1080} height={950}
quality={100} />

## What This Error Means

Seeing that your application failed to respond means that Railway's Edge Proxy cannot communicate with your application, causing your request to fail with a 502 (Bad Gateway) status code.

## Why This Error Can Occur

There are a few reasons why this error can occur, the most common being that your application is not listening on the correct host or port.

Another common reason is that your target port is set to an incorrect value.

In some far less common cases this error can also occur if your application is under heavy load and is not able to respond to the incoming request.

## Possible Solutions

The correct solution depends on the cause of the error.

### Target port set to the incorrect value

If your domain is using a target port, ensure that the target port for your public domain matches the port your application is listening on.

This setting can be found within your service settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743470803/docs/custom-port_r8vhbx.png"
alt="Screenshot showing target ports on a domain"
layout="intrinsic"
width={1200}
height={999}
quality={100}
/>

In the screenshot above, the domain was previously incorrectly configured with port 3000, when the application was actually listening on port 8080.

### Application Not Listening on the Correct Host or Port

Your web server should bind to the host 0.0.0.0 and listen on the port specified by the PORT environment variable, which Railway automatically injects into your application.

Start your application's server using:

- Host = 0.0.0.0
- Port = Value of the PORT environment variable provided by Railway.

**Below are some solution examples for common languages and frameworks.**

#### Node / Express

#### Node / Nest

#### Node / Next

Next needs an additional flag to listen on PORT:

#### Python / Gunicorn

gunicorn listens on 0.0.0.0 and the PORT environment variable by default:

#### Python / Uvicorn

uvicorn needs additional configuration flags to listen on 0.0.0.0 and PORT:

#### Go / net/http

This example is for net/http in the Go standard library, but you can also apply this to other frameworks:

### Application Under Heavy Load

If you think your application could be under heavy load, you can confirm this by checking the Metrics tab within your service panel.

For example, if you are running a Node.js application, and see that your vCPU usage has peaked at any point to around 1 vCPU, this is a good indication that your application is under heavy load given Node's single-threaded nature.

If this is the case, you can scale your application horizontally to handle more requests.

Horizontal scaling can easily be done by adding more instances to one or more regions.

## Code Examples

// Use PORT provided in environment or default to 3000
const port = process.env.PORT || 3000;

// Listen on `port` and 0.0.0.0
app.listen(port, "0.0.0.0", function () {
  // ...
});

// Use `PORT` provided in environment or default to 3000
const port = process.env.PORT || 3000;

// Listen on `port` and 0.0.0.0
async function bootstrap() {
  // ...
  await app.listen(port, "0.0.0.0");
}

next start --port ${PORT-3000}

gunicorn main:app

uvicorn main:app --host 0.0.0.0 --port $PORT

func main() {
  // ...
  // Use `PORT` provided in environment or default to 3000
  port := cmp.Or(os.Getenv("PORT"), 3000)

  log.Fatal(http.ListenAndServe((":" + port), handler))
  // ...
}


# No Start Command Could Be Found
Source: https://docs.railway.com/reference/errors/no-start-command-could-be-found

Learn how to troubleshoot and fix the 'No Start Command Could be Found' error.

Railway uses Nixpacks to analyze your application's files to generate a container image for your application.s

Seeing the No start command could be found error means that Nixpacks was unable to automatically find an appropriate start command for your application.

A start command is a command that will be executed by Railway to run your application.

## Why This Error Can Occur

By default, Railway uses Nixpacks to build and run your application. Nixpacks will try its best to find an appropriate start command for your application.

Some limited examples of start commands that Nixpacks will try are -

For Node based apps it will try to use npm start, yarn start, pnpm start, or bun start if a start script is present in your package.json file.

For Python apps it will try to use python main.py if a main.py file is present, or python manage.py migrate && gunicorn {app_name}.wsgi if a Django application is detected.

For Ruby apps it will try to use bundle exec rails server -b 0.0.0.0 if a Rails application is detected.

Failing the automatic detection, Nixpacks will return the No start command could be found error.

## Possible Solutions

Since Nixpacks was unable to find a start command, you will need to specify a start command yourself.

You can do this in the service settings under the Start Command field.

Some common start commands for various frameworks and languages are -

#### Node.js

Where main.js is the entry point for your application, could be index.js, server.js, app.js, etc.

#### Next.js

_Note: The --port flag is needed to ensure that Next.js listens on the correct port._

#### Nuxt.js

This will run Nuxt.js in production mode using its built-in Nitro server.

#### FastAPI

Where main is the name of the file that contains the app variable from FastAPI.

_Note: The --host and --port flags are needed to ensure that FastAPI listens on the correct host and port._

#### Flask

Where main is the name of the file that contains the app variable from Flask.

#### Django

Where myproject is the name of the folder that contains your wsgi.py file.

#### Ruby on Rails

_Note: The -b and -p flags are needed to ensure that Rails listens on the correct host and port._

#### Vite

_Note: The serve command is needed to serve the static site files and can be installed by running npm install serve locally._

#### Create React App

_Note: The serve command is needed to serve the static site files and can be installed by running npm install serve locally._

## Code Examples

node main.js

npx next start --port $PORT

node .output/server/index.mjs

uvicorn main:app --host 0.0.0.0 --port $PORT

gunicorn main:app

gunicorn myproject.wsgi

bundle exec rails server -b 0.0.0.0 -p $PORT

serve --single --listen $PORT dist

serve --single --listen $PORT build


# 405 Method Not Allowed
Source: https://docs.railway.com/reference/errors/405-method-not-allowed

Learn how to troubleshoot and fix the '405 Method Not Allowed' error.

This error is returned by your application when you attempt to make a POST request to your application, but the request is redirected to a GET request.

Depending on the application, this may result in your application returning either a 405 Method Not Allowed or a 404 Not Found status code.

Seemingly POST requests are being turned into GET requests.

## Why This Error Can Occur

This occurs because your request was made using HTTP. Railway will attempt to redirect your insecure request with a 301 Moved Permanently status code.

When an HTTP client encounters a 301 Moved Permanently redirect, the client will follow the redirect. However, according to the <a href="https://www.rfc-editor.org/rfc/rfc7231#section-6.4.2" target="_blank">HTTP/1.1 specifications</a>, the client will typically change the request method from POST to GET when it follows the redirect to the new URL.

## Solution

Ensure you are explicitly using https:// when calling your Railway-hosted services.

For example, if you are using curl to test your application, you should use the following command:

Notice the https:// prefix.

This ensures that the request is made using HTTPS, avoiding the 405 Method Not Allowed error that your application would otherwise return.

## Code Examples

curl -X POST https://your-app.railway.app/api


# Unable to Generate a Build Plan
Source: https://docs.railway.com/reference/errors/nixpacks-was-unable-to-generate-a-build-plan

Learn how to troubleshoot and fix the 'Nixpacks was unable to generate a build plan for this app' error.

Railway uses Nixpacks to analyze your application's files to generate a container image for your application.

Seeing the Nixpacks was unable to generate a build plan for this app error means that Nixpacks was unable to correlate your application's files with a supported build plan.

A build plan is a set of predefined instructions that Nixpacks uses to build and run your application on the Railway platform.

A list of supported build plans can be found here under the Language Support section.

## Why This Error Can Occur

This error can occur for a variety of reasons, here are some common ones and what the failed build logs could look like for each scenario -

- You are attempting to deploy a monorepo.

  Nixpacks doesn't know which directory you want to deploy from.

- Your application's files and or directory structure do not match any of the supported build plans.

  This is obviously Python, a supported language, but Nixpacks doesn't know exactly to do with just a web.py file since it was never explicitly programmed to handle this.

- Your application is using a language or framework that is not supported by Nixpacks.

  This is Nim, but unfortunately, Nixpacks doesn't have a build plan for Nim.

## Possible Solutions

### Try Railpack

If you're encountering issues with Nixpacks, consider switching to Railpack, Railway's default builder. Railpack provides better language support, smaller image sizes, and improved build performance. You can enable it in your service settings or by setting "builder": "RAILPACK" in your railway.json file.

### Monorepo Without Root Directory

If you are attempting to deploy a monorepo, you will need to set a root directory in your service settings under the source repository section.

For a comprehensive guide on how to deploy a monorepo, please refer to our Deploying a Monorepo guide.

### Unsupported Project Layout or Directory Structure

While you may be using a language or framework that is supported by Nixpacks, the project layout or directory structure of your application may not be natively supported.

For example, if you are using Python but Python was not automatically detected, you can write your own build plan.

In a nixpacks.toml file -

Of course, this is just an example, but you can see how you can write your own build plan to support your application.

Supported Languages (Providers) can be found here under the Language Support section.

If writing your own build plan is not an option, you can try to deploy your application using a Dockerfile.

### Language or Framework Not Supported

If you believe your application should be supported, please create an issue on the Nixpacks GitHub repository.

To unblock yourself, you can try to deploy your application using a Dockerfile.

If your project contains a Dockerfile Railway will automatically use it to build your application.

Read more about using a Dockerfile.

## Code Examples

The contents of the app directory are:

  /frontend
  /backend

The contents of the app directory are:

  web.py
  requirements.txt

The contents of the app directory are:

  main.nim
  nimble.nimble

providers = ["python"] # Tell Nixpacks to use the Python build plan

[start]
cmd = "python web.py" # Tell Nixpacks to start your web.py file


# ENOTFOUND redis.railway.internal
Source: https://docs.railway.com/reference/errors/enotfound-redis-railway-internal

Learn how to troubleshoot and fix the 'ENOTFOUND' redis.railway.internal error.

The error code ENOTFOUND means that your application could not resolve the redis.railway.internal hostname to an IP address when trying to connect to the Redis database.

## Why This Error Can Occur

This error can occur for a few different reasons, but the main reason is because your application uses the ioredis package to connect to the Redis database, or uses a package that uses ioredis as a dependency such as bullmq.

By default, ioredis will only do an IPv4 (A record) lookup for the redis.railway.internal hostname.

That presents a problem given that Railway's private network uses only IPv6 (AAAA records).

The lookup will fail because the A records for redis.railway.internal do not exist.

Some other reasons that this error can occur would be -

- Your application and Redis database are in different projects.

- You are trying to connect to a Redis database locally with the private hostname and port.

For either of these reasons, the issue arises because the private network is scoped to a single environment within a project, and would not be accessible from your local machine or other projects.

If the Redis database is in the same project as your application, and you are not trying to connect to a Redis database locally, ioredis is the likely cause of the error.

## Solutions

The solution depends on the package you are using to connect to the Redis database, though the solution is the same for both.

### ioredis

#### Using ioredis directly in your application

ioredis has an option to do a dual stack lookup, which will try to resolve the redis.railway.internal hostname using both IPv4 and IPv6 addresses (A and AAAA records).

To enable this, in your REDIS_URL environment variable, you can set the family to 0 to enable dual stack lookup.

#### Using bullmq

Similarly, for bullmq since it uses ioredis as a dependency, you can set the family option to 0 in your connection object.

#### Other packages

Above we covered the two most common packages that can cause this error, but there are other packages that use ioredis as a dependency that may also cause this error.

If you are using a package that uses ioredis as a dependency, you can try to find a way to set the family option to 0 either in your connection object or in your REDIS_URL environment variable. Similar to the examples above.

### Redis database in a different project

Create a new Redis database in the same project as your application, and connect it to the Redis database using the private network as shown in the examples above.

Read about best pracices to get the most out of the platform here.

### Connecting to a Redis database locally

The easiest way to connect to a Redis database locally is to use the public network.

You can do this is by using the REDIS_PUBLIC_URL environment variable to connect to the Redis database.

## Code Examples

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL + "?family=0");

const ping = await redis.ping();

import { Queue } from "bullmq";

const redisURL = new URL(process.env.REDIS_URL);

const queue = new Queue("Queue", {
  connection: {
    family: 0,
    host: redisURL.hostname,
    port: redisURL.port,
    username: redisURL.username,
    password: redisURL.password,
  },
});

const jobs = await queue.getJobs();

console.log(jobs);

import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_PUBLIC_URL);

const ping = await redis.ping();


# Databases
Source: https://docs.railway.com/reference/databases

Database services on Railway.

Databases can be deployed into a Railway project from a template, or by creating one through the service creation flow.

## How Database Services Work in Railway

Below are the core concepts to understand when working with databases in Railway.

#### Services

Railway services are containers deployed from a Docker Image or code repository, usually with environment variables defined within the service configuration to control the behavior of the service.

#### Volumes

When deploying a database service, data can be persisted between rebuilds of the container by attaching a Volume to the service.

#### TCP Proxy

To access a database service from outside the private network of a particular project, proxy traffic to the exposed TCP port by enabling TCP Proxy on the service.

## Database Templates

Many database templates are available to Railway users, which ease the process of deploying a database service.

### Railway-provided Templates

Railway provides several templates to provision some of the most popular databases out there. They also deploy with a helpful Database View.

Explore the guides in the How To section for information on how to use these templates -

- PostgreSQL
- MySQL
- MongoDB
- Redis

### Template Marketplace

Our <a href="https://railway.com/templates" target="_blank">Template Marketplace</a> includes many solutions for database services.

Here are some examples -

- Minio
- ClickHouse
- Dragonfly
- Chroma

## Support

Explore the Databases guide section for more information on how to get started using databases in Railway.


# Environments
Source: https://docs.railway.com/reference/environments

Understanding environments and their use cases in your Railway projects.



## How it Works

All projects in Railway are created with a production environment by default. Once a project has been created, new environments can be created and configured to complement any development workflow.

## Types of Environments

#### Persistent Environments

Persistent environments are intended to persist but remain isolated from production with regard to their configuration.

For example, it is a common pattern to maintain a staging environment that is configured to auto-deploy from a staging branch and with variables relevant to staging.

#### PR Environments

PR Environments are temporary. They are created when a Pull Request is opened on a branch and are deleted as soon as the PR is merged or closed.

## Environment Isolation

All changes made to a service are scoped to a single environment. This means that you can make changes to a service in an environment without affecting other environments.

## Use Cases

Environments are generally used for isolating changes from the production environment, to iterate and test before pushing to production.

- Have development environments for each team member that are identical to the
  production environment
- Have separate staging and production environments that auto-deploy when changes are made to different branches in a code repository.

## Support

Explore the Environments guide for more information on how to use and manage environments.


# Projects
Source: https://docs.railway.com/reference/projects

Projects are containers for environments and services in Railway.

If you are logged in, projects can be found on <a href="https://railway.com/dashboard" target="_blank">your project dashboard</a>.

## Project Canvas

<Image src="https://res.cloudinary.com/railway/image/upload/v1644620884/docs/ProjectPage_new_pa52tp.png"
alt="Screenshot of Project Canvas"
layout="responsive"
width={1377} height={823} quality={100} />

The project canvas is the default view for a project. Within it, a user can manage services and environments or select a service to view its configuration.

## Project Resources

- 100 GB outbound network bandwidth
- Ability to deploy multiple services
- Unlimited inbound network bandwidth
- Unlimited database services

## Project Visibility

Projects are private by default and only accessible to members of the project.

Projects can be made public, to be shared in a read-only state with anyone on the internet.

Public visibility is helpful for educators who want to show students how their projects look before a user deploys their own.

- Viewers don't need a Railway account to see the project
- Environment variables are private from viewers
- Services and Deployment logs are public

Find instructions for updating your project's visibility here.

## Project Transfers

Projects can be transferred to other users or to Teams, depending on subscription plan.

- Project transfers to other users are only allowed for users subscribed to the Hobby Plan (both the initiator and recipient of the transfer).

- Project transfers to Teams are only allowed for users who are Admin members of an existing Team. Teams are a feature of the Pro Plan.

Detailed instructions on how to transfer projects can be found here.


# Services
Source: https://docs.railway.com/reference/services

Discover the different types of services available in your Railway projects.

Each service keeps a log of deployment attempts and performance metrics.

Variables, source references (e.g. GitHub repository URI), and relevant start and build commands are also stored in the service, among other configuration.

## Types of Services

#### Persistent Services

Services that are always running. Examples include web applications, backend APIs, message queues, database services, etc.

#### Scheduled Jobs

Services that are run until completion, on a defined schedule, also called Cron Jobs.

## Service Source

A service source can be any of the following - Docker Image, GitHub or Local repository.

If a Dockerfile is found within the source repository, Railway will automatically use it to build an image for the service.

#### Docker Image

Services can be deployed directly from a Docker image from Docker Hub, GitHub Container Registry, GitLab Container Registry, or Quay.io. The images can be public or private.

#### GitHub Repository

Services can be connected to a GitHub repo and automatically deployed on each commit.

#### Local Repository

Services can be deployed from a local machine by using the Railway CLI.

## Ephemeral Storage

Every service deployment has access ephemeral storage, with the limits being 1GB on the Free plan and 100GB on a paid plan. If a service deployment consumes more than its ephemeral storage limit, it can be forcefully stopped and redeployed.

If your service requires data to persist between deployments, or needs more storage, you should add a volume.

## Templates

A template is a pre-configured group of services. A template can be used to start a project or to expand an existing project.

## Constraints

- Service names have a max length of 32 characters.


# Variables
Source: https://docs.railway.com/reference/variables

Variables provide a powerful way to manage configuration and secrets across services in Railway.



## How it Works

When defined, variables are made available to your application as environment variables in the following scenarios:

- The build process for each service deployment.
- The running service deployment.
- The command invoked by railway run <COMMAND>
- The local shell via railway shell

In Railway, there is also a notion of configuration variables which allow you to control the behavior of the platform.

## Template Syntax

Railway's templating syntax gives you flexibility in managing variables:

- NAMESPACE - The value for NAMESPACE is determined by the location of the variable being referenced. For a shared variable, the namespace is "shared". For a variable defined in another service, the namespace is the name of the service, e.g. "Postgres" or "backend-api".
- VAR - The value for VAR is the name, or key, of the variable being referenced.

You can also combine additional text or even other variables, to construct the values that you need:

## Types of Variables

In Railway, there is a notion of service variables, shared variables, reference variables, sealed variables, and a few kinds of reserved variables.

### Service Variables

Service variables are scoped to a specific service. They can be referenced in other services by using a Reference Variable.

### Shared Variables

Shared variables are scoped to a project and environment. They help reduce duplication of variables across multiple services within the same project.

### Reference Variables

Reference variables are those defined by referencing variables in other services, shared variables, or even variables in the same service. This is useful for ease of maintenance, allowing you to set a variable in a single place and reference it as needed.

Reference variables use Railway's template syntax.

### Sealed Variables

Sealed variables are scoped to a specific service. Once a variable is sealed, its value is not visible via the UI or the Railway API.

### Variable Functions

Template variable functions allow you to dynamically generate variables (or parts of a variable) on demand when the template is deployed.

### Railway-Provided Variables

Railway provides the following additional system environment variables to all
builds and deployments.

| Name                           | Description                                                                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_PUBLIC_DOMAIN        | The public service or customer domain, of the form example.up.railway.app                                                                          |
| RAILWAY_PRIVATE_DOMAIN       | The private DNS name of the service.                                                                                                                 |
| RAILWAY_TCP_PROXY_DOMAIN     | (see TCP Proxy for details) The public TCP proxy domain for the service, if applicable. Example: roundhouse.proxy.rlwy.net |
| RAILWAY_TCP_PROXY_PORT       | (see TCP Proxy for details) The external port for the TCP Proxy, if applicable. Example: 11105                             |
| RAILWAY_TCP_APPLICATION_PORT | (see TCP Proxy for details) The internal port for the TCP Proxy, if applicable. Example: 25565                             |
| RAILWAY_PROJECT_NAME         | The project name the service belongs to.                                                                                                             |
| RAILWAY_PROJECT_ID           | The project id the service belongs to.                                                                                                               |
| RAILWAY_ENVIRONMENT_NAME     | The environment name of the service instance.                                                                                                        |
| RAILWAY_ENVIRONMENT_ID       | The environment id of the service instance.                                                                                                          |
| RAILWAY_SERVICE_NAME         | The service name.                                                                                                                                    |
| RAILWAY_SERVICE_ID           | The service id.                                                                                                                                      |
| RAILWAY_REPLICA_ID           | The replica ID for the deployment.                                                                                                                   |
| RAILWAY_REPLICA_REGION       | The region where the replica is deployed. Example: us-west2                                                                                        |
| RAILWAY_DEPLOYMENT_ID        | The ID for the deployment.                                                                                                                           |
| RAILWAY_SNAPSHOT_ID          | The snapshot ID for the deployment.                                                                                                                  |
| RAILWAY_VOLUME_NAME          | The name of the attached volume, if any. Example: foobar                                                                                           |
| RAILWAY_VOLUME_MOUNT_PATH    | The mount path of the attached volume, if any. Example: /data                                                                                      |

### Git Variables

These variables are provided if the deploy originated from a GitHub trigger.

| Name                         | Description                                                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_GIT_COMMIT_SHA     | The git SHA of the commit that triggered the deployment. Example: d0beb8f5c55b36df7d674d55965a23b8d54ad69b |
| RAILWAY_GIT_AUTHOR         | The user of the commit that triggered the deployment. Example: gschier                                                                                                                             |
| RAILWAY_GIT_BRANCH         | The branch that triggered the deployment. Example: main                                                                                                                                            |
| RAILWAY_GIT_REPO_NAME      | The name of the repository that triggered the deployment. Example: myproject                                                                                                                       |
| RAILWAY_GIT_REPO_OWNER     | The name of the repository owner that triggered the deployment. Example: mycompany                                                                                                                 |
| RAILWAY_GIT_COMMIT_MESSAGE | The message of the commit that triggered the deployment. Example: Fixed a few bugs                                                                                                                 |

### User-Provided Configuration Variables

Users can use the following environment variables to configure Railway's behavior.

| Name                                  | Description                                                                                                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RAILWAY_DEPLOYMENT_OVERLAP_SECONDS  | How long the old deploy will overlap with the newest one being deployed, its default value is 0. Example: 20                                                              |
| RAILWAY_DOCKERFILE_PATH             | The path to the Dockerfile to be used by the service, its default value is Dockerfile. Example: Railway.dockerfile                                                        |
| NIXPACKS_CONFIG_FILE                | The path to the Nixpacks configuration file relative to the root of the app, its default value is nixpacks.toml. Example: frontend.nixpacks.toml                          |
| NIXPACKS_VERSION                    | The <a href="https://github.com/railwayapp/nixpacks/releases" target="_blank">version</a> of Nixpacks to use, if unspecfied a default version will be used. Example: 1.29.1 |
| RAILWAY_HEALTHCHECK_TIMEOUT_SEC     | The timeout length (in seconds) of healthchecks. Example: 300                                                                                                               |
| RAILWAY_DEPLOYMENT_DRAINING_SECONDS | The SIGTERM to SIGKILL buffer time (in seconds), its default value is 0. Example: 30                                                                                        |
| RAILWAY_RUN_UID                     | The UID of the user which should run the main process inside the container. Set to 0 to explicitly run as root.                                                             |
| RAILWAY_SHM_SIZE_BYTES              | This variable accepts a value in binary bytes, with a default value of 67108864 bytes (64 MB)                                                                                 |

## Support

For information on how to use variables refer to the Variables guide.

## Dockerfiles

For information on how to use variables in your Dockerfile refer to the Dockerfiles guide.

## Code Examples

${{NAMESPACE.VAR}}

DOMAIN=${{shared.DOMAIN}}
GRAPHQL_PATH=/v1/gql
GRAPHQL_ENDPOINT=https://${{DOMAIN}}/${{GRAPHQL_PATH}}


# Volumes
Source: https://docs.railway.com/reference/volumes

Volumes are a feature that enables persistent data for services on Railway.



## How it works

When mounting a volume to a service, a volume is made available to the service on the specified mount path.

## Size Limits

Volumes have a default size based on the subscription plan.

- Free and Trial plans: **0.5GB**
- Hobby plans: **5GB**
- Pro and team plans: **50GB**

Volumes can be "Grown" after upgrading to a different plan.

Pro users and above can self-serve to increase their volume up to 250 GB.

For Pro and above users, please reach out to us on our Central Station if you need more than 250GB. Enterprise users with $2,000/month committed spend can also use Slack.

## I/O Specifications

Volumes have the following I/O characteristics:

- **Read IOPS**: 3,000 operations per second
- **Write IOPS**: 3,000 operations per second

These specifications apply to all volume sizes and subscription plans.

## Pricing

Volumes are billed at a rate per GB / minutely, and invoiced monthly. You can find specific per-minute pricing here.

You are only charged for the amount of storage used by your volumes. _Each volume requires approx 2-3% of the total storage to store metadata about the filesystem, so a new volume will always start with some used amount of space used depending on the size._

## Backups

Services with volumes support manual and automated backups, backups are covered in the backups reference guide.

## Caveats

Here are some limitations of which we are currently aware:

- Each service can only have a single volume
- Replicas cannot be used with volumes
- There is no built-in S/FTP support
- To prevent data corruption, we prevent multiple deployments from being active
  and mounted to the same service. This means that there will be a small amount
  of downtime when re-deploying a service that has a volume attached, even if there is a healthcheck endpoint configured
- Down-sizing a volume is not currently supported, but increasing size is supported
- When resizing a volume, all deployments must be taken offline to prevent data
  corruption
- There is no file browser, or direct file download. To access your files,
  you must do so via the attached service's mount point
- Docker images that run as a non-root UID by default will have permissions issues when performing operations within an attached volume. If you are affected by this, you can set RAILWAY_RUN_UID=0 environment variable in your service.

## Support

Refer to the guide on how to use volumes for more details on how to use the feature.


# Functions
Source: https://docs.railway.com/reference/functions

Write and deploy code from the Railway canvas without managing infrastructure or creating a git repository.

Functions are Services that run a single file of TypeScript code using the Bun runtime.
Use them like any other Service, but without the overhead of a repository.

They are ideal for small tasks like handling webhooks, cron jobs, or simple APIs.

## Key features

- **Instant deploys**: Deploy code changes _in seconds_. No need to wait for a build step.
- **Import any NPM package**: Use any NPM package in your function. We will automatically install it for you when your code runs. Pin specific versions by using a package@version syntax in your imports, e.g. import { Hono } from "hono@4"
- **Use native Bun APIs**: Access Bun APIs like Bun.file() and Bun.serve().
- **Service variables**: Service Variables are automatically available in the function editor via import.meta.env, process.env, or Bun.env
- **Attach volumes**: Persist data in your function using Volumes.
- **Use Vim**: Enable Vim keybindings in the function editor by using the shortcut Cmd+Option+V on a Mac or Ctrl+Alt+V on Windows.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1738958871/docs/railway-functions-2_vk0umf.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={589} height={366} quality={80} />

## Limitations

- 1 file per function
- Max file size of 96KB

## Edit and Deploy

If you're familiar with VSCode or other IDEs, you'll feel right at home with our built-in editor.

- **To edit** your function, open the "Source Code" tab in your service.
- **To stage** your changes, press âŒ˜+S (or Control+S if using Windows).
- **To deploy** staged changes, press Shift+Enter.

## Versioning

Railway automatically versions your function code. Each time you deploy, a new version is created and is available for rollback.
To rollback or redeploy a previous version, find the Deployment you want to rollback to in the "Deployments" tab
of your service. Then click the "Redeploy" button.

You can find the source code of a previous deployment by opening the deployment details.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1738960017/docs/railway-functions-versions_jqdhal.png"
alt="Screenshot of pre-deploy command configuration"
layout="intrinsic"
width={588} height={499} quality={80} />


# App Sleeping
Source: https://docs.railway.com/reference/app-sleeping

Learn how Serverless reduces cost usage on Railway.

Serverless allows you to increase the efficiency of resource utilization on Railway and may reduce the usage cost of a service, by ensuring it is running only when necessary.

## How it Works

When Serverless is enabled for a service, Railway automatically detects inactivity based on outbound traffic.

#### Inactive Service Detection

Inactivity is based on the detection of any outbound packets, which could include network requests, database connections, or even NTP. If no packets are sent from the service for over 10 minutes, the service is considered inactive.

Some things that can prevent a service from being put to sleep -

- Keeping active database connections open, such as a database connection pooler.
- Frameworks that report telemetry to their respective services, such as Next.js.
- Making requests to other services in the same project over the private network.
- Making requests to other Railway services over the public internet.
- Making requests to external services over the public internet.
- Receiving traffic from other services in the same project over the private network.
- Receiving traffic from other Railway services over the public internet.
- Receiving traffic from external services over the public internet.

It's important to note that the networking graph in the metrics tab only displays public internet traffic. If you're using a private network to communicate with other services, this traffic won't appear in the metrics tab. However, it's still counted as outbound traffic and will prevent the service from being put to sleep.

#### Waking a Service Up

A service is woken when it receives traffic from the internet or from another service in the same project through the private network.

The first request made to a slept service wakes it. It may take a small amount of time for the service to spin up again on the first request (commonly known as "cold boot time").

## Caveats

- There will be a small delay in the response time of the first request sent to a slept service (commonly known as "cold boot times")
- For Railway to put a service to sleep, a service must not send _outbound_ traffic for at least 10 minutes. Outbound traffic can include telemetry, database connections, NTP, etc. Inbound traffic is excluded from considering when to sleep a service.
- Enabling Serverless will apply the setting across all Replicas
- Slept services still consume a slot on our infrastructure, enabling Serverless de-prioritizes your workload and in remote cases, may require a rebuild to re-live the service.

## Support

For information on how to enable Serverless on your services refer to the how to guide.


# Build and Start Commands
Source: https://docs.railway.com/reference/build-and-start-commands

Learn how to configure build and start commands.

If necessary, build and start commands can be manually configured.

## How it Works

Overrides are exposed in the service configuration to enable customizing the Build and Start commands. When an override is configured, Railway uses the commands specified to build and start the service.

#### Build Command

The command to build the service, for example yarn run build. Override the detected build command by setting a value in your service settings.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743192207/docs/build-command_bwdprb.png"
alt="Screenshot of Railway Build Command"
layout="responsive"
width={1200} height={373} quality={80} />

#### Start Command

Railway automatically configures the start command based on the code being deployed.

If your service deploys with a Dockerfile or from an image, the start command defaults to the ENTRYPOINT and / or CMD defined in the Dockerfile.

Override the detected start command by setting a value in your service settings.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1637798815/docs/custom-start-command_a8vcxs.png"
alt="Screenshot of custom start command configuration"
layout="intrinsic"
width={1302} height={408} quality={80} />

If you need to use environment variables in the start command for services deployed from a Dockerfile or image you will need to wrap your command in a shell -

This is because commands ran in exec form do not support variable expansion.

## Support

For more information on how to configure builds, check out the Builds guide section.

For more information on how to configure a service's deployment lifecycle, like the Start command, check out the Deployments guide section.

## Code Examples

/bin/sh -c "exec python main.py --port $PORT"


# Config as Code
Source: https://docs.railway.com/reference/config-as-code

Learn how to manage and deploy apps on Railway using config as code with toml and json files.

alongside your code. By default, we will look for a railway.toml or
railway.json file.

Everything in the build and deploy sections of the service
settings can be specified in this configuration file.

## How does it work?

When a new deployment is triggered, Railway will look for any config files in your
code and combine these values with the settings from the dashboard.

The resulting build and deploy config will be used **only for the current deployment**.

The settings in the dashboard will not be updated with the settings defined in
code.

Configuration defined in code will always override values from the
dashboard.

## Config Source Location

On the deployment details page, all the settings that a deployment went out with are shown. For settings that come from a configuration file, there is a little file icon. Hovering over the icon will show exactly what part of the file the values originated from.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743195106/docs/configuration_emrjth.png"
alt="Screenshot of Deployment Details Pane"
layout="responsive"
width={1200} height={631} quality={100} />

## Configurable Settings

### Specify the Builder

Set the builder for the deployment.

Possible values are:

- RAILPACK (default)
- DOCKERFILE
- NIXPACKS (deprecated)

Note: Railway will always build with a Dockerfile if it finds one. New services default to Railpack unless otherwise specified.

Read more about Builds here.

### Watch Patterns

Array of patterns used to conditionally trigger a deploys.

Read more about watch patterns here.

### Build Command

Build command to pass to the Nixpacks builder.

This field can be set to null.

Read more about the build command here.

### Dockerfile Path

Location of non-standard Dockerfile.

This field can be set to null.

More about building from a Dockerfile here.

### Railpack Version

Must be a valid Railpack version.

This field can be set to null.

You can also use the NIXPACKS_VERSION configuration
variable
to set the Nixpacks version.

### Nixpacks Config Path

Location of a non-standard Nixpacks config file. This setting only applies to services using the deprecated Nixpacks builder.

This field can be set to null.

### Nixpacks Plan

Full nixpacks plan. See the Nixpacks documentation for more info.

This field can be set to null.

You can also define specific options as follows.

In this example, we are adding ffmpeg to the setup phase.

#### Custom Install Command

Use nixpacksPlan to configure a custom install command.

### Nixpacks Version

Must be a valid Nixpacks version.

This field can be set to null.

You can also use the NIXPACKS_VERSION configuration
variable
to set the Nixpacks version.

### Start Command

The command to run when starting the container.

This field can be set to null.

Read more about the start command here.

### Pre-deploy Command

The command to run before starting the container.

This field can be omitted.

Read more about the pre-deploy command here.

### Multi-region Configuration

Horizontal scaling across multiple regions, with two replicas in each region.

This field can be set to null.

Read more about horizontal scaling with multiple regions here.

### Healthcheck Path

Path to check after starting your deployment to ensure it is healthy.

This field can be set to null.

Read more about the healthcheck path here.

### Healthcheck Timeout

Number of seconds to wait for the healthcheck path to become healthy.

This field can be set to null.

Read more about the healthcheck timeout here.

### Restart Policy Type

How to handle the deployment crashing.

Possible values are:

- ON_FAILURE
- ALWAYS
- NEVER

Read more about the Restart policy here.

### Restart Policy Max Retries

Set the max number of retries for the restart policy.

This field can be set to null.

Read more about the Restart policy here.

### Cron Schedule

Cron schedule of the deployed service.

This field can be set to null.

### Setting Environment Overrides

Configuration can be overridden for a specific environment by nesting it in a
environments.[name] block.

When resolving the settings for a deployment, Railway will use this priority order:

1. Environment specific config in code
2. Base config in code
3. Service settings

The following example changes the start command just in the production
environment.

#### PR Environment Overrides

Deployments for pull requests can be configured using a special pr environment. This configuration is applied only to deploys that belong to an ephemeral environment. When resolving the settings for a PR deployment, the following priority order is used:

1. Environment with the name of the ephemeral environment
2. Environment with the hardcoded name "pr"
3. Base environment of the pull request
4. Base config as code
5. Service settings

### Configuring a Build provider with Nixpacks

To define a build provider ahead of time, create a nixpacks.toml file and configure it like so:

### Deployment Teardown

You can configure Deployment Teardown settings to tune the behavior of zero downtime deployments on Railway.

#### Overlap Seconds

Time in seconds that the previous deploy will overlap with the newest one being deployed. Read more about the deployment's lifecycle here.

This field can be set to null.

#### Draining Seconds

The time in seconds between when the previous deploy is sent a SIGTERM to the time it is sent a SIGKILL. Read more about the deployment's lifecycle here.

This field can be set to null.

## Code Examples

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "builder": "RAILPACK"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "watchPatterns": ["src/**"]
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "buildCommand": "yarn run build"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "dockerfilePath": "Dockerfile.backend"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "railpackVersion": "0.7.0"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "nixpacksConfigPath": "backend_nixpacks.toml"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "nixpacksPlan": {
      "providers": ["python", "node"],
      "phases": {
        "install": {
          "dependsOn": ["setup"],
          "cmds": ["npm ci"]
        }
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "nixpacksPlan": {
      "phases": {
        "setup": {
          "nixPkgs": ["...", "ffmpeg"]
        }
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "nixpacksPlan": {
      "phases": {
        "install": {
          "dependsOn": ["setup"],
          "cmds": ["npm install --legacy-peer-deps"]
        }
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "build": {
    "nixpacksVersion": "1.29.1"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "startCommand": "node index.js"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "preDeployCommand": ["npm run db:migrate"]
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "multiRegionConfig": {
      "us-west2": {
        "numReplicas": 2
      },
      "us-east4-eqdc4a": {
        "numReplicas": 2
      },
      "europe-west4-drams3a": {
        "numReplicas": 2
      },
      "asia-southeast1-eqsg3a": {
        "numReplicas": 2
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "healthcheckPath": "/health"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "healthcheckPath": "/health",
    "healthcheckTimeout": 300
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "restartPolicyType": "ALWAYS"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "restartPolicyType": "ALWAYS",
    "restartPolicyMaxRetries": 5
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "cronSchedule": "*/15 * * * *"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "environments": {
    "staging": {
      "deploy": {
        "startCommand": "npm run staging"
      }
    }
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "environments": {
    "pr": {
      "deploy": {
        "startCommand": "npm run pr"
      }
    }
  }
}

providers = ["...", "python"]

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "overlapSeconds": "60"
  }
}

{
  "$schema": "https://railway.com/railway.schema.json",
  "deploy": {
    "drainingSeconds": "10"
  }
}


# Cron Jobs
Source: https://docs.railway.com/reference/cron-jobs

Learn how to run cron jobs on Railway.



## How it Works

Railway will look for a defined cron schedule in your service settings, and execute the start command for that service on the given schedule. The service is expected to execute a task, and exit as soon as that task is finished, not leaving any resources open, such as database connections. More on execution requirements below.

#### Scheduling Libraries

If you are already using a scheduling library or system in your service such as node-cron or Quartz, Railway cron jobs are a substitute of them that allows you to save resources between executions.

## Service Execution Requirements

Scheduled services should exit as soon as they are done with the task they are responsible to perform. Thus, the process should close any connections, such as database connections, to exit properly.

Currently, Railway does not automatically terminate deployments. As a result, if a previous execution is still running when the next scheduled execution is due, Railway will skip the new cron job.

## Crontab Expressions

A crontab expression is a scheduling format used in Unix-like operating systems to specify when and how often a command or script should be executed automatically.

Crontab expressions consists of five fields separated by spaces, representing different units of time. These fields specify the minute, hour, day of the month, month, and day of the week when the command should be executed.

The values of these fields can be an asterisk *, a list of values separated by commas, a range of values (using -), step values (using /) or an integer value.

#### Field Definitions

- **Minute (0-59)**: Represents the minute of the hour when the command should be executed. An asterisk (*) denotes any value, meaning the command will be executed every minute, or you can specify a specific minute value (e.g., 0, 15, 30).

- **Hour (0-23)**: Represents the hour of the day when the command should be executed. You can specify a specific hour value (e.g., 0, 6, 12), or use an asterisk (*) to indicate any hour.

- **Day of the month (1-31)**: Represents the day of the month when the command should be executed. You can specify a specific day value (e.g., 1, 15, 31), or use an asterisk (*) to indicate any day.

- **Month (1-12)**: Represents the month when the command should be executed. You can specify a specific month value (e.g., 1, 6, 12), or use an asterisk (*) to indicate any month.

- **Day of the week (0-7, where both 0 and 7 represent Sunday)**: Represents the day of the week when the command should be executed. You can specify a specific day value (e.g., 0-Sunday, 1-Monday, etc.), or use an asterisk (*) to indicate any day of the week.

Note that schedules are based on UTC (Coordinated Universal Time).

## Frequency

The shortest time between successive executions of a cron job cannot be less than 5 minutes.

## Examples

- Run a command every hour at the 30th minute: 30 * * * *

- Run a command every day at 3:15 PM: 15 15 * * *

- Run a command every Monday at 8:00 AM: 0 8 * * 1

- Run a command every month on the 1st day at 12:00 AM: 0 0 1 * *

- Run a command every Sunday at 2:30 PM in January: 30 14 * 1 0

- Run a command every weekday (Monday to Friday) at 9:30 AM: 30 9 * * 1-5

- Run a command every 15 minutes: */15 * * * *

- Run a command every 2 hours: 0 */2 * * *

- Run a command every 2nd day of the month at 6:00 AM: 0 6 2 * *

## FAQ

### When to use Railway's cron jobs?

- For short-lived tasks that complete quickly and exit properly, such as a daily database backup.
- When you want to save resources between task executions, as opposed to having an in-code scheduler run 24/7.

### When not to use Railway's cron jobs?

- For long-running processes that don't exit, such as a web server or discord bot.
- When you need more frequent execution than every 5 minutes.
- When you need absolute time precision. Railway does not guarantee execution times to the minute as they can vary by a few minutes.

### What time zone is used for cron jobs?

Cron jobs are scheduled based on UTC (Coordinated Universal Time).

You will need to account for timezone offsets when setting your cron schedule.

## Support

For information on how to configure cron jobs, refer to this guide.

## Code Examples

* * * * *
â”‚ â”‚ â”‚ â”‚ â”‚
â”‚ â”‚ â”‚ â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Day of the week (0 - 6)
â”‚ â”‚ â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Month (1 - 12)
â”‚ â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Day of the month (1 - 31)
â”‚ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Hour (0 - 23)
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Minute (0 - 59)


# Deployments
Source: https://docs.railway.com/reference/deployments

Deployments are attempts to build and deliver your service. Learn how they work on Railway.

All deployments will appear in the deployments view on your selected service.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1645148376/docs/deployment-photo_q4q8in.png"
alt="Screenshot of Deploy View"
layout="responsive"
width={1103} height={523} quality={80} />

## How it Works

Upon service creation, or when changes are detected in the service source, Railway will build the service and package it into a container with Railpack or a Dockerfile if present. If the source is a Docker Image, the build step is skipped.

Railway then starts the service using either the detected or configured Start Command.

This cycle represents a deployment in Railway.

## Deployment States

A comprehensive up to date list of statues can be found in Railway's GraphQL playground under DeploymentStatus (screenshot).

Deployments can be in any of the following states:

#### Initializing

Every Deployment in Railway begins as Initializing - once it has been accepted into our build queue, the status will change to Building.

#### Building

While a Deployment is Building, Railway will attempt to create a deployable Docker image containing your code and configuration (see Builds).

#### Deploying

Once the build succeeds, Railway will attempt to deploy your image and the Deployment's status becomes Deploying. If a healthcheck is configured, Railway will wait for it to succeed before proceeding to the next step.

#### Failed

If an error occurs during the build or deploy process, the Deployment will stop and the status will become Failed.

#### Active

Railway will determine the deployment's active state with the following logic -

- If the deployment **has** a healthcheck configured, Railway will mark the deployment as Active when the healthcheck succeeds.

- If the deployment **does not** have a healthcheck configured, Railway will mark the deployment as Active after starting the container.

#### Completed

This is the status of the Deployment when the running app exits with a non-zero exit code.

#### Crashed

A Deployment will remain in the Active state unless it crashes, at which point it will become Crashed.

#### Removed

When a new Deployment is triggered, older deploys in a Active, Completed, or a Crashed state are eventually removed - first having their status updated to Removing before they are finally Removed. Deployments may also be removed manually.

The time from when a new deployment becomes Active until the previous deployment is removed can be controlled by setting a RAILWAY_DEPLOYMENT_OVERLAP_SECONDS service variable.

## Deployment Menu

The deployment menu contains actions you can take on a deployment.

**Note:** Some actions are only available on certain deployment states.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1726503037/docs/redeploy_remove_deploy_jescm0.png"
  alt="Deployment Menu"
  width={1007}
  height={690}
  quality={80}
/>

#### View logs

Opens the deployment up to the corresponding logs, during build the build logs will be shown, during deploy the deploy logs will be shown.

#### Restart

Restarts the process within the deployment's container, this is often used to bring a service back online after a crash or if you application has locked up.

#### Redeploy

Redeploys the selected deployment.

This is often used to bring a service back online after -

- A crash.
- A usage limit has been reached and raised.
- Upgrading to Hobby when trial credits were previously depleted.
- Being demoted from Hobby to free and then upgrading again.

**Notes** -

- The redeploy will use the source code from the selected deployment.

- Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible.

#### Rollback

Redeploys the selected deployment.

**Notes** -

- The rollback will use the source code from the selected deployment.

- Deployments older than your plan's retention policy cannot be restored via rollback, and thus the rollback option will not be visible.

#### Remove

Stops the currently running deployment, this also marks the deployment as REMOVED and moves it into the history section.

#### Abort

Cancels the selected initializing or building deployment, this also marks the deployment as REMOVED and moves it into the history section.

## Ephemeral Storage

Every service deployment has access to 10GB of ephemeral storage. If a service deployment consumes more than 10GB, it can be forcefully stopped and redeployed.

If your service requires data to persist between deployments, or needs more than 10GB of storage, you should add a volume.

## Singleton Deploys

By default, Railway maintains only one deploy per service.

In practice, this means that if you trigger a new deploy either manually or automatically, the old version will be stopped and removed with a slight overlap for zero downtime.

Once the new deployment is online, the old deployment is sent a SIGTERM signal and given 3 seconds to gracefully shutdown before being forcefully stopped with a SIGKILL. We do not send any other signals under any circumstances.

The time given to gracefully shutdown can be controlled by setting a RAILWAY_DEPLOYMENT_DRAINING_SECONDS service variable.

## Railway Initiated Deployments

Occasionally, Railway will initiate a new deployment to migrate your service from one host to another. **This is primarily for your service's security and performance.**

We perform these migrations when implementing security patches or platform upgrades to the underlying infrastructure where your service was previously running. During platform-wide upgrades, your service might be redeployed multiple times as we roll out changes across our infrastructure. These deployments are mandatory and cannot be opted out of.

These Railway-initiated deployments will display with a banner above the Active deployment to clearly identify them.

## Deployments Paused - Limited Access

Railway's core offering is dynamic, allowing you to vertically or horizontally scale with little-to-no-notice. To offer this flexibility to customers, Railway takes the stance that Pro/Enterprise tiers may, in rare occasions, be prioritized above Free/Hobby tiers.

During periods where Pro/Enterprise users require additional resources, Railway may temporarily suspend resource allocation, including builds, to Free, and more rarely Hobby, customers.

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1749837403/CleanShot_2025-06-13_at_10.55.34_2x_ks2adh.png"
  alt="Limited Access indicator shown during high traffic periods"
  layout="responsive"
  width={1200}
  height={479}
  quality={100}
/>

### During a Pause

- You'll see a "Limited Access" indicator in your dashboard
- New deployments will be queued rather than immediately processed
- All other Railway features remain fully functional
- No data or existing deployments are affected

### Continue Deploying During High Traffic

If you need to deploy immediately during a high traffic pause, you can upgrade to the Pro plan to bypass the deployment queue. Pro tier customers are not affected by deployment pausing and can continue deploying normally during high traffic periods.

### When Normal Operations Resume

- Queued deployments will automatically process in order
- You'll receive a notification when deployment capabilities are restored
- No action is required on your part

## Support

For information on how to manage your deployments, explore the guides in this section.


# Deployment Regions
Source: https://docs.railway.com/reference/deployment-regions

Deploy your apps across multiple regions worldwide with Railwayâ€™s powerful infrastructure.

Consider factors like compliance needs and proximity to your users when choosing a region.

## Region Options

Railway has deploy regions in the Americas, Europe, and Asia-Pacific to provide broad coverage around the world.

Within the service settings, you can select one of the following regions -

| Name                 | Location               | Region Identifier        |
| -------------------- | ---------------------- | ------------------------ |
| US West Metal        | California, USA        | us-west2               |
| US East Metal        | Virginia, USA          | us-east4-eqdc4a        |
| EU West Metal        | Amsterdam, Netherlands | europe-west4-drams3a   |
| Southeast Asia Metal | Singapore              | asia-southeast1-eqsg3a |

_Additional regions may be added in the future as Railway continues expanding its infrastructure footprint._

**Note:** The region identifier is the value that can be used in your Config as Code file.

By default, Railway deploys to your preferred region, you can change this in your Account Settings.

All regions provide the same experience, performance, and reliability you expect from Railway.

## Impact of Region Changes

The region of a service can be changed at any time, without any changes to your domain, private networking, etc.

There will be no downtime when changing the region of a service, except if it has a volume attached to it (see below).

### Volumes

Volumes follow the region of the service to which they are attached.

If you change the region of a service with an attached volume, the volume will need to be migrated to the new region.

<Image
    quality={100}
    src="https://res.cloudinary.com/railway/image/upload/v1695660986/docs/volume_migrate_modal.png"
    alt="Volume"
    width={669}
    height={678}
/>

Note that this migration can take a while depending on the size of the volume, and will cause downtime of your service during that time.

<Image
    quality={100}
    src="https://res.cloudinary.com/railway/image/upload/v1695661106/docs/volume_migration.png"
    alt="Volume"
    width={732}
    height={483}
/>

The same is true if you attach a detached volume to a service in a different region. It will need to be migrated to the new region, which can take a while and cause downtime.


# Dockerfiles
Source: https://docs.railway.com/reference/dockerfiles

Learn Dockerfile configuration on Railway.



## How it works

When building a service, Railway will look for and use a Dockerfile at the root of the source directory.

**Note:** For the automatic Dockerfile detection to work, the Dockerfile must be named Dockerfile with a capital D, otherwise Railway will not use it by default.

Railway notifies you when it's using the Dockerfile in the build process with the following message in the logs:

## Support

For more information, refer to the guide on how to use Dockerfiles.

## Code Examples

==========================
Using detected Dockerfile!
==========================


# Healthchecks
Source: https://docs.railway.com/reference/healthchecks

Learn about healthchecks on Railway.



## How it Works

When a new deployment is triggered for a service, if a healthcheck endpoint is configured, Railway will query the endpoint until it receives an HTTP 200 response. Only then will the new deployment be made active and the previous deployment inactive.

#### Note About Continuous Monitoring

The healthcheck endpoint is currently **_not intended for continuous monitoring_** as it is only called at the start of the deployment, to ensure it is healthy prior to routing traffic to it.

If you are looking for a quick way to setup continuous monitoring of your service(s), check out the <a href="https://railway.com/template/p6dsil" target="_blank">Uptime Kuma template</a> in our template marketplace.

## Healthcheck Timeout

The default timeout on healthchecks is 300 seconds (5 minutes). If your application fails to serve a 200 status code during this allotted time, the deploy will be marked as failed.

This timeout is configurable in the service settings.

## Support

For information on how to configure healthchecks, click here.


# Backups
Source: https://docs.railway.com/reference/backups

Learn how Railway handles backups for volume contents to ensure data safety and recovery.



## How it works

When a volume is mounted to a service, backups can be manually created, deleted and restored. And they can also be scheduled to run on a Daily / Weekly / Monthly schedule.

## Backup Schedules

Backups can be scheduled to run on a daily, weekly or monthly basis. They will be kept for a number of days / months based on the schedule.

You can set the schedule in the service settings panel, under the Backups tab.

- **Daily** - Backed up every 24 hours, kept for 6 days
- **Weekly** - Backed up every 7 days, kept for 1 month
- **Monthly** - Backed up every 30 days, kept for 3 months

You can select multiple backup schedules for a single volume. These schedules can be modified at any time, and you can also manually trigger backups as needed.

## How to restore a backup

The available backups for a volume are listed in the attached service's Backups tab.

<Image src="https://res.cloudinary.com/railway/image/upload/v1737785142/docs/the-basics/backups_fdx09o.png"
alt="Screenshot of the service backups tab"
layout="responsive"
width={1365} height={765} quality={100} />

To restore a backup, first locate the backup you want to restore via its date stamp, then click the Restore button on the backup.

**Note:** Depending on the size of the backup, this may take a few seconds to a few minutes to complete.

Once completed, we will stage the change for you to review, click the Details button at the top of the project canvas to view the changes.

During this process, you will see a new volume mounted to the same location as the original volume, its name will be the date stamp of the backup.

The previous volume will be retained but has been unmounted from the service, it will have the original volume name such as silk-volume.

**Note:** Restoring a backup will remove any newer backups you may have created after the backup you are restoring, you will still have access to backups older than the one you are restoring.

If everything looks good and you're ready to proceed, click the Deploy button to complete the restore.

The changes will be applied and your service will be redeployed.

## Pricing

Backups are incremental and Copy-on-Write, we only charge for the data exclusive to them, that aren't from other snapshots or the volume itself.

You are only billed for the incremental size of the backup at a rate per GB / minutely, and invoiced monthly. Backups follow the same pricing as Volumes. You can find specific per-minute pricing here.

## Volume Backup Limits

Volume backups have size limitations based on the volume capacity:

- **Manual backups** are limited to 50% of the volume's total size
- This limitation applies to prevent backup operations from consuming excessive storage resources
- If your data exceeds this threshold, consider growing your volume capacity before creating backups or reaching out to support to raise the limit

## Caveats

Backups are a newer feature that is still under development. Here are some limitations of which we are currently aware:

- Backup incremental sizes are cached for a couple of hours when listed in the frontend, so they may show slightly stale data.
- Wiping a volume deletes all backups.
- Backups can only be restored into the same project + environment.


# Integrations
Source: https://docs.railway.com/reference/integrations

Discover Railwayâ€™s out-of-the-box integrations and how they enhance your development process.



## Project Tokens

Project tokens can be used in environments where you cannot login (e.g. remote
servers or CI). You can create project tokens for a specific Railway
environment on the project page.

<Image src="https://res.cloudinary.com/railway/image/upload/v1644622499/docs/projecttokens_lwjgat.png"
alt="Screenshot of Project Canvas"
layout="responsive"
width={1377} height={823} quality={100} />

Project tokens allow the CLI to access all the environment variables associated
with a specific project and environment. Use the token by setting the
RAILWAY_TOKEN environment variable and then running railway run.

## Serverless Platforms

### Vercel

Use the <a href="https://vercel.com/changelog/railway-integration-postgres-redis-mysql" target="_blank">Railway Vercel
integration</a> to provide your production and preview deployments with access to your Railway
environments.

You can enable this integration in your project dashboard by connecting
to your Vercel account, specify a team, project, and production/preview
environments. We will then provide your production and preview deployments on Vercel
with all the environment variables needed to connect to your Railway
environments.

This allows you to keep production and preview deployment databases separate.

### Other Platforms

We are working on adding more integrations to various serverless platforms.
However, if you want to use Railway for a platform we do not support, you can
manually add the environment variables for any of your services (e.g. the DATABASE_URL
for Postgres) to the serverless platform.

## GitHub Integration

Railway supports GitHub personal or organizational repos, provided the Railway app is given the correct permissions.

### Railway Deployment Checks

GitHub Commits have a status check to indicate the status of the Railway build. This applies for both PRs and all commits that auto deploy to Railway.

## Doppler Secrets Management

It's common for developers to store secrets in environment variables. However, this can be a security risk if you accidentally commit your secrets to a public repository. To avoid this, you can use a secrets management tool to store your secrets in a secure location. Railway supports Doppler as a secrets management tool. You can use Doppler to manage your Railway environment variables using the Railway Integration that Doppler provides.

You can get instructions on how to use Doppler with Railway on the <a href="https://docs.doppler.com/docs/railway" target="_blank">Doppler Docs
integration</a>.

## Code Examples

RAILWAY_TOKEN=XXXX railway run


# Railpack
Source: https://docs.railway.com/reference/railpack

Railway uses Railpack to build and deploy your code with zero configuration.

build and deploy your code with zero configuration.

## Supported Languages

Currently, we support the following languages out of the box:

- Node
- Python 
- Go
- PHP
- HTML/Staticfile
- Java
- Ruby
- Deno
- Rust
- Elixir
- Shell scripts

## How it Works

Railpack automatically analyzes your code and turns it into a container image.
It detects your programming language, installs dependencies, and configures
build and start commands without any manual configuration required.

## The Build Process

When Railway builds your app with Railpack, the build process will
automatically:

1. **Analyze** your source code to detect the programming language and framework
2. **Install** the appropriate runtime and dependencies
3. **Build** your application using detected or configured build commands
4. **Package** everything into an optimized container image

## Configuration

Railpack works with zero configuration, but you can customize the build process
when needed using environment variables
or a Railpack config file.

## Support

If you have a language or feature that you want us to support, please don't
hesitate to reach out on <a href="https://discord.gg/xAm2w6g"
target="_blank">Discord</a> or on the <a
href="https://github.com/railwayapp/railpack">Railpack repo</a>.


# Nixpacks
Source: https://docs.railway.com/reference/nixpacks

Railway uses Nixpacks to build and deploy your code with zero configuration.

Nixpacks is deprecated and no longer receiving new features. New services automatically use Railpack. 
Existing services will continue to work with Nixpacks. To migrate to Railpack, update your service settings.
</DeprecationBanner>

Railway uses <a href="https://nixpacks.com/docs" target="_blank">Nixpacks</a> to build and deploy your code with
zero configuration. This documentation is maintained for existing services using Nixpacks. For new services, we recommend using Railpack.

## Supported Languages

Currently, we support the following languages out of the box:

- Bun (Experimental)
- Clojure
- Cobol
- Crystal
- C#/.NET
- Dart
- Deno
- Elixir
- F#
- Gleam
- Go
- Haskell
- Java
- Lunatic
- Node
- PHP
- Python
- Ruby
- Rust
- Scheme
- Staticfile
- Swift
- Scala
- Zig

## The Build Table / Build Plan

When Railway builds your app with Nixpacks a Build Plan will be printed **at the top** of the build logs.

This table displays a list of packages and commands that will be used in the build (and start) process for your application.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1722994637/docs/build_table_j6izfy.png"
alt="nixpacks build table"
layout="responsive"
width={1365} height={790} quality={80} />

## Support

If you have a language or feature that you want us to support, please don't hesitate to
reach out on <a href="https://discord.gg/xAm2w6g" target="_blank">Discord</a> or on the <a href="https://github.com/railwayapp/nixpacks/discussions/245" target="_blank">Nixpacks repo</a>.


# Private Networking
Source: https://docs.railway.com/reference/private-networking

Learn everything about private networking on Railway.



## How it works

Under the hood, Railway is using encrypted Wireguard tunnels to create an IPv6 mesh network between all services within an environment. This allows traffic to route between services without exposing ports publicly.

**Note: You cannot use private networking to communicate with services in other environments.**

### Internal DNS

Every service in a project and environment gets an internal DNS name under the railway.internal domain that resolves to the internal IP address of the service.

This allows communication between services in an environment without exposing any ports publicly. Any valid IPv6 traffic is allowed, UDP, TCP and HTTP.

<Image src="https://res.cloudinary.com/railway/image/upload/v1686946888/docs/CleanShot_2023-06-16_at_16.21.08_2x_lgp9ne.png"
alt="Preview of What The Guide is Building"
layout="intrinsic"
width={1310} height={420} quality={100} />

## Caveats

During the feature development process we found a few caveats that you should be aware of:

- Private networking is not available during the build phase.
- You will need to bind to a IPv6 port to receive traffic on the private network.
- We don't support IPv4 private networking.
- Private networking does not function between environments.

## Support

For information on how to use Private Networking, check out this guide.


# Public Networking
Source: https://docs.railway.com/reference/public-networking

Learn everything about public networking on Railway.



## How it Works

Railway can detect if a deployed service is listening for traffic. When detected, Railway will provide a public domain for your service with the click of a button. The only thing you need to do, is properly handle the port assignment. More on this in the Public Networking guide.

If you have your own Domain already, Railway also supports adding custom domains to your services. For instructions on adding a custom domain, see the Public Networking guide.

## Technical Specifications

_This information is subject to change at any time._

| Category                 | Key Information                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DNS/Domain Names**     | - Support for domains, subdomains, and wildcard domains.<br/>- Subdomains and wildcards cannot overlap (foo.hello.com cannot exist with *.hello.com unless owned by the same service).<br/>- Root domains need a DNS provider with ALIAS records or CNAME flattening.<br/>- Unicode domains should be PUNYcode encoded.<br/>- Non-public/internal domain names are not supported.                                                          |
| **Certificate Issuance** | - Railway attempts to issue a certificate for **up to 72 hours** after domain creation before failing.<br/>- Certificates are expected to be issued within an hour.                                                                                                                                                                                                                                                                            |
| **TLS**                  | - Support for TLS 1.2 and TLS 1.3 with specific cipher sets.<br/>- Certificates are valid for 90 days and renewed every 30 days.                                                                                                                                                                                                                                                                                                               |
| **Edge Traffic**         | - Support for HTTP/1.1.<br/>- Support for websockets over HTTP/1.1.<br/>- Proxy Keep-Alive timeout of 60 seconds (1 minute).<br/>- Max 32 KB Combined Header Size<br/>- Max duration of 15 minutes for HTTP requests.                                                                                                                                                                                                                          |
| **Request Headers**      | - X-Real-IP for identifying client's remote IP.<br/>- X-Forwarded-Proto always indicates https.<br/>- X-Forwarded-Host for identifying the original host header.<br/>- X-Railway-Edge for identifying the edge region that handled the request.<br/>- X-Request-Start for identifying the time the request was received (Unix milliseconds timestamp).<br/>- X-Railway-Request-Id for correlating requests against network logs. |
| **Requests**             | - Inbound traffic must be TLS-encrypted<br/>- HTTP GET requests to port 80 are redirected to HTTPS.<br/>- HTTP POST requests to port 80 are redirected to HTTPS as GET requests.<br/>- SNI is required for correct certificate matching.                                                                                                                                                                                                       |

## Domain Rate Limits

_This information is subject to change at any time._

To ensure the integrity and performance of our network, we enforce the following limits for all services.

| Category                    | Limit                         | Description                                               |
| --------------------------- | ----------------------------- | --------------------------------------------------------- |
| **Maximum Connections**     | 10,000 concurrent connections | The number of concurrent connections.                     |
| **HTTP Requests/Sec**       | 3,000 RPS                     | The number of HTTP requests to a given domain per second. |
| **Requests Per Connection** | 10,000 requests               | The number of requests each connection can make.          |

If your application requires higher limits, please don't hesitate to reach out to us at team@railway.com.

## Custom Domain Count Limits

The Hobby plan is limited to 2 custom domains per service.

The Pro Plan is limited to 20 domains per service by default but can be increased for Pro users on request, by reaching out to us at team@railway.com or via private thread.

## FAQ

<Collapse title="What type of traffic can I send to my services in Railway?">
We currently support HTTP and HTTP2 traffic from the internet to your services.

All traffic must be HTTPS and use TLS 1.2 or above, and TLS SNI is mandatory for requests.

- Plain HTTP GET requests will be redirected to HTTPS with a 301 response.
- Plain HTTP POST requests will be converted to GET requests.

For services that require TCP traffic, like databases, we also have a TCP Proxy feature.
</Collapse>

<Collapse title="How does Railway handle SSL certificates?">
We provide LetsEncrypt SSL certificates using RSA 2048bit keys.  Certificates are valid for 90 days and are automatically renewed 2 months into their life.

Certificate issuance should happen within an hour of your DNS being updated with the values we provide.

For proxied domains (Cloudflare orange cloud), we may not always be able to issue a certificate for the domain, but Cloudflare to Railway traffic will be encrypted with TLS using our default *.up.railway.app certificate.
</Collapse>

<Collapse title="Does Railway protect my services against DDoS?">
Railway Metal infrastructure is built to mitigate attacks at network layer 4 and below, however we do not provide protection on the application layer. If you need WAF functionality, we recommend using Cloudflare alongside Railway.
</Collapse>

<Collapse title="How do I handle forwarding traffic to my exposed port?">
To have traffic from the public internet properly forwarded to your service's exposed port, you must ensure that you are properly using the PORT environment variable made available to every service deployment.
- If your application is listening on an explicitly defined port, you must define a PORT variable with the proper assignment in your service's variables.
- If you do not explicitly define the PORT, Railway provides one for you and exposes it during deployment.

More on this in the Public Networking guide.
</Collapse>


# Outbound Networking
Source: https://docs.railway.com/reference/outbound-networking

Learn about outbound networking features and email delivery options on Railway.



## Email Delivery

SMTP is only available on the Pro plan and above.

Free, Trial, and Hobby plans must use transactional email services with HTTPS APIs. SMTP is disabled on these plans to prevent spam and abuse. However, even when SMTP is available, we recommend transactional email services with HTTPS APIs for all plans due to their enhanced features and analytics.

<Banner variant="info">Upon upgrading to Pro, please re-deploy your service that needs to use SMTP for the changes to take effect.</Banner>

### Email Service Examples

Here are examples of transactional email services you can use:

**Note:** These services are required for Free, Trial, and Hobby plans since outbound SMTP is disabled.

- Resend - **Railway's recommended approach**
- SendGrid
- Mailgun
- Postmark

These services provide detailed analytics and robust APIs designed for modern applications. They also work on all Railway plans since they use HTTPS instead of SMTP.

### Debugging SMTP Issues

If you are experiencing issues with SMTP on the Pro plan, please the follow the steps below to help us diagnose the problem:

1. First, ensure that you have tried re-deploying your service

2. SSH into your service using the Railway CLI:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757952518/docs/smtp-copy-ssh_qtczce.png"
alt="Screenshot of SSH into your service"
layout="responsive"
width={767} height={729} quality={100} />

3. Copy-paste this command and change the SMTP_HOST to the host you're trying to connect to:

4. Execute the command. You should see output similar to this:

Example:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1757952876/docs/smtp-exec-cmd_ytqx7u.png"
alt="Screenshot of executing debug command"
layout="responsive"
width={767} height={729} quality={100} />

Replace smtp.resend.com above with your SMTP host.

5. If any of the ports are unreachable, please contact your email provider to
ensure that they are not blocking connections from Railway's IPs. Port 2525 is
a non-standard SMTP port that may be blocked on popular email providers, so
2525 being unreachable is not an issue

6. Otherwise, please reach out to us at Central Station
and share the output of the command for further assistance

## Static Outbound IPs

Railway offers Static Outbound IPs for Pro plan customers who need consistent IP addresses for firewall whitelisting or third-party integrations.

## Outbound IPv6

Railway does not currently support outbound IPv6. Any IPv6 request will fail showing "Network is unreachable" or ENETUNREACH.

## Related Features

- Static Outbound IPs - Assign permanent outbound IP addresses
- Private Networking - Internal service communication
- Public Networking - Inbound traffic to your services

## Code Examples

SMTP_HOST="$REPLACE_THIS_WITH_YOUR_SMTP_HOST" bash -c '
for port in 25 465 587 2525; do
  timeout 1 bash -c "</dev/tcp/$SMTP_HOST/$port" 2>/dev/null && \
    echo "$SMTP_HOST port $port reachable" || \
    echo "$SMTP_HOST port $port unreachable"
done
'

smtp.yourhost.com port 25 reachable
smtp.yourhost.com port 465 reachable
smtp.yourhost.com port 587 reachable
smtp.yourhost.com port 2525 reachable


# Static Outbound IPs
Source: https://docs.railway.com/reference/static-outbound-ips

Learn how to enable static outbound IPs on Railway.



## Use Cases

This feature may be useful to you if you're using a third-party service provider or firewall which requires you to whitelist which IP addreseses your services will be connecting from, such as MongoDB Atlas.

The IPv4 address assigned to your service through this feature **cannot** be used to receive inbound traffic.

## Enabling Static Outbound IPs

Customers on the Pro plan can enable Static Outbound IPs for any service they wish.

1. Navigate to the Settings tab of your desired service
2. Toggle Enable Static IPs in the Networking section of Settings
3. You will be presented with an IPv4 address which is tied to the region your service is deployed in
4. The Static IP will be used by your service after the next deploy

<Image
  src="https://res.cloudinary.com/railway/image/upload/v1716858865/docs/d6u20lrvxmlc8rfu91rx.png"
  layout="responsive"
  alt="Static IPs"
  width={1328} height={710} quality={80} />

## Caveats

- There is no guarantee that the IPv4 address assigned to your service is dedicated. It may be shared with other customers.
- The IP address cannot be used for inbound traffic.
- If you wish to move your service to a different region, the IP address will change.


# Scaling
Source: https://docs.railway.com/reference/scaling

Learn how to scale your applications on Railway.



## How it Works

### Vertical Autoscaling

By default Railway will scale your service up to the specified vCPU and Memory limits of your plan.

### Horizontal Scaling with Replicas

Scale horizontally by manually increasing the number of replicas for a service in the service settings. Increasing the number of replicas on a service will create multiple instances of the service deployment.

Each replica has access to the full resources allocated by your plan. For instance, with the Pro plan, each of your replicas can utilize up to 32 vCPU and 32GB of memory, for example, if you had 2 replicas, your service would be able to utilize up to 64 vCPU and 64GB of memory split between the 2 replicas.

#### Multi-region replicas

Multi-region replicas are exactly as advertised -- horizontally scaled replicas that are located in different geographic regions.

The service settings panel will reveal an interface for assigning replicas to different regions.

<Image 
    src="https://res.cloudinary.com/railway/image/upload/v1733386054/multi-region-replicas_zov7rv.png"
    alt="Multi-region replicas"
    layout="responsive"
    width={1370}
    height={934}
/>

Creating, deleting, and re-assigning replicas will trigger a staged change which upon applying will trigger a redeploy.

#### Load Balancing Between Replicas

If you are using multi-region replicas, Railway will automatically route public traffic to the nearest region and then randomly distribute requests to the replicas within that region.

If you are using a single region with multiple replicas, Railway will randomly distribute public traffic to the replicas of that region.

We plan to add more advanced load balancing strategies in the future.

#### Metrics

For services with multiple replicas, the metrics from all replicas are summed up and displayed in the metrics tab, for example, if you have 2 replicas, each using 100 MB of memory, the memory usage displayed in the metrics tab will be 200 MB.

#### Sticky Sessions

For now Railway does not support sticky sessions nor report the usage of the replicas within the metrics view.

## Support

For information on how to use horizontal scaling with replicas, refer to this guide.


# TCP Proxy
Source: https://docs.railway.com/reference/tcp-proxy

Learn how to proxy TCP traffic to a service by creating a TCP proxy on Railway.



## How it works

Enabling TCP Proxy on a service requires specification of a port to which the traffic should be proxied. Railway then generates a domain and proxy port, and all traffic sent to domain:port will be proxied to the service.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743194081/docs/tcp-proxy_edctub.png"
alt="Screenshot of TCP proxy configuration"
layout="responsive"
width={1200} height={822} quality={100} />

#### Load Balancing

Currently we use a random load balancing strategy for TCP traffic.

## Use Cases

TCP Proxy is useful for services that don't support HTTP, such as databases.

## Support

For more information on how to set it up, refer to the TCP Proxy section of the Public Networking guide.


# Logging
Source: https://docs.railway.com/reference/logging

Learn about log retention on Railway.



## How it Works

Any build or deployment logs emitted to standard output or standard error (
eg. console.log(...)) are captured by Railway to be viewed or searched later.

## Log Retention

Depending on your plan, logs are retained for a certain amount of time.

| Plan          | Retention\*   |
| ------------- | ------------- |
| Hobby / Trial | 7 days        |
| Pro           | 30 days       |
| Enterprise    | Up to 90 days |

_\* Upgrading plans will immediately restore logs that were previously
outside of the retention period._

## Logging throughput

To maintain quality of service for all users, Railway enforces a logging rate limit of **500 log lines per second per <a href="/reference/scaling#horizontal-scaling-with-replicas" target="_blank">replica</a>** across all plans. When this limit is exceeded, additional logs are dropped and you'll see a warning message like this:

If you encounter this limit, here are some strategies to reduce your logging volume:

- Reduce log verbosity in production
- Use structured logging with minimal formatting (e.g., minified JSON instead of pretty-printed objects)
- Implement log sampling for high-frequency events
- Conditionally disable verbose logging based on the environment
- Combine multiple related log entries into single messages

## Viewing Logs

For information on how to view logs, head over to the guide for using logs.

## Code Examples

Railway rate limit of 500 logs/sec reached for replica, update your application to reduce the logging rate. Messages dropped: 50


# Metrics
Source: https://docs.railway.com/reference/metrics

Discover resource usage for your services on Railway via the Metrics tab.



## How it Works

For each service, Railway captures metric data. These metrics are then made available in graphs within a service's panel, under the metrics tab.

## Metrics with multiple replicas

When a service runs multiple replicas, you can view metrics in two ways: **Sum** or **Replica**.

_Note: Public network traffic metrics are only available in the Sum view._

### Sum view

!Viewing the sum of all replica metrics

In **Sum** view, metrics from all replicas are combined. For example, if you have two replicas using 100 MB of memory each, the metrics tab will show 200 MB.

### Replica view

!Viewing metrics of individual replicas

In **Replica** view, you can see metrics for each replica individually. This is useful for diagnosing issues with specific replicas or spotting if some regions are under- over overutilized.

The total from all replicas may differ slightly from the Sum view due to rounding or overlapping instances during zero-downtime deployments.

## Provided Metrics

The following metrics are provided:

- CPU
- Memory
- Disk Usage
- Network

## Viewing Metrics

For information on how to view and read metrics, visit this guide.


# Webhooks
Source: https://docs.railway.com/reference/webhooks

Learn about webhooks on Railway.

<Image src="https://res.cloudinary.com/railway/image/upload/v1743196876/docs/new-webhook_lrfxxa.png"
alt="New Webhook UI"
layout="responsive"
width={1200} height={754} quality={80} />

## Setting up a Project webhook

For information on how to setup webhooks, visit this guide.

## Deployment Status

When a deployment's status changes, Railway will send a notification via HTTP to the URL provided in the webhook configuration.

Deployment states can be found here.

## Volume Usage Alerts

When a volume usage breaches certain thresholds, Railway will send a notification to pro customers via HTTP to the URL provided in the webhook configuration.

The thresholds that alert can be configured in the volume settings page.

## Muxers: Provider-specific Webhooks

Webhooks contain Muxers which will automatically transform the payload based on the webhook URL. Below are the currently supported Muxers:

- Discord
- Slack

For more information, visit this guide.


# Accounts
Source: https://docs.railway.com/reference/accounts

Learn about Railway Accounts

Users are only allowed one account per person. This is enforced through email, GitHub, and payment method verification.

## Account Settings

<Image src="https://res.cloudinary.com/railway/image/upload/v1743471483/docs/account-settings_najujk.png"
alt="Screenshot of Account Navigation"
layout="responsive"
width={1200} height={857} quality={80} />

The account settings page is accessible by clicking the profile photo in the top right and selecting <a href="https://railway.com/account" target="_blank">Account Settings</a>.

### Account Information

Accounts can change their display name, profile photo, and account email under <a href="https://railway.com/account" target="_blank">Account Settings</a>.

### Deleting an Account

Selecting "Delete Account" at the bottom of the <a href="https://railway.com/account" target="_blank">Account Settings</a> page will delete an account. All data related to the account will be deleted.

After a successful confirmation, Railway deletes all account information, project data, and removes the account from all email lists.

We aim to be compliant with EU GDPRâ€™s data removal provisions.

## Account Security

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/sessions_qo0lhw.png"
alt="Screenshot of Sessions Page"
layout="responsive"
width={1162} height={587} quality={80} />

Railway is committed to you and your project's security. We provide a variety of methods to help keep users' peace of mind.

### Two-factor Authentication

Two-factor authentication can be enabled under the Account Security page. Most TOTP applications are supported.

After scanning the provided QR code and entering the code for the initial pairing of the application, 2FA will require additional verification for login and destructive actions.

### Account Sessions

Users can view all active browser and CLI sessions on the <a href="https://railway.com/account/security" target="_blank">account security page</a>. Revoking a session will immediately log that device out.

## Referrals

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/referrals_cash_ashj73.png"
alt="Screenshot of Referrals Page"
layout="intrinsic"
width={1784} height={1104} quality={80} />

Every account has an editable referral link. Users can copy and share their personal referral link to earn cash or credits.

Any user who is referred gets $20 in Railway credits, equivalent to a free month on the Pro tier.

Upon every invoice a referral pays, the user who referred them receives 15% commission on that revenue.

Users can view their referral invite status on the <a href="https://railway.com/account/referrals" target="_blank">referrals page</a>, and their total earnings on the <a href="https://railway.com/account/earnings" target="_blank">earnings page</a>.

## Billing

Accounts are billed monthly. Resources used by deleted projects up until the time of deletion are still counted towards the total bill.

Railway may collect applicable sales tax and VAT on your account based on your billing location and local tax requirements, where and when applicable. To ensure accurate tax assessment, Workspace Admins must verify that their billing information, including Billing Address, Organization Name, and Tax ID, is accurate. Organization Name and Tax ID are not required when using Railway for personal use.

Users can manage their billing information as well as view historical payments on the <a href="https://railway.com/workspace/billing" target="_blank">billing page</a>.

## Link Discord Account

Within Account settings, link a Discord account with a Railway account to gain access to additional features on the <a href="https://discord.gg/railway" target="_blank">Railway Discord server</a>.

If the Discord user has not joined the Railway Discord server, linking the account will automatically invite the user to the server.

### Discord Support

Discord users can access the <a href="https://discord.gg/railway" target="_blank">Railway Discord server</a> to get help from the Railway team and other users.

### Priority Boarding Enrollment

For the most adventurous, we offer a beta program called Priority Boarding. Integration with Discord is required. To learn more, visit Priority Boarding.


# Priority Boarding
Source: https://docs.railway.com/reference/priority-boarding

Priority Boarding is Railway's beta program for getting access early to new features. Learn how to be a part of it.

To read more about Priority Boarding, check out <a href="https://blog.railway.com/p/building-the-beta" target="_blank">Priority Boarding: The Journey to Get There</a>.

Learn how to join Priority Boarding here.


# Project Members
Source: https://docs.railway.com/reference/project-members

Learn about the permissions for project members.

<Image src="https://res.cloudinary.com/railway/image/upload/v1644620958/docs/MemberView_New_p0s3be.png"
alt="Screenshot of Project Team Members"
layout="responsive"
width={1377} height={823} quality={100} />

## Scope of Permissions

There are three scopes for project members -

1. **Owner**: full administration of the project.

2. **Editor**: Can create deployments, change project settings and add Editor and Viewer members.

   **Note:** Editors can not do destructive actions such as deleting services or deleting the project itself.

3. **Viewer**: Read only access to the project. Viewers can not make deploys or see environment variables.

The Project Owner is charged for the project's usage.


# Project Usage
Source: https://docs.railway.com/reference/project-usage

Learn how users can see the resource usage of their projects.

Users can see the usage of a project under <a href="https://railway.com/workspace/usage" target="_blank">the Usage page</a> within the Workspace settings.

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/project-usage_gd43fq.png"
alt="Screenshot of Expanded Project Usage Pane"
layout="intrinsic"
width={491} height={286} quality={80} />

### Billing Period Usage

This section outlines the current usage within a billing period, as well as any discounts and credits the user has applied to their account.

In addition to the current usage, the user can see their estimated resource usage for the current billing period.

### Usage by Project

The chart shows the cumulative usage for the billing period. If you delete a project, Railway will still count the usage towards your total.

The Current and Estimated cost metrics show the current resource usage and the estimated usage by the end of the billing period.


# Support
Source: https://docs.railway.com/reference/support

Learn about Railway's support channels.



## Support Tier Overview

### Trial, Free, Hobby

Users on Trial, Free, and Hobby plans have access to community-driven support through Central Station or Discord. While Railway employees may participate in community discussions, responses are not guaranteed for these tiers.

### Pro 

Users on the Pro plan receive direct support from Railway through Central Station, with typical response times of 3-5 business days. Please note that the Pro tier does not include SLOs or application-level support.

### Enterprise & Business Class

Organizations requiring SLOs and enhanced support should consider upgrading to Business Class support. Please refer to the Business Class section for comprehensive details.

## Email Support

Railway does not provide support via email. All support requests should be directed to Central Station or Discord. Email communication is reserved for the following specific purposes:

- Sales inquiries: team@railway.com
- Security reports: bugbounty@railway.com
- Abuse reports: abuse@railway.com
- Privacy inquiries: privacy@railway.com

Emails outside these categories may not receive a response.

## Application-Level Support

Railway generally does not provide application-level support, such as debugging your code, fixing bugs in your application, or helping you with third-party services. We may provide these services on a case-by-case basis for Business Class / Enterprise customers. If you need help with your application, we recommend reaching out to the community on Central Station or Discord.

## Central Station

Railway conducts its support over the Central Station platform.

It hosts our community of 1,600,000+ users and developers. It is where you can find answers to common questions, ask questions, and get in touch with the Railway team.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743120744/central-station_x3txbu.png"
alt="Screenshot of Railway Central Station"
layout="intrinsic"
width={1737} height={913} quality={100} />

Please ensure that you've searched for your issue before creating a new thread, follow the guidelines in How To Ask For Help, and abide by our Code of Conduct.

### Private Threads

You create a **Private Thread** on Central Station if you need to share sensitive information, such as invoices or personal data. Private Threads are only visible to you and Railway employees.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743120858/private-thread_en0bkd.png"
alt="Screenshot of Railway Central Station - Private Threads"
layout="intrinsic"
width={1436} height={455} quality={100} />

Private Threads have a slower response time because only Railway employees can see them. We recommend you to only create a Private Thread if you need to share sensitive information.

Railway may make the thread public for community involvement if we determine that there is no sensitive information in your thread.

## Discord

We have a vibrant Discord community of over 28,000+ users and deveYou can find the Railway Discord at https://discord.gg/railway.

Please ask your questions in the <a href="https://discord.com/channels/713503345364697088/1006629907067064482" target="_blank">âœ‹ ï½œ help</a> channel, and refrain from pinging anyone with the Team or Conductor roles.

## Slack

Railway offers Slack Connect channels to Enterprise plan customers with a minimum committed spend of $2,000/month. Customers can raise issues, coordinate their migration over to Railway, and provide feedback within a Slack Connect channel.

Additionally, the solutions team at Railway may provide a shared Slack Connect channel to facilitate better communication and support.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733324712/docs/cs-2024-12-04-22.20_bms1sa.png"
alt="Screenshot of Slack"
layout="intrinsic"
width={571} height={743} quality={100} />

Enterprise teams with $2,000/month committed spend can create a Slack Connect channel within the Workspace settings page:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733324438/docs/cs-2024-12-04-23.00_uvchnr.png"
alt="Screenshot of Slack Account Linking"
layout="intrinsic"
width={845} height={157} quality={100} />

Users in a Slack Connect channel can invite their team members using the Slack interface or by pressing the Join Slack button again to initiate new invites.

## Business Class

For companies who need dedicated support, we offer Business Class.

Business Class is support and success designed for those who need the full attention of Railway. Business Class support is a dedicated support channel with SLOs for your company. Workspaces become eligible for Business Class support after $2,000/mo in spend.

Reach out to us at team@railway.com to enable your SLO.

### Business Class SLOs

We prioritize Business Class customers over all other support requests.

| Severity                             | Acknowledgement Time |
| ------------------------------------ | -------------------- |
| P1 (Outages, Escalations)            | One hour - 24/7      |
| P2 (Bugs)                            | Same Business Day    |
| P3 (Integrations, General Questions) | Two Business Days    |

For Enterprise customers with $2,000/month committed spend who have a shared 
Slack Connect channel with us, you have access to "Critical" urgency level 
support requests:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1733325632/docs/cs-2024-12-04-23.20_smvweu.png"
alt="Screenshot of Critical urgency level in Slack"
layout="intrinsic"
width={392} height={255} quality={100} />

This feature is also available on Central Station for Business Class customers:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1759234073/docs/critical-issue-private-threads_kdxpvb.png"
alt="Screenshot of Critical urgency level in Central Station"
layout="intrinsic"
width={781} height={282} quality={100} />

Opening a Critical ticket allows you to page our support on-call directly for an immediate response. Please only use this for production outages or critical platform issues preventing your team from using Railway.

### Definition of Priorities

| Priority | Surface Areas                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | **Outages that impact production**. This covers the following components: incidents declared on <a href="https://status.railway.com/" target="_blank">status.railway.com</a> including and especially incidents with end-customer impact (e.g. inability to login to the Dashboard), customer workload-impacting issues due to high load requiring intervention from Railway (e.g. requiring additional resources beyond your current limits). |
| 2        | **Issues related to Railway features**. This covers features offered by Railway, including but not limited to our Dashboard, CLI, and platform-level features such as Deployments, Environments, Private Networking, Volumes.                                                                                                                                                                                                                  |
| 3        | **Integration work and general questions related to Railway**. This covers customer-related requests involving integrating Railway with other services (e.g. fronting your Railway workload with a DDoS protection service), leveraging tools to use Railway the way you like (e.g. IaC provisioning/Terraform), or questions about Railway features or its platform.                                                                          |

### Business Class Response Hours

We offer support during business hours, and prioritize requests from Business Class customers:

- Business hours are Monday through Friday, 9am to 9pm Pacific Time
- Exceptions apply to our business hours during P1 outages where the team will be on-call 24/7
- The team may reply outside of business hours, but we do not guarantee a response outside of business hours

### Business Class Resource Limits

For Business Class customers, Railway increases resource limits beyond the standard limits on a need-based basis. Contact the team through your dedicated communication channel to increase limits.

### Uptime Calculation

As part of this offering, we agree to provide a monthly summary on the uptime of the components of Railway. Customers are provided an RCA to any outages on the Routing Layer.

### Compliance & Audits

Security audits can be provided by request. For most customers, we can provide our security and compliance documentation can be accessed via Railway's Trust Center at trust.railway.com. Please sign in with your Railway account's email address to access Trust Center.

## Enterprise

For enterprises, we offer everything in Business Class along with custom support tailored to your needs. Railway can enter into a contractual SLA under our negotiated pricing offering. Reach out to us at team@railway.com for more information.

## How To Ask For Help

When you reach out for help, it's important that you help us help you! Please include as much information as you can, including but not limited to:

- Description of the issue you're facing
- IDs (Project ID, Service Name/ID, Deployment ID, etc.)
- Railway environment of your service/deployment
- Error messages and descriptions
- Logs (build and/or deploy)
- Link to GitHub repo/code or template you're using, if applicable

Please note that Railway does not provide application-level support.


# Teams
Source: https://docs.railway.com/reference/teams

Learn how you can manage a workspaces within Railway.

For more information, visit our documentation on pricing or <a href="https://railway.com/pricing" target="_blank">railway.com/pricing</a>.

> **Note:** Effective March 3rd, 2025, for users on Railway hosted metal instances, all seat costs will be waived.

## Creating a Workspace

Organizations can create a workspace by heading to the <a href="https://railway.com/new/workspace" target="_blank">Create Workspace</a> page and entering the required information.

## Managing Workspaces

You can open your workspace's settings page to manage members and see billing information by clicking the gear icon next to the name of your workspace on the dashboard.

## Inviting Members

Under the People tab of the settings page, you can invite members.

There are three roles for Workspace members:

- Admin: Full administration of the Workspace and all Workspace projects
- Member: Access to all Workspace projects
- Deployer: View projects and deploy through commits to repos via GitHub integration.

|                              | Admin | Member | Deployer |
| :--------------------------- | :---: | :----: | :------: |
| Automatic GitHub deployments |  âœ”ï¸   |   âœ”ï¸   |    âœ”ï¸    |
| CLI deployments              |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Creating variables           |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Modifying variables          |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Deleting variables           |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Modifying service settings   |  âœ”ï¸   |   âŒ   |    âŒ    |
| Creating services            |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Deleting services            |  âœ”ï¸   |   âŒ   |    âŒ    |
| Viewing logs                 |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Creating volumes             |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Deleting volumes             |  âœ”ï¸   |   âŒ   |    âŒ    |
| Creating new projects        |  âœ”ï¸   |   âœ”ï¸   |    âŒ    |
| Deleting projects            |  âœ”ï¸   |   âŒ   |    âŒ    |
| Adding additional members    |  âœ”ï¸   |   âŒ   |    âŒ    |
| Removing members             |  âœ”ï¸   |   âŒ   |    âŒ    |
| Changing member roles        |  âœ”ï¸   |   âŒ   |    âŒ    |
| Adding trusted domains       |  âœ”ï¸   |   âŒ   |    âŒ    |
| Making a withdrawal          |  âœ”ï¸   |   âŒ   |    âŒ    |
| Accessing billing settings   |  âœ”ï¸   |   âŒ   |    âŒ    |

_Note_: Changes that trigger a deployment will skip the approval requirement when the author has a Deployer role (or higher) and their GitHub account is connected.

## Trusted Domains

Trusted domains may be configured on the workspace settings page. Note that workspace members added via trusted domain will be billed at the normal rate.

<Image 
    src="https://res.cloudinary.com/railway/image/upload/v1733955730/docs/t-d_jbtbm7.png"
    width="1200"
    height="548"
    alt="Trusted domains are configurable via the workspace settings"
/>

You can automate the onboarding of new workspace members with trusted domains. Railway users that sign up with one of the trusted domains associated with your workspace will automatically be granted access to the workspace with the specified role (see above).

For example, new users with example.com email addresses will automatically be added to your workspaces that have the example.com trusted domain.

We verify that you have administrative access to the domain by looking for services in your workspace that use this domain or a subdomain. Make sure to setup a custom domain on your service before adding it as a trusted domain.

## Transferring Projects

Transfer projects from another Workspace or Hobby workspace easily. Detailed instructions can be found here.

## Invoicing and Billing

Railway offers a consumption-based pricing model for your projects. You don't get charged for resources you don't use, instead, Railway charges by the minute for each vCPU and memory resource your service uses.

However, if you expect to use a consistent amount of resources for large companies, you can contact us for a quote and demo. Railway will work with you to find a solution that works for your needs. We are willing to offer Purchase Orders and concierge onboarding for large companies.

### Committed Spend Tiers

Railway offers committed spend tiers for customers with consistent usage needs. Instead of negotiated contract pricing, customers can commit to a specific monthly threshold to unlock additional features and services.

Monthly thresholds for addons is found in our committed spend pricing.

Reach out to us at team@railway.com for more information.

## FAQs

### How do I get my Pro seat costs waived?

As of March 3rd, 2025, Railway waives all seat costs for users on Railway hosted metal instances. To qualify for this benefit:

1. Your workspace must be on the Pro plan
2. Your services must be quality for metal pricing and run on Railway hosted metal instances
3. This waiver will be automatically applied for your next monthly invoice

If you're interested in moving to Railway hosted metal instances to take advantage of this benefit, please contact our team to discuss your requirements and set up a dedicated host solution.

The seat cost waiver provides significant savings for workspaces of all sizes, especially as your workspace grows. This is part of our commitment to providing more flexible and cost-effective pricing options for our customers.


# Usage Limits
Source: https://docs.railway.com/reference/usage-limits

Learn how to configure usage limits.



## Configuring Usage Limits

<Image src="https://res.cloudinary.com/railway/image/upload/v1743193518/docs/usage-limits_pqlot9.png" alt="Usage Limits Modal" layout="responsive" width={1200} height={1075} />

Visit your Workspace Usage page to set the usage limits. Once you click the <kbd>Set Usage Limits</kbd> button, you will see a modal above where you can set a <kbd>Custom email alert</kbd> and a <kbd>Hard limit</kbd>.

<Banner variant="info">The link above takes you to the usage page for your personal account. If you want to set a usage limit for your team, you can use the account switcher in the top left corner of your dashboard to access the team's usage page.</Banner>

## Custom Email Alert

You can think of this as a _soft limit_. When your resource usage reaches the specified amount, we will email you that this threshold has been met. Your resources will remain unaffected.

## Hard Limit

Once your resource usage hits the specified hard limit, all your workloads will be taken offline to prevent them from incurring further resource usage. Think of the hard limit as the absolute maximum amount you're willing to spend on your infrastructure.

We will send you multiple reminders as your usage approaches your hard limit:

1. When your usage reaches 75% of your hard limit
2. When your usage reaches 90% of your hard limit

We will send you another email if your workloads are taken down due to your specified usage limits.

<Banner variant="danger">Setting a hard limit is a possibly destructive action as you're risking having all your resources shut down once your usage crosses the specified amount.</Banner>

## FAQ

<Collapse title="Can I set a usage limit?">
Yes, usage limits are available for all subscription plans.
</Collapse>

<Collapse title="Do I need to set a hard limit to set a custom email alert?">
No. You can leave the hard limit blank if you simply want to be notified at a particular amount of usage.
</Collapse>

<Collapse title="What is the minimum hard limit?">
The minimum amount you can specify as the hard limit is $10.
</Collapse>

<Collapse title="How can I restart my resources if I hit my usage limit?">
To restart your resources, you can either increase your usage limit or remove it entirely.

For guidance on restarting your resources, please refer to our FAQ section.
</Collapse>

<Collapse title="Will my resources be automatically started during the next billing cycle?">
No. Once your resources are shut down, it is your responsibility to restart them.
</Collapse>


# CLI API
Source: https://docs.railway.com/reference/cli-api

Learn about the Railway CLI commands.

Railway project from the command line.

This document describes the commands available in the CLI.

For information on how to install the CLI and more examples of usage, see the CLI guide.

## Add

_Add a service to your project_

## Completion

_Generate a shell-completions for the following shells: bash, elvish, fish, and powershell_

## Connect

_Connect to a database's shell (psql for Postgres, mongosh for MongoDB, etc.)_

This requires you to have the database's appropriate shell/client installed in your $PATH:

- Postgres: psql (https://www.postgresql.org/docs/current/app-psql.html)
- Redis: redis-cli (https://redis.io/docs/ui/cli/)
- MongoDB: mongosh (https://www.mongodb.com/docs/mongodb-shell/)
- MySQL: mysql (https://dev.mysql.com/doc/refman/8.0/en/mysql.html)

## Deploy

_Deploy a template into your project_

## Domain

_Create a domain for a service_

## Docs

_Open the Railway documentation site in the default browser_


````

## Down

_Remove the most recent deployment_

## Environment

_Create, delete or link an environment_

View environment docs for more information.

If you run railway environment without specifying a name, you will be prompted
with an environment selector that lists all your environments for the project.

### railway environment new

_Create a new environment_

### railway environment delete

_Delete an environment_

**Note**: railway environment delete will not work if an account has 2FA and the terminal is not being run interactively.

## Init

_Create a new Project from the CLI_

## Link

_Connect to an existing Railway project_

Running link with no project ID will prompt you to select a team and project.

## List

_List all projects in your Railway account_

## Login

_Login to your Railway account_

This will open the browser to https://railway.com/cli-login.

### Browserless

If you are in an environment where the terminal cannot open a web browser, (i.e.
SSH session or Codespaces), you can
perform a _browserless_ login.

This will prompt you to go to a URL (you can copy and paste) and present you
with a 4 word code that you need to verify. If the codes match, click "Verify"
and you will be logged in.

## Logout

_Logout of your Railway account_

## Logs

_View logs for the most recent deployment_

## Open

_Open your current Railway project in the browser_

## Run

_Run a command using the Railway environment_

This also injects all environment variables associated with the databases you have
installed in your project.

## Service

_Link a service to the current project_

## Shell

_Create a subshell (based on $SHELL) with all the variables from your project/environment/service loaded and accessible_

## SSH

_SSH into a project/service_

## Status

_View the status of your Railway project and user_

## Unlink

_Disconnects the current directory from Railway_

You will need to rerun railway link to use railway in this directory again.

## Up

_Deploy a directory to your Railway project_

If no path is provided, the top linked directory is deployed. The currently selected environment is used.

## Variables

_View a table of all the environment variables associated with your project and environment_

## Whoami

_View what user is currently authenticated with Railway_

## Volume

_Manage project volumes with options to list, add, delete, update, attach, and detach volumes_

## Redeploy

_Redeploy the currently deployed version of a service_

## Help

_Help command reference_

## Code Examples

~ railway add --help
Add a service to your project

Usage: railway add [OPTIONS]

Options:
  -d, --database <DATABASE>
          The name of the database to add

          [possible values: postgres, mysql, redis, mongo]

  -s, --service [<SERVICE>]
          The name of the service to create (leave blank for randomly generated)

  -r, --repo <REPO>
          The repo to link to the service

  -i, --image <IMAGE>
          The docker image to link to the service

  -v, --variables <VARIABLES>
          The "{key}={value}" environment variable pair to set the service variables. Example:

          railway add --service --variables "MY_SPECIAL_ENV_VAR=1" --variables "BACKEND_PORT=3000"

      --json
          Output in JSON format

  -h, --help
          Print help (see a summary with '-h')

  -V, --version
          Print version

~ railway completion --help
Generate completion script

Usage: railway completion [OPTIONS] <SHELL>

Arguments:
  <SHELL>  [possible values: bash, elvish, fish, powershell, zsh]

Options:
      --json     Output in JSON format
  -h, --help     Print help
  -V, --version  Print version

~ railway connect --help
Connect to a database's shell (psql for Postgres, mongosh for MongoDB, etc.)

Usage: railway connect [OPTIONS] [SERVICE_NAME]

Arguments:
  [SERVICE_NAME]  The name of the database to connect to

Options:
  -e, --environment <ENVIRONMENT>  Environment to pull variables from (defaults to linked environment)
      --json                       Output in JSON format
  -h, --help                       Print help
  -V, --version                    Print version

railway deploy --help
Provisions a template into your project

Usage: railway deploy [OPTIONS]

Options:
  -t, --template <TEMPLATE>  The code of the template to deploy
  -v, --variable <VARIABLE>  The "{key}={value}" environment variable pair to set the template variables
          To specify the variable for a single service prefix it with "{service}." Example:
          bash railway deploy -t postgres -v "MY_SPECIAL_ENV_VAR=1" -v "Backend.Port=3000"

      --json                 Output in JSON format
  -h, --help                 Print help (see a summary with '-h')
  -V, --version              Print version

~ railway domain --help
Add a custom domain or generate a railway provided domain for a service

Usage: railway domain [OPTIONS] [DOMAIN]

Arguments:
  [DOMAIN]  Optionally, specify a custom domain to use. If not specified, a domain will be generated

Options:
  -p, --port <PORT>        The port to connect to the domain
  -s, --service <SERVICE>  The name of the service to generate the domain for
      --json               Output in JSON format
  -h, --help               Print help (see more with '--help')
  -V, --version            Print version

`~ railway docs --help
Open Railway Documentation in default browser

Usage: railway docs [OPTIONS]

Options:
      --json     Output in JSON format
  -h, --help     Print help
  -V, --version  Print version

`
## Down

_Remove the most recent deployment_

## Environment

_Create, delete or link an environment_

View [environment docs](/reference/environments) for more information.

If you run `railway environment` without specifying a name, you will be prompted
with an environment selector that lists all your environments for the project.

### railway environment new

_Create a new environment_

### railway environment delete

_Delete an environment_

**Note**: `railway environment delete` will not work if an account has 2FA and the terminal is not being run interactively.

## Init

_Create a new Project from the CLI_

## Link

_Connect to an existing Railway project_

Running `link` with no project ID will prompt you to select a team and project.

## List

_List all projects in your Railway account_

## Login

_Login to your Railway account_

This will open the browser to `https://railway.com/cli-login`.

### Browserless

If you are in an environment where the terminal cannot open a web browser, (i.e.
SSH session or [Codespaces](https://github.com/features/codespaces)), you can
perform a _browserless_ login.

This will prompt you to go to a URL (you can copy and paste) and present you
with a 4 word code that you need to verify. If the codes match, click "Verify"
and you will be logged in.

## Logout

_Logout of your Railway account_

## Logs

_View logs for the most recent deployment_

## Open

_Open your current Railway project in the browser_

## Run

_Run a command using the Railway environment_

This also injects all environment variables associated with the databases you have
installed in your project.

## Service

_Link a service to the current project_

## Shell

_Create a subshell (based on `$SHELL`) with all the variables from your project/environment/service loaded and accessible_

## SSH

_SSH into a project/service_

## Status

_View the status of your Railway project and user_

## Unlink

_Disconnects the current directory from Railway_

You will need to rerun `railway link` to use `railway` in this directory again.

## Up

_Deploy a directory to your Railway project_

If no path is provided, the top linked directory is deployed. The currently selected environment is used.

## Variables

_View a table of all the environment variables associated with your project and environment_

## Whoami

_View what user is currently authenticated with Railway_

## Volume

_Manage project volumes with options to list, add, delete, update, attach, and detach volumes_

## Redeploy

_Redeploy the currently deployed version of a service_

## Help

_Help command reference_


# MCP Server
Source: https://docs.railway.com/reference/mcp-server

Learn about the official Railway MCP (Model Context Protocol) server and how to use it.

With this server, you can ask your IDE or AI assistant to create projects, deploy templates, create/select environments, or pull environment variables.


> ðŸš¨ The Railway MCP Server is **highly experimental**. Expect bugs and missing features. By design, destructive actions (e.g., deleting services or environments) are excluded, but you should still carefully review any tool executions before running them.

The Railway MCP Server is open-source and available on GitHub.

## Understanding MCP and Railway MCP Server

The **Model Context Protocol (MCP)** defines a standard for how AI applications (hosts) can interact with external tools and data sources through a client-server architecture.

* **Hosts**: Applications such as Cursor, VS Code, Claude Desktop, or Windsurf that connect to MCP servers.
* **Clients**: The layer within hosts that maintains one-to-one connections with individual MCP servers.
* **Servers**: Standalone programs (like the Railway MCP Server) that expose tools and workflows for managing external systems.

The **Railway MCP Server** acts as the server in this architecture, translating natural language requests into CLI workflows powered by the Railway CLI.

## Prerequisites

To get started with the MCP server, you need to have the Railway CLI installed and authenticated.

## Installation

### Cursor

You can one-click install the MCP server in Cursor by clicking the "Add to Cursor" button below:

![Install MCP Server](https://cursor.com/en/install-mcp?name=Railway&config=eyJjb21tYW5kIjoibnB4IC15IEByYWlsd2F5L21jcC1zZXJ2ZXIifQ%3D%3D)

Alternatively, you can add the following configuration to your .cursor/mcp.json file manually:

### VS Code

Add the following configuration to your .vscode/mcp.json file:


### Claude Code

To install the MCP server in Claude Code, you can use the following command:

## Example Usage

* **Create and deploy a new app**

* **Deploy from a template**

* **Pull environment variables**

* **Create a new environment**

## Available MCP Tools

The Railway MCP Server provides a curated set of tools. Your AI assistant will automatically call these tools based on the context of your request.

* **Status**

  * check-railway-status â€” Verify CLI installation and authentication

* **Project Management**

  * list-projects â€” List all projects
  * create-project-and-link â€” Create a project and link it to the current directory

* **Service Management**

  * list-services â€” List project services
  * link-service â€” Link a service to the current directory
  * deploy â€” Deploy a service
  * deploy-template â€” Deploy from the Railway Template Library

* **Environment Management**

  * create-environment â€” Create a new environment
  * link-environment â€” Link environment to current directory

* **Configuration & Variables**

  * list-variables â€” List environment variables
  * set-variables â€” Set environment variables
  * generate-domain â€” Generate a Railway domain

* **Monitoring & Logs**

  * get-logs â€” Retrieve service logs

## Security Considerations

Under the hood, the Railway MCP Server runs the Railway CLI commands. While destructive operations are intentionally excluded and not exposed as MCP tools, you should still:

* **Review actions** requested by the LLM before running them.
* **Restrict access** to ensure only trusted users can invoke the MCP server.
* **Avoid production risks** by limiting usage to local development and non-critical environments.

## Feature requests

The Railway MCP Server is a work in progress. We are actively working on adding more tools and features. If you have a feature request, leave your feedback on this Central Station post.

## Code Examples

{
  "mcpServers": {
    "Railway": {
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}

{
  "servers": {
    "Railway": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@railway/mcp-server"]
    }
  }
}

claude mcp add Railway npx @railway/mcp-server

Create a Next.js app in this directory and deploy it to Railway.
  Also assign it a domain.

Deploy a Postgres database

Deploy a single node ClickHouse database

Pull environment variables for my project and save them to a .env file

Create a development environment called `development` 
  cloned from production and set it as linked


# Public API
Source: https://docs.railway.com/reference/public-api

Learn about the Railway GraphQL Public API.



## Endpoint

The public API is accessible at the following endpoint:

## Authentication

To use the API, you will need an API token. There are three types of tokens you can create.

#### Team Token and Personal Token

You can create an API token by visiting the <a href="https://railway.com/account/tokens" target="_blank">tokens page</a> in your account settings.

- **Team tokens** are tied to a team and will have access to all the team's resources. This token cannot be used to access your personal resources on Railway so feel free to share it with your teammates.
- **Non-team tokens** will be tied to your Railway account and will have access to all your resources. Do not share this token with anyone else.

#### Project Token

You can create a project token by visiting the tokens page in your project settings.

Project tokens are scoped to a specific environment within a project and can only be used to authenticate requests to that environment.

## Schema

The Railway API supports introspection meaning you can use popular tools like Postman or Insomnia to query the schema. Simply set up your connection with the endpoint and Authorization token, and fetch the schema.

### API Collection File

We provide a collection file which can be imported into your preferred API client. Once imported, you should only need to add your API token to get connected and start executing queries in the collection. Click here to download it.

### GraphiQL Playground

Use our GraphiQL playground to view the schema and test your queries.

Make sure to set an Authorization header with an auth token. Click the "Headers" tab at the bottom of the GraphiQL page and enter this json, using your own token:

## Rate Limits

In order to protect the Railway API from spam and misusage, we have established some basic rate limits. The current limits to the API are:

- Requests per hour: **100** RPH for Free customers, **1000** RPH for Hobby customers, **10000** RPH for Pro customers; custom for Enterprise.
- Requests per second: **10** RPS for Hobby customers; **50** RPS for Pro customers; custom for Enterprise.

To help you keep track of your usage, Railway sends a few headers with the response on each request.

| Header                | Description                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| X-RateLimit-Limit     | The maximum number of API requests allowed per day.                                                                                                |
| X-RateLimit-Remaining | The number of API requests your token can make in the current window.                                                                              |
| X-RateLimit-Reset     | The time at which the current window ends and your remaining requests reset.                                                                       |
| Retry-After           | The amount of time after which you can make another request. This header is only sent once you've used up all your requests in the current window. |

## Support

For more information on how to use the Public API and for examples of queries, view the Public API guide.

If you run into problems using the API or have any suggestions, feel free to join our Discord server where you can interact with the engineers working on the API directly.

## Code Examples

https://backboard.railway.com/graphql/v2

curl --request POST \
  --url https://backboard.railway.com/graphql/v2 \
  --header 'Authorization: Bearer <API_TOKEN_GOES_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{"query":"query { me { name email } }"}'

curl --request POST \
  --url https://backboard.railway.com/graphql/v2 \
  --header 'Project-Access-Token: <PROJECT_TOKEN_GOES_HERE>' \
  --header 'Content-Type: application/json' \
  --data '{"query":"query { projectToken { projectId environmentId } }"}'

{ "Authorization": "Bearer <API_TOKEN_GOES_HERE>" }


# Templates
Source: https://docs.railway.com/reference/templates

Learn how Railwayâ€™s Kickback program rewards template publishers for their contributions.

As a user in Railway, you can create and publish templates for others to use, or you can deploy templates from our <a href="https://railway.com/templates" target="_blank">template marketplace</a>.

For information on how to create, publish, and deploy templates, visit our Templates guides.

## Kickback program

If you publish a template, and it is deployed into other users' projects, you are immediately eligible for a 50% kickback of the usage cost incurred, in the form of Railway credits.

If a user deploys your template, and the usage of the services cost the user $100, you would receive $50 in Railway credits or $50 in cash (USD).

Read more about the kickback program <a href="https://railway.com/open-source-kickback" target="_blank">here</a>.

### Kickback Eligibility Requirements

- Your template must be published to the marketplace to be eligible for kickback.
- For Hobby users with a $5 discount, only usage in excess of the discount is counted in the kickback.
- All service types and resource usage of those services (compute, volume, egress, etc) _do count_ towards the kickback.
- Platform fees are not included in the kickback, but usage fees of the platform are included. Examples of platform fees are:

  - Cost of Subscription Plan ($5 for Hobby, $20 for Pro)
  - Additional Team Seats

  As an example, if a user pays $20 in platform fees, then incurs $200 of usage from your template, you are eligible for a $100 kickback (50% of $200).

- The minimum kickback our program supports is $0.01, meaning usage of your template must incur at least $0.04 in usage after discounts and/or platform fees.

## Earnings and Withdrawals

By default, your template kickbacks are automatically converted into Railway Credits. But we also offer cash withdrawals. Visit the /earnings tab inside your account settings for more details. There you can add your details and request a withdrawal.

<Banner variant="warning">Cash Withdrawals are **not** supported in countries like **Brazil, China, and Russia**. A full list of supported countries is available on the earnings page.</Banner>

### FAQ

#### How do I start earning cash?

- Simply flip the switch on the Earnings page marked Direct Deposit to Railway Credits. This will stop auto-depositing your earnings into our Credits system. You will then begin accruing cash in your Available Balance.

#### How do I request a withdrawal?

- Follow the instructions inside the Earnings tab. We use Stripe Connect to handle withdrawals. After completing the onboarding process, you will be able to request a withdrawal.

#### Why is my country not supported?

- Due to local regulations and compliance requirements, certain regions are not eligible for cash withdrawals. You can choose from the 130+ countries that are supported in the onboarding process.

#### Can I make manual withdrawals to credits too?

- Yes! Choose to Credits in the dropdown and then make your withdrawal request.

#### I have earned a lot of kickbacks from a template, but this page says my available balance is $0. Why?

- The current kickback method is to automatically apply your kickbacks as Railway Credits. You can opt out of this if you wish to start accruing cash.

#### Can I still use the older, automatic-credits setting?

- Yes. This behavior is enabled by default. You can opt out of it, and back in to it, at any time. Simply use the switch on the Earnings page marked Direct Deposit to Railway Credits.

#### What is the minimum and maximum withdrawal amount?

- For now, withdrawals may be made in $100 - $10,000 increments.

#### What is the timeframe from withdrawal request to payout?

- Withdrawals are usually processed instantly. Once processed, the funds will usually take up to 10 business days to reach your account. Depending on your region and bank, this may take longer.

## Updatable Templates

When you deploy any services from a template based on a GitHub repo, every time you visit the project in Railway, we will check to see if the project it is based on has been updated by its creator.

If it has received an upstream update, we will create a branch on the GitHub repo that was created when deploying the template, allowing for you to test it out within a PR deploy.

If you are happy with the changes, you can merge the pull request, and we will automatically deploy it to your production environment.

<Banner variant="info">
If you're curious, you can read more about how we built updatable templates in this <Link href="https://blog.railway.com/p/updatable-starters" target="_blank">blog post</Link>.
</Banner>

Note that this feature only works for services based on GitHub repositories. At this time, we do not have a mechanism to check for updates to Docker images from which services may be sourced.


# Plans
Source: https://docs.railway.com/reference/pricing/plans

Learn about Railway's plans and pricing.



## Plans

Railway offers four plans in addition to a Trial:

|                |                                                                                                                                                    |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Free**       | For running small apps with $1 of free credit per month                                                                                             |
| **Hobby**      | For indie hackers and developers to build and deploy personal projects                                                                             |
| **Pro**        | For professional developers and their teams shipping to production                                                                                 |
| **Enterprise** | For teams building and deploying production applications with the need for enterprise features related to compliance, SLAs, and account management |

### Subscription Pricing

Each Railway account needs an active subscription. The base subscription fee allows you to use the Railway platform and features included in the tier of your subscription. The subscription fee goes towards your usage-costs on the platform.

| Plan           | Price       |
| -------------- | ----------- |
| **Free**       | $0 / month  |
| **Hobby**      | $5 / month  |
| **Pro**        | $20 / month |
| **Enterprise** | Custom      |

Read more about our plans at <a href="https://railway.com/pricing" target="_blank">railway.com/pricing</a>.

Curious about potential savings? Upload your current invoice and see how much you can save by running your workloads on Railway.

### Default Plan Resources

Depending on the plan you are on, you are allowed to use up these resources per service.

| Plan           | **RAM**   | **CPU**     | **Ephemeral Storage** | **Volume Storage** | **Image Size** |
| -------------- | --------- | ----------- | --------------------- | ------------------ | -------------- |
| **Trial**      | **1 GB**  | **2 vCPU**  | **1 GB**              | **0.5 GB**         | **4 GB**       |
| **Free**       | **0.5 GB**| **1 vCPU**  | **1 GB**              | **0.5 GB**         | **4 GB**       | 
| **Hobby**      | **8 GB**  | **8 vCPU**  | **100 GB**            | **5 GB**           | **100 GB**     |
| **Pro**        | **32 GB** | **32 vCPU** | **100 GB**            | **50 GB \***       | **Unlimited**  |
| **Enterprise** | **48 GB** | **64 vCPU** | **100 GB**            | **2 TB \***        | **Unlimited**  |

Note that these are initial values and users on the Pro and Enterprise plans can request limit increases.

\* For Volumes, Pro users and above can self-serve to increase their volume up to 250 GB. Check out this guide for information.

### Resource Usage Pricing

On top of the base subscription fee above, Railway charges for the resources that you consume.

You are only charged for the resources you actually use, which helps prevent runaway cloud costs and provides assurances that you're always getting the best deal possible on your cloud spend.

| Resource                                 | Resource Price                                        |
| ---------------------------------------- | ----------------------------------------------------- |
| **RAM**                                  | $10 / GB / month ($0.000231 / GB / minute)            |
| **CPU**                                  | $20 / vCPU / month ($0.000463 / vCPU / minute)        |
| **Network Egress**                       | $0.05 / GB ($0.000000047683716 / KB)                  |
| **Volume Storage** | $0.15 / GB / month ($0.000003472222222 / GB / minute) |

To learn more about controlling your resource usage costs, read our FAQ on How do I prevent spending more than I want to?

## Included Usage

The Hobby plan includes $5 of resource usage per month.

If your total resource usage at the end of your billing period is $5 or less, you will not be charged for resource usage. If your total resource usage exceeds $5 in any given billing period, you will be charged the delta.

Included resource usage is reset at the end of every billing cycle and does not accumulate over time.

**Examples**:

- If your resource usage is $3, your total bill for the cycle will be $5. You are only charged the subscription fee because your resource usage is below $5 and therefore included in your subscription
- If your resource usage is $7, your total bill for the cycle will be $7 ($5 subscription fee + $2 of usage), because your resource usage exceeds the included resource usage

Similarly, the Pro plan includes $20 of resource usage per month and the same examples and billing logic apply. If your usage stays within $20, you'll only pay the subscription fee. If it exceeds $20, you'll be charged the difference on top of the subscription.

### Additional Services

Railway offers Business Class Support as an add-on service to the Pro plan. Business Class Support is included with Enterprise. Contact us to get started.

## Image Retention Policy

Railway retains images for a period of time after a deployment is removed. This is to allow for rollback to a previous deployment.

| Plan             | **Policy**    |
| ---------------- | ------------- |
| **Free / Trial** | **24 hours**  |
| **Hobby**        | **72 hours**  |
| **Pro**          | **120 hours** |
| **Enterprise**   | **360 hours** |

When a deployment is removed, the image will be retained for the duration of the policy.

Rolling back a removed deployment within the retention policy will restore the previous image, settings, and all variables with a new deployment; no redeployment is required.

A removed deployment that is outside of the retention policy will not have the option to rollback; instead, you will need to use the redeploy feature. This will rebuild the image from the original source code with the deployment's original variables.

## Committed Spend Tiers

Railway offers committed spend tiers for customers with consistent usage needs. Instead of negotiated contract pricing, customers can commit to a specific monthly spend level to unlock additional features and services.

For example, customers who commit to a $10,000/month spend rate can access dedicated hosts, with all pricing going towards their usage. This approach provides more flexibility and transparency compared to traditional contract pricing.

| Feature                    | Commitment Spend | Description                                                                                                      |
| -------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| **90-day log history**     | $200/month       | Extended log retention for better historical analysis and auditing.                                              |
| **48 GB RAM / 64 vCPU**    | $500/month       | Access to increased computing resources at a committed monthly spend level.                                      |
| **HIPAA BAAs**             | $1,000/month     | HIPAA Business Associate Agreements for compliant health data handling. Requires a year commitment paid monthly. |
| **Slack Connect channels** | $2,000/month     | Dedicated Slack Connect channels for enhanced communication and support with the Railway team.                   |
| **SLOs**                   | $2,000/month     | Service Level Objectives to ensure and track application performance.                                            |
| **Dedicated Hosts**        | $10,000/month    | Custom dedicated infrastructure for enhanced performance and control.                                            |

To learn more about committed spend tiers, please contact our team.

### One-time Grant of Credits on the Free Trial

Users who create a new Trial account receive a free one-time grant of $5. Railway will expend any free credit before consuming any purchased credits. Trial plan users are unable to purchase credits without upgrading to the Hobby plan.

Learn more about Railway's Free Trial here.

## Partial Month Charges

In some cases, your billing method may be charged for the partial amount of your bill earlier in the billing cycle.
This ensures that your account remains in good standing, and helps us mitigate risk and fraud.

## FAQs

### Which plan is right for me?

- **Hobby** is for indie hackers and developers to build and deploy personal projects
- **Pro** is for professional developers and their teams shipping to production
- **Enterprise** is for dev teams building and deploying production applications with the need for enterprise features related to compliance, SLAs, and account management

### Can I upgrade or downgrade at any time?

You can upgrade any time, and when you do, you will get to the features of your new plan, as well as access to more powerful resources, immediately. When you downgrade, the changes will take effect at the beginning of your next billing cycle.

### What is the difference between subscription and resource usage?

There are two main components to your bill:

| Component          | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| **Subscription**   | Cost of the plan you're on                                              |
| **Resource Usage** | Cost of the resources you've consumed: [cost per unit] x [used units] |

Subscription is a flat fee you pay monthly for the tier you're subscribed to, and Resource Usage varies according to your resource consumption for the month.

### Can I add collaborators to my project?

Railway's Pro and Enterprise plans are designed for collaboration. These plans allow you to add members to your team and manage their permissions.

Read more about adding members to your Pro or Enterprise team here.

### How long does Railway keep my volume data if I am no longer on a paid plan?

Railway will delete your data from the platform as per the timeline below after sufficient warning.

| Plan                   | Days                       |
| ---------------------- | -------------------------- |
| **Free or Trial plan** | 30 days after expiry       |
| **Hobby plan**         | 60 days after cancellation |
| **Pro plan**           | 90 days after cancellation |

### Is the Hobby Plan free?

No. The Hobby Plan is $5 a month, and it includes a resource usage credit of $5. Even if you do not use the $5 in usage (CPU, Memory, egress), you always pay the $5 subscription fee.

### Can I get the Hobby plan subscription fee waived?

Railway waives the monthly Hobby plan subscription fee for a small set of active builders on the platform.

Eligibility is automatically assessed based on several factors, including your usage on the platform, your GitHub account, and more. If you qualify, you will be notified in the Dashboard or when you upgrade to the Hobby plan. If you do not qualify, you will not be eligible for the waiver.

This is a fully automated process, and Railway does not respond to requests for waiver.

### I prefer to prepay. Is that possible?

Not anymore as of March 30th, Railway requires the use of a post-paid card.

### What happens if I use credits as a payment method and my account runs out of credits?

If you are using credits as a payment method and your credit balance reaches zero, your subscription will be cancelled. You will no longer be able to deploy to Railway and we will stop all of your workloads. To resolve this, you will need to sign up for a new subscription after topping up sufficient credits.

### Why was I charged for a partial month of usage?

Railway has an automated system in place which can result in a partial amount of your bill being charged to your payment method, earlier in the billing cycle.

This is intended to ensure that your account remains in good standing, and helps us to mitigate risk and fraud.


# Free Trial
Source: https://docs.railway.com/reference/pricing/free-trial

Learn about Railway's free trial plan.

After 30 days passes or $5 is spent, the free trial reverts to the Free plan, which provides $1 of free credit per month. The credit does not roll over month to month.

## Full vs Limited Trial

Your trial experience depends on whether Railway can verify your account.

| Trial Type        | Deploy Code | Deploy Databases |
| ----------------- | ----------- | ---------------- |
| **Full Trial**    | âœ…          | âœ…               |
| **Limited Trial** | âŒ          | âœ…               |

When you sign up for a free Trial, you can connect your GitHub account to initiate verification. Your verification status depends on a number of factors, including the age and activity of your GitHub account.

If your account is not verified â€” either because you have not initiated the verification process or your account does not meet our criteria for verification â€” your trial experience will be limited to deploying databases.

Verification is a necessary measure to prevent abuse of the free Trial, limiting users from creating multiple accounts and reducing the risk of trial users deploying or hosting content that violates Railway's Terms of Service.

This is a fully automated process, and Railway does not respond to requests for verification. If your account is not verified, you can upgrade to the Hobby plan to unlock the full Railway experience.

## FAQs

### How do I get started with the free Trial?

If you do not already have a Railway account, you can sign up for a free Trial by clicking "Login" at railway.com.

### How does the Trial work?

When you sign up for the free Trial, you will receive a one-time grant of $5 in credits that you can use to try out Railway. The credits will be applied towards any usage on the platform and expire in 30 days. If you upgrade to a plan while you still have a credit balance from the trial, the remaining balance will carry over to your new plan.

### What resources can I access during the Trial?

During the trial, you can access the same features as on the Hobby plan, however you will be limited to 1 GB of RAM and shared (rather than dedicated) vCPU cores. Additionally, your projects will be limited to 5 services per project.

As a trial user, you can always spin-up databases. However, to deploy code, you must be on the Full Trial.

### What's the difference between the Limited Trial and the Full Trial?

If you connect your GitHub account, and we are able to verify it against a set of parameters, you will be on the Full Trial where you can deploy both code and databases.

If you do not connect a GitHub account, or we are not able to verify your account, you will be on the Limited Trial, where you can only deploy databases.

While you're on the Limited Trial, you can initiate verification at any time by visiting railway.com/verify in order to access the Full Trial experience.

### How far will the $5 one-time Trial grant last?

The longevity of your one-time trial grant depends on how many resources you consume within the 30 day period you sign-up for the platform. The more resources you deploy, the greater the consumption.

### Data Retention

Railway deletes stateful volumes created by Trial accounts 30 days after the expiration of your credits. To retain your data, upgrade your account after the Trial period.


# FAQs
Source: https://docs.railway.com/reference/pricing/faqs

General common Questions & Answers related to Railway's pricing.

### Can I try Railway without a credit-card?

Yes. As a new Railway user, you can sign up for a Free Trial. You will receive a one-time grant of $5 to use on resources.

### What payment methods are accepted?

Railway only accepts credit cards for plan subscriptions. We also support custom invoicing for customers on the Enterprise plan.

### What will it cost to run my app?

With Railway, you are billed for the subscription fee of the plan you're subscribed to, and the resource usage of your workloads.

To understand how much your app will cost to run on Railway, we recommend you to:

1. Deploy your project with the Trial or Hobby plan
2. Allow it to run for one week
3. Check your Estimated Usage in the Usage Section of your Workspace settings

Keeping it running for one week allows us to rack up sufficient metrics to provide you with an estimate of your usage for the current billing cycle. You can then use this information to extrapolate the cost you should expect.

We are unable to give exact quotes or estimates for how much it will cost to run your app because it is highly dependent on what you're deploying.

For a rough approximation of the cost for running your app, try our pricing calculator.

If you are supporting a commercial application, we highly recommend you to upgrade to the Pro plan for higher resource limits and access to priority support.

### How do I prevent spending more than I want to?

Check out our guide on optimizing usage.

### Why is my resource usage higher than expected?

You can check your resource usage in the Usage Section of your Workspace settings. This includes a breakdown of your resource usage by project, along with the resource it's consuming (CPU, Memory, Network, etc.)

Common reasons for high resource usage include:

- Memory leaks in your application, causing it to consume more memory than necessary
- Higher traffic than usual, causing your app to consume more CPU and/or Network
- Certain templates or apps may be inherently more resource-intensive than others
- If you notice high egress cost in your bill, ensure that you are connecting to your Railway databases over Private Networking
- If you have PR deploys enabled in your project, Railway will deploy a mirror copy of your workload(s) based on the environment it forks from (productionÂ by default). You are billed for those workload(s) running in the ephemeral environment

Unfortunately, we are unable to assist with figuring out why your bill is higher than normal, as it is entirely dependent on what you have deployed. Resource usage is billed in a manner akin to how a utility company operates: they can tell you the amount of electricity you've consumed, but they can't explain the reasons for your high usage. Similarly, we can only provide information on the quantity of resources you consume, not the reasons behind it.

### Why am I charged for more than $5 on the Hobby plan?

Railway's pricing has two components: a monthly subscription fee, and resource usage costs. While the Hobby plan includes $5 of resource usage per month, you are charged for any usage that exceeds this amount.

Learn more here.

### Why is there an "Applied balance" on my invoice?

When the amount due on your invoice is less than $0.50, and you do not have a credit balance, Railway marks the invoice as paid and registers the amount to your credit balance as a debit to be charged on a future invoice.

### How do I view or upgrade my current plan?

Your current plan is listed in the Account Selector in the top left corner of your Dashboard. You can also view your active plan and upgrade options from the Plans page. 

### How do I cancel my subscription?

To cancel your active subscription, go to the "Active Plan" section of your Billing page and click Cancel Plan. 

When you cancel your subscription, Railway will stop all deployments in your workspace to prevent further charges. Your plan will remain active until the end of your billing cycle. 

### How do I add or update billing information?

To add or update your Billing information, go to the Billing page. In the "Billing Info" section, you can add or update the following information: 
- Payment Method
- Billing Email
- Billing Address
- Tax ID / VAT number

When Billing Information is added or updated, it will be reflected on all future invoices from Railway. 

### How is Salex Tax/VAT handled?

Railway may collect applicable sales tax and VAT on your account based on your billing location and local tax requirements, where and when applicable. When assessed and collected, Sales Tax/VAT is explicitly outlined on your invoice.

To ensure accurate tax assessment, Workspace Admins must verify that their billing information, including Billing Address, Organization Name, and Tax ID (when applicable), is accurate. Organization Name and Tax ID are not required when using Railway for personal use.

To view and manage your subscription, visit the billing section of your workspace.

### How do I remove my saved payment method from my account?

If your subscription is canceled and you have no pending invoices, you can remove your saved payment method by doing the following:

1. Go to the billing page for your workspace
2. Click "Delete" in the payment method section

### What happens if the payment fails for my subscription?

If your subscription payment fails, we retry the payment method on file over several days. We also inform you of the payment failure, in case your payment method needs to be updated.

If payment continues to fail, we flag your services to be stopped and send you a warning.

If we do not receive payment, your services are stopped until all open invoices have been paid.

### My services were stopped, what do I do?

Your services may be stopped by Railway for the following reasons, along with their solutions -

- **Usage limits reached:** You've hit your usage limits. Increase your usage limit or wait until the next billing period.

- **Trial credits exhausted:** You've run out of trial credits. Consider upgrading to a paid plan to continue using the service.

- **Failed payment:** Your payment method has failed. Update your payment method and pay your outstanding invoice.

- **Unpaid invoice:** You have an outstanding invoice. Pay your outstanding invoice.

In all cases, you can redeploy your services once the underlying issue is resolved, this can be done from the Removed deployment's 3-dot menu.

**Note:** Although Railway will remove your deployment for any of the above reasons, Railway will not remove the volume attached to the service.

### I am a freelancer or represent an agency. How do I manage my billing relationships with my clients?

Create a Pro plan on Railway and add the client to the workspace. If you run into issues when it's time to hand over your workload to your client, you can reach out to us over our Central Station.

### Why did I receive another invoice after cancelling my subscription?

You may receive an invoice containing charges for Resource Usage after you cancel your subscription. These are resource usages you have consumed in that billing cycle that we reserve the right to charge you for.

### How do I request a refund?

Please refer to Pricing -> Refunds.

### Requesting an invoice re-issuance

If you encounter "This invoice can no longer be paid on Stripe" error or need
your Tax ID added to a previous invoice, follow the steps below to get an
invoice reissued.

1. Go to your workspace's billing page at https://railway.com/workspace/billing. Ensure you select the correct workspace using the Workspace Switcher in the top left corner.

2. Scroll to **Billing History**. For the invoice you want to reissue, click on the Gear icon next to it and select **Re-issue**.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1747010826/docs/cs-2025-05-12-08.14_3_lrlrz9.png"
alt="Screenshot of invoice options"
layout="intrinsic"
width={507} height={231} quality={100} />

3. Follow the instructions in the pop-up:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1747010832/docs/cs-2025-05-12-08.14_fyi63w.png"
alt="Screenshot of invoice re-issuance"
layout="intrinsic"
width={876} height={557} quality={100} />

Before you re-issue an invoice, please ensure your billing information is
up-to-date.

Once your invoice has been re-issued, it will contain the latest billing
information, and appear in your **Billing History**.

If you do not receive the re-issued invoice within 24 hours, please reach
out to us at station.railway.com.


# Refunds
Source: https://docs.railway.com/reference/pricing/refunds

Learn about Railwayâ€™s refund policy and how to request a refund if eligible.



## Requesting A Refund

You can request for a refund in Workspace Settings -> Billing under **Billing History**:

<Image
src="https://res.cloudinary.com/railway/image/upload/v1743469117/refund_e0pzvw.png"
alt="Screenshot of refund request button inside Account -> Billing"
layout="intrinsic"
width={1200} height={289} quality={100} />

If you do not see a refund button next to your invoice, you are ineligible for a refund. **This decision is final** and we are unable to issue refunds for invoices that have been deemed ineligible.

After a refund is issued,

- It may take up to 5~10 business days for the refund to be processed and reflected in your account
- Your subscription may be cancelled immediately by us
- Your services may be taken offline immediately

If you'd like to stop using Railway, please remove your projects and cancel your subscription immediately. See "How do I view/manage/cancel my subscription?" for further information.

## FAQs

### Why was my refund request denied?

Refunds are issued at our sole discretion. If your refund request was denied, it may be due to one of the following reasons:

- Your invoice contains resource usage costs. We generally do not issue refunds for resource usage, as those were resources you have consumed (in a manner akin to how a utility company charges for electricity or water)

- You have received a refund from Railway in the past

- You have violated our Fair Use Policy and/or Terms of Service


# AWS Marketplace
Source: https://docs.railway.com/reference/pricing/aws-marketplace

Learn about Railway's AWS Marketplace offering and pricing.



## Offering

Railway offers solutions, peering templates and deployment to AWS- while using your AWS vendor relationship. For large Enterprises, Railway can be an option for large engineering teams to significantly reduce operational overhead.

## Pricing Structure

Pricing for Railway through AWS Marketplace is based on contract duration. You can pay upfront or in installments according to your contract terms with the vendor. The contract includes:

- A specified quantity of usage for the contract duration
- Usage-based pricing for any usage exceeding the entitled amount
- Additional charges applied on top of the contract price for overages

## Contract Terms

### 12-Month Contract

The standard offering is a 12-month contract with the following terms:

- Base price: $10,000.00 per 12 months
- Overage rate: $1.00 per unit
- Private pricing agreements available through the Railway sales team

## Refund Policy

All fees are non-refundable and non-cancellable except as required by law.

## Getting Started

To purchase Railway through AWS Marketplace:

1. Visit the Railway listing on AWS Marketplace
2. Click "View purchase options"
3. Contact the Railway sales team
4. Complete the purchase through your AWS account

## Support

For questions about AWS Marketplace purchases or to discuss private pricing agreements, please contact our sales team.


# Migrate to Railway Metal
Source: https://docs.railway.com/reference/migrate-to-railway-metal

Learn how to move self-migrate your services over to Railway Metal

We will cover: how to initiate a migration, how to best prepare for a migration, and what mechanically happens when you initiate a migration of your services to Railway Metal.

## What is Railway Metal?

Railway Metal is the next generation of Railway's underlying infrastructure. It is built on hardware that we own and operate in datacenters around the world. You can get more information about Railway Metal on the parent documentation page here.

We announced on December 26th that we would be moving users to Railway Metal over a 6 month migration timeline.

**We expect all user workloads to be on Railway Metal by July 4th, 2025.**

Railway is **currently** initiating migrations of user workloads to Railway Metal regions at off-peak times per region.

As such, we advise our customers to move all of their workloads to Railway Metal to avoid Railway initiated downtime.

## What does a migration to Railway Metal entail?

A migration to Railway Metal is just like any deployment on Railway that would happen if you changed the region setting to a different value.

Railway is built region agnostically, meaning, the choice of region doesn't impact the availability of products or features depending on the region. In doing so, user workloads can be deployed into different geographic regions at will.

A migration to Railway Metal is a simple region change.

For Stateless deployments, meaning, a deployment with no volume- there is no downtime. Stateless deployments are just landing into a new region.

For services with a volume attached, or Stateful deployments, there is a brief 30-45 second period of downtime as the volume re-mounts into the new deployment. _This is exactly the same as the existing cross region deployment functionality that exists in Railway today._

## Initiating a migration

You can initiate a migration by selecting a region in the service settings pane with any label that has: Metal (New)

After you select the region, you will get the Staged Change anchored modal at the center top position of the project canvas.

By pressing: "Deploy", you initiate a migration to Railway Metal.

### What happens when my service is migrating?

When you change the value of the region within the service settings page, Railway is told to deploy into that region when the environment applies the staged change. In Railway's system, we process a deployment request from our queue triggering a build.

Depending on if the service is Stateful or Stateless- we then initiate one of two bespoke migration processes.

**For Stateless:** Railway rebuilds your application onto our Metal region, and after the container image is built, then is landed on a running host in one of our datacenters.

**For Stateful:** Railway detects if a volume is mounted to your service, if a volume is detected, Railway initiates a volume migration and holds the deployment until the volume is ready to be mounted within the new region. The process is as follows:

1. Railway initiates a backup of the volume for internal and customer use.
2. Railway makes the backup of the volume accessible on the project canvas in the original region.
3. Railway then copies the volume into the new region.
4. (Optional) If there are backups in the volume, we also copy those backups into the new region. _Depending on the number and size of backups, this incurs a time penalty on the migration._
5. Railway then confirms the integrity of data.
6. Railway attempts a build of the deployment after the volume is confirmed to be accessible in the new region.
7. Railway mounts to the volume in the new region after a successful build.

During the process, as of 2025/05/13 - Railway is able to report the transfer speed and progress of the volume migration to users.

### What happens to writes on the DB on migrations that I initiated?

Because Railway is copying the volume primitive using the same primitive that we use for the volume backup feature, writes persist until we unmount the running deployment of the DB. As such, you don't need to plan for downtime of your database except for the 30 to 40 seconds when a deployment remounts into the database.

## Preparing for migration

For production applications on Railway, we advise customers to make sure your service has configuration to ensure it's online between deployments. Railway by default, attempts to only deploy a new instance of your service only when your application is live and healthy. However, there are a number of additional measures you can take to increase resilience.

Before initiating a migration we recommend that users configure the following:

- Healthchecks
- Build and start commands
- Volume Backups
- Deployment overlap
  - Configured by setting RAILWAY_DEPLOYMENT_OVERLAP_SECONDS within the Railway service variable settings

We also advise users to make sure that:

- Data is being written to disk instead of the ephemeral container storage
  - If unsure, you can check by SSHing into the container via the Railway CLI and running ls on the mount point.
- On your DB, that the version is pinned to a major version instead of :latest on the image source
- You are able to backup and restore your data
- You test in a development environment before you migrate your production environment

Railway is not responsible for data loss that occurs on re-deployment for data on the container's ephemeral disk.

## Post-migration

The Railway team throughout this period is checking in with all customers to ensure:

- They receive their Metal seat discount
- Application performance is within customer expectations
- A great experience migrating with adequate communication

### Rollback

If you encounter any issues with your service after a Railway initiated upgrade, you can
rollback to the previous version by clicking Rollback button in the banner
above.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970652/docs/m4_rtxp2z.png"
alt="Automatic rollback"
layout="responsive"
width={1338} height={608} quality={80} />

### Manual rollback

To rollback manually, modify your service's Settings -> Deploy -> Regions
and select regions without the Metal tag.

<Image
src="https://res.cloudinary.com/railway/image/upload/v1736970930/docs/m3_kvwdgd.png"
alt="Manual rollback"
layout="responsive"
width={1140} height={560} quality={80} />

The Railway team during this period has doubled the amount of staffing around on-call and support to ensure this transition goes smoothly for our users.

Any issues, comments, and concerns- raise a thread on Station.


# Production Readiness Checklist
Source: https://docs.railway.com/reference/production-readiness-checklist

Ensure your app is production-ready with this comprehensive Railway checklist.

In this page, we'll explore key areas for production readiness, suggesting actions to take to address each one:

- Performance and Reliability
- Observability and Monitoring
- Quality Assurance
- Security
- Disaster Recovery

---

## Performance and Reliability

Ensuring your application is performant and reliable under changing conditions like load and external latency is critical for production-readiness. Consider taking the following actions to ensure your application is performant and reliable -

**&check; Serve your application from the right region**

- Deploying your application as close to your users as possible minimizes the number of network hops, reducing latency and improving performance.

  Railway offers multiple deployment regions around the globe.

  You may also consider implementing a CDN to cache server responses on an edge network.

**&check; Use private networking between services**

- When communicating between services over the public network, latency is introduced by the network hops that requests must make to reach their destination.

  To reduce latency, ensure communication between services in the same project and environment happens over the private network.

**&check; Configure a restart policy**

- Services can crash for different reasons, frequently due to unhandled exceptions in code, and it is important to implement a strategy to mitigate performance degradation and user impact.

  Ensure that you have properly configured your services restart policy.

**&check; Configure at least 2 replicas**

- If a service crashes or becomes unavailable due to a long-running request, your application could experience downtime or degraded performance.

  Increase the number of replicas to at least 2, so if one instance of your service crashes or becomes unavailable, there is another to continue handling requests.

**&check; Confirm your compute capacity**

- The vCPU and memory capacity of your services greatly impacts their ability to perform efficiently.

  The compute allocation for your services is handled automatically by Railway, and the limits are determined by your chosen subscription plan. You should review your plan limits and consider if upgrading is necessary to achieve the desired compute.

**&check; Consider deploying a database cluster or replica set**

- Data is critical to most applications, and you should ensure that the data layer in your stack is highly available and fault tolerant.

  Consider implementing a cluster or replica set, similar to the <a href="https://railway.com/template/q589Jl" target="_blank">Redis HA with Sentinel</a> template, to ensure that your data remains available even if one node becomes unstable.

  We are hard at work developing other templated solutions for more production-ready datastores, keep an eye on the template marketplace for more to become available.

---

## Observability and Monitoring

Observability and monitoring refers to tracking the health and performance of your application. Consider taking the following actions to ensure you are able to track your application health -

**&check; Get familiar with the log explorer**

- When researching an application issue across multiple services, it can be disruptive and time-consuming to move between log views for each service individually.

  Familiarize yourself with the Log Explorer so you can query logs across all of your services in one place.

**&check; Setup webhooks and email notifications**

- Ensure you are alerted if the deployment status of your services change.

  Enable email notifications in you Account Settings to receive these alerts via email.

  Setup webhooks to have the alerts sent to another system, like Slack or Discord.

_What's next for observability features in Railway? We have a ton of ideas, but we would love to hear yours in our <a href="https://station.railway.com/feature-request/better-logging-support-1e6f5676" target="_blank">community forums</a>._

---

## Quality Assurance

Quality assurance involves following practices to ensure changes to your application code meet quality standards before they are deployed to production. Consider the following actions to ensure you're set up for success -

**&check; Implement check suites**

- Common practice is to run a suite of tests, scans, or other automated jobs against your code before it is merged into production. You may want to configure your deployments to wait until those jobs have completed successfully before triggering a build.

  Enable check suites to have Railway wait for your GitHub workflows to complete successfully before triggering a deployment.

**&check; Use environments**

- Maintaining separate environments for production and development is good practice for controlling changes in a production environment.

  Consider setting up environments to properly test changes before merging to production.

  Additionally, PR environments can be enabled to create environments when PRs are opened on your production branch.

**&check; Use config as code**

- Along with your source code, you can maintain your Railway configuration in a json or toml file, enabling you to keep track of changes, just as you do with your source code.

  Take advantage of config as code to control and track changes to your Railway configuration.

**&check; Understand the deployment rollback feature**

- Introducing breaking changes to your application code is sometimes unavoidable, and it can be a headache reverting to previous commits.

  Be sure to check out the deployment rollback feature, in case you need to rollback to a previous deployment.

---

## Security

Protecting your application and user data from malicious threats and vulnerabilities is mission-critical in production applications. Consider the following for peace of mind -

**&check; Use private networking**

- The easiest way to protect your services from malicious threats, is to keep them unexposed to the public network.

  Secure communication between services in the same project and environment by using the private network.

**&check; Implement a security layer**

- While Railway does have protections in place at the platform level, we do not currently offer a configurable service for users' applications.

  Consider using a service like Cloudflare that offers both WAF and DDoS mitigation, to protect your services against web threats and ensure availability and performance.

  _In the future, we would love to offer a native security solution. If you agree, <a href="https://station.railway.com/feature-request/implement-a-waf-firewall-security-54fe2aaf" target="_blank">let us know</a>._

---

## Disaster Recovery

Being prepared for major and unexpected issues helps minimize downtime and data loss. Consider taking the following actions to ensure you are prepared -

**&check; Set up an instance of your application in two regions**

- In the event of a major disaster, an entire region may become unavailable.

  Using deployment regions, you can deploy an entire instance of your application in another region.

  To save on cost of running a separate instance of your application, use App Sleep to turn down resource usage on the inactive services.

**&check; Regularly back up your data**

- Data is critical to preserve in many applications. You should ensure you have a backup strategy in place for your data.

  Enable and configure backups for your services with volumes to ensure you can restore your data in case of any data loss.

---

## Conclusion

Using a mix of native features and external tools, we hope you can feel confident that your applications on Railway meet the highest standards of performance, reliability, and security.

Remember, our team is always here to assist you with solutions. Reach out in <a href="https://discord.com/channels/713503345364697088/1006629907067064482" target="_blank">Discord</a> or over email at team@railway.com for assistance.

Finally, as suggested on several sections above, we are working tirelessly to give you the best experience imaginable on Railway. If you have requests or suggestions, please <a href="https://station.railway.com" target="_blank">let us know</a>!



# Maturity
Source: https://docs.railway.com/maturity

# Philosophy
Source: https://docs.railway.com/maturity/philosophy

Explore Railwayâ€™s core philosophy and the principles that drive our platform.

We design and develop our product features to serve what we consider to be the three primary stages of software development:

- Development
- Deployment
- Diagnosis

Most developer-oriented products attempt to target one or more stages within the software development cycle. Railway provides solutions for developers for all of these stages, whereas some vendors focus on specific stages.

Railway is a company staffed with people who know developers would prefer to use tools they are familiar with. We believe software should be "take what you need, and leave what you don't." As a result, we are comfortable recommending additional vendors if they might acutely meet their needs. Our goal is for your unique need to be served so you can focus on delivering for your customers.

Companies should be as upfront as possible about their product and offerings to help you decide what is best for your team and users.

Let's talk about the number one use case: delivering apps to users in a Production environment. Railway, the company, is sustainable, building our product, team, and company to last as long as your projects.

## Objective

The goal of this section is to describe the processes, internal and external that companies have requested in our years of operation to help them build confidence to determine if Railway is a good fit for their company. Railway maintains a policy to be forthcoming and frank at all times. We would rather have a developer make the correct choice for their company than to adopt Railway and then come to regret that decision.

If you have any additional questions or if you require any additional disclosure you can contact us to set up a call at team@railway.com.

## Product Philosophy

Railway is focused on building an amazing developer experience. Our goal is to enable developers to deploy their code and see their work in action, without thinking about CI/CD, deployments, networking, and so forth, until they need to.

### Take What You Need

To achieve our goal, we've designed Railway to "just work", with all the necessary magic built in to achieve that. Railway at a high level reads your code repo, makes a best guess effort to build it into an OCI compliant image, and runs the image with a start command.

- Have a code repository but have yet to think about deployment? We got you. Connect your code repository and let Railway take care of the rest.
- Already built the perfect Dockerfile? Bring it. If you have a Dockerfile in your repo, we'll find it and use that to build your image.

If you've outgrown the "magic" built into deployment platforms, or are suspicious of things that are just too magical, we are happy to provide a high level overview of our architecture.

### Leave What You Don't

Streamlined deployment workflows and sane defaults are inherited by every project in Railway out of the box; but as a team of engineers, we at Railway are very aware that what works for one project does not always work for another. Or sometimes, you just need to be in control - maybe you already have a workflow you like, or maybe you need to layer Railway into existing infrastructure, and abstractions only get in your way.

That's why we've designed the platform for flexibility, wherever you need it.

On Railway, you can use the default pattern for deployment or opt to use vendor. In fact, we will even support you in your effort to integrate Railway in a unique way. Here are a couple of use cases we've helped customers take advantage of -

- Deploying to Railway from Gitlab CI/CD
- Supporting the development of a Terraform provider
- Region based routing to workloads via Cloudflare

We love working with our customers to solve interesting use cases. If you're not seeing a track for you, get in touch at team@railway.com and we'll find it!

## High-level Architecture

As mentioned before, Railway at a high level takes your code, builds it, and throws it on running infrastructure on GCP. At a granular level Railway relies on a few systems to maintain workloads.

- Build Layer
  - Where archived folders of code or a Dockerfile (via GitHub or railway up) is sent to be built into an image
  - Nixpacks: the OSS software that reads your code and builds it via Nix
  - Image Registry: either via Dockerhub/GitHub packages, or a previously built image from Railway's Build servers
- Deployment Layer
  - Where images are ran in containers, images are pulled from the Build Layer
  - Databases on Railway are images + volumes mounted on a machine
  - Cron services are containers ran on a defined schedule
- Routing Layer
  - This is the system that Railway maintains that routes requests into your running containers and provides private networks to suites of containers.
- Logging Layer
  - A suite of machines networked running Clickhouse that store container logs. This is accessed when you open the service logs pane.
- Dashboard Layer
  - Infrastructure and code that is used to manage the above layers.
  - This also includes any monitors that Railway uses to maintain the state of the Deployment Layer to maintain application state. (ex. Removing a deployment.)

Your code will either be in some, or all steps depending on the amount of Railway that you choose to adopt.

### Operational Procedures

Railway uses a suite of alerting vendors, additional internal tools, and PagerDuty to ensure uptime of our services described above. You can see Railway's uptime on our Instatus page. Operational incident management reports and RCAs are available by request for those on an Enterprise plan.

### Do I have to change how I write code?

No, Railway is a deployment platform that works with your existing code. We don't require you to change how you write code or use any specific frameworks. We support all languages and frameworks that can be run in a Docker container or within Nixpacks.

### Is Railway serverless?

No, services on Railway are deployed in stateful Docker containers. The old deployments are removed on every new deploy.

We do have a feature, App Sleeping, that allows you to configure your service to "sleep" when it is inactive, and therefore will stop it from incurring usage cost while not in use.

## Book a Demo

If you're looking to adopt Railway for your business, we'd love to chat and ensure your questions are answered. Click here to book some time with us.


# Use Cases
Source: https://docs.railway.com/maturity/use-cases

Explore real-world use cases for deploying and managing applications on Railway.

As mentioned in our philosophy document. Railway will make a best effort to provide all the information a developer needs to make the best choice for their workload.

## Is Railway Production Ready?

Many of our customers use Railway to reliably deploy their applications to customers at scale. With that said, Production standards are going to be different depending on what your users expect. We have companies that use Railway in a variety of different verticals such as:

- Enterprise SaaS
- Consumer Social
- Education
- E-Commerce
- Crypto
- ML/AI
- Agencies

Companies on Railway range from hobby projects, to extremely fast growing startups, to publicly traded companies. Railway has been incrementally adopted from using the platform as a developer's scratchpad before writing Terraform to hand off to an Ops. team or being implemented end to end.

Railway's been in operation for now for more than three years and we have served billions of requests, with 100s of millions of deploys serving millions of end-users simultaneously.

## Railway Scale

All of these verticals deploy workloads that may require high bandwidth operations or intensive compute.

However, service scale on the platform is not unbounded. As a foundational infrastructure company, we understand that customers may outpace our pace of improvement for the platform. Even though 32 vCPU and 32 GB of memory sounds like a lot (with up to 20 replicas) on the Pro plan, when faced with hyper-growth: throwing more resources at the issue might be your best bet until long term optimizations can be made by your team.

Railway will gladly bump up your service limits within your tier of service to meet your needs. Even so, we will be frank and honest if you may need to seek elsewhere to augment your workloads with extra compute. If your compute needs outpace our Pro offering, consider our Enterprise plans where we offer even greater limits and capacity planning, email us to learn more, or click here to schedule some time to chat.

### Databases

We have customers using our databases for their production environment with no issue. Railway's databases are optimized for a batteries included development experience. They are good for applications that are prioritizing velocity and iteration speed over scale.

Our databases are provided with no SLAs, are not highly available, and scale only to the limits of your plan. We don't think they are suitable for anything mission-critical, like if you wanted to start a bank.

We advise developers to:

- Configure backups
- Run-book and restore their backups
- Configure secondaries to connect to in-case of a disaster situation

Included in our planned near-term work for databases on Railway are additional database metrics, and SSH access into the running database.

As mentioned before: we don't believe in vendor lock-in here at Railway, if your needs outpace us, consider other vendors like PlanetScale (for MySQL) or Cockroach (for Postgres).

### Metrics

Railway provides up to 7 days worth of data on service information such as:

- CPU
- Memory
- Disk Usage
- Network

We also overlay commit and deployment behavior to correlate issues with application health to deployments. This is on top of the service logs that are continually delivered to users viewing a particular deployment of a service.

For service logs, we store logs for up to 90 days for Pro plan workspaces.

Included in our planned near-term work for logging and observability on Railway are improvements to structured logging, and OpenTelemetry compatible endpoints.

It is common for teams who wish to have additional observability to use an additional monitoring tool that maintains a longer time horizon of data such as New Relic, Sentry, or Datadog. Within projects, deploying a Datadog Agent is as easy as deploying the template and providing your Datadog API Keys.

### Networking

Railway doesn't have a hard bandwidth limit to the broader internet.

We may throttle your outbound bandwidth and reach out to you when it exceeds 100GB/month to ensure the legitimacy of your workloads. If you need to control where your traffic is allowed to come from such as setting up firewall rules, we recommend setting up Cloudflare or an external load balancer/L7 application firewall to handle it.

Private networking bandwidth is un-metered.

We intend to provide advanced traffic-shaping controls within Railway in the future.

### Service Level Objectives

Railway does meet SLOs for companies who have greater need for incident, support, and business planning responsiveness. We provide this via Business Class, offered as an add-on to Pro plans and included in all Enterprise plans. More info.

### Will Railway exist in 10 years?

A common question we get in conversations with (rightly) skeptical developers is the above question. Most documentation pages don't address the meta question of a company's existence but how we run _our_ business affects yours.

The short and simple answer is: **Yes**.

Railway aims to exist for a very long time. Railway has presence on existing public clouds, while also building out presence on co-location providers. As a company, we have been structured sustainably with a first principles approach to every expense while growing sustainably.

### Unsupported Use-Cases

Unfortunately, our platform isn't yet well-equipped to handle the following verticals that require extensive Gov't certification or GPU compute:

- Government
- Traditional Banking
- Machine Learning Compute

## General Recommendations

A document like this can only go so far. We have a standing invitation for any team who needs an extended scale use-case to reach out to us directly by e-mailing team@railway.com, or via our Discord server. You can also schedule some time with us directly by clicking here.

We would be happy to answer any additional questions you may have.


# Compliance
Source: https://docs.railway.com/maturity/compliance

Learn about Railway's compliance standards and how we ensure security and regulatory adherence.

Companies choose Railway so that they can speed up their development velocity while also maintaining their security and compliance posture.

We are happy to sign NDAs with your company to provide additional information about our security and compliance practices. Please reach out to us at team@railway.com to get started, or click here to book some time to chat.

You can request to view our audit, compliance, security, and regulatory documents and processes on our Trust Center at trust.railway.com.

## Certifications

We know that your businesses need to develop strong and lasting relationships with your vendors to build confidence that we can be trusted to deliver your workloads. Part of that is through certifications, audits, and continual refinement of our practices. Railway aims to comply with all the distributions of workloads and privacy procedures.

### SOC 2 Type II and SOC 3

Railway is SOC 2 Type II certified and SOC 3 certified.

Customers who are in the process of securing SOC 2 certification can request a copy of the Railway security audit on our Trust Center.

### HIPAA BAA

Railway follows a shared responsibility model for HIPAA compliance and PHI. Railway will make its best effort to advise your company on setting up encryption for your data, auditing the storage of keys, establishing access control, and ensuring secure storage of sensitive patient data. When a BAA is in effect, the Railway team will no longer be able to directly access your running workloads.

HIPAA BAA is an add-on with a paid monthly spend threshold. All pricing goes towards your usage on Railway. Monthly thresholds for addons is found in our committed spend pricing.

If your company needs a BAA, you can contact our solutions team at team@railway.com, or click here to schedule some time to chat.

We are working on operationalized BAAs and continually gathering requirements for health-focused workloads for Enterprises. You can share your feedback in Central Station.

## Privacy

Railway is committed to protecting the privacy of our users. We understand that when working with user code and data, it is important to have a clear understanding of how we handle your data. Railway, on behalf of our users, may remove offending workloads but at no point will a Railway team member modify your application without your expressed permission through an approved communication channel.

Click here to see our Privacy Policy.

## GDPR Compliance - Data Processing Agreement (DPA)

Railway provides a Data Processing Agreement (DPA) to help customers comply with GDPR requirements when processing personal data through our platform. If you operate a business in the EU or process personal data of EU residents, you may need to execute a DPA with Railway to ensure compliance with GDPR Article 28 requirements for data processor relationships.

You can access and execute Railway's standard DPA through our self-service link: Sign Railway's DPA

You can also review Railway's standard DPA terms at railway.com/legal/dpa.

## VAT Tax ID and Address

Customers in the EU may need to add their VAT Tax ID to their invoices for compliance and reporting purposes.

You can add your VAT Tax ID and address on Railway in your Workspace settings -> Billing -> Manage Subscription.

If you have multiple workspaces, you need to add your VAT Tax information to each respective Workspace's Subscription.

After adding your information, it will appear on your future invoices.

## EU Dora

For European organizations in finance that need to comply with EU Dora - Railway is willing to provide documents after a click through NDA that describe disaster recovery procedures, uptime statistics, and IT controls for organizations to who need to submit compliance documents to local regulators. You can get information on our Trust Page


# Incident Management
Source: https://docs.railway.com/maturity/incident-management

Learn how Railway handles incident management.

Railway understands the importance of effective incident management procedures. We do what we can to minimize downtime, mitigate the impact of incidents, and ensure the smooth operation of our systems. In the interest of transparency, we publish as much of our procedure to keep our customers in the know on how we handle and learn from incidents.

## Monitoring + Reporting

Railway has a robust monitoring system in place to proactively detect and address any potential incidents. We continuously monitor our infrastructure, including servers, networks, and applications, to ensure their smooth operation. By monitoring key metrics and performance indicators, we can identify any anomalies or potential issues before they escalate into full-blown incidents.

However, it's important to note that while we strive to stay ahead of incidents, there may be situations where unforeseen issues arise. In such cases, we rely on qualitative customer feedback to help us identify and address any issues promptly. We encourage our customers to report any problems they encounter through our Central Station, Slack, or Discord.

## Status Page + Uptime

Railway's uptime and incident retrospective can be accessed on the Railway Instatus page at https://railway.instatus.com/. On this page, you can view the historical uptime of Railway's systems and services. Additionally, you can find detailed information about past incidents, including retrospectives that provide insights into how incidents were handled and what measures were taken to prevent similar issues in the future.

For Enterprise customers, we offer SLOs and guarantees of service that may not be represented on the uptime dashboard.

## Incident Severity

Railway catalogues incident's in the following buckets.

- **High**: the incident is potentially catastrophic to Railway Corporation and/or disrupts
  Railway Corporationâ€™s day-to-day operations; violation of contractual requirements is likely. Ex. Any business level impact to 25 percent of our customers for one hour or more. All incidents within this severity get public communications.
- **Medium**: the incident will cause harm to one or more business units within Railway
  Corporation and/or will cause delays to a customer business unitâ€™s activities.
- **Low**: the incident is a clear failure of a component, but will not substantively impact the business. Railway still performs retrospectives within this severity.

### Responsible Disclosure

Enterprise customers get Root Cause Analysis, and we attempt to publish event retrospectives on https://blog.railway.com/engineering


# Compare to Heroku
Source: https://docs.railway.com/maturity/compare-to-heroku

Compare Railway and Heroku on infrastructure, pricing model and deployment experience.

- You can deploy your app from a Docker image or by importing your appâ€™s source code from GitHub.
- Services are deployed to a long-running server.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Create isolated preview environments for every pull request.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Custom domains with fully managed TLS, including wildcard domains.
- Run arbitrary commands against deployed services (SSH).

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### Heroku

Heroku follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnâ€™t scale down quickly enough, leaving you paying for unused resources.

Beyond scaling, there are other notable limitations. Heroku doesnâ€™t natively support multi-region deployments. To achieve that, you must create separate instances in different regions and set up an external load balancer to route traffic appropriately.

Furthermore, services deployed to the platform do not offer persistent data storage. Any data written to the local filesystem is ephemeral and will be lost upon redeployment, meaning you'll need to integrate with external storage solutions if your application requires data durability.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 32 vCPU and 32 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 96 vCPU and 96 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâ€™re running.

## Pricing

### Heroku

Heroku follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!Heroku instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnâ€™t have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâ€™re overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

Additionally, Heroku runs on AWS, so the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for:

- Unlocking additional features (e.g. private networking is a paid enterprise add-on).
- Pay extra for resources (e.g., bandwidth, memory, CPU and storage).

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donâ€™t need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâ€™ll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

Finally, Railwayâ€™s infrastructure runs on hardware thatâ€™s owned and operated in data centers across the globe. This means youâ€™re not going to be overcharged for resources.

## Dashboard experience

### Heroku

Herokuâ€™s unit of deployment is the app, and each app is deployed independently. If you have a different infrastructure components (e.g. API, frontend, background workers, etc.) they will be treated as independent entities. There is no topâ€‘level â€œprojectâ€ object that groups related apps.

Additionally, Heroku does not support shared environment variables across apps. Each deployed app has its own isolated set of variables, making it harder to manage secrets or config values shared across multiple services.

!Heroku dashboard

### Railway

Railwayâ€™s dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâ€™re related to one other.

You can also share environment variables between services, streamlining config management across complex projects with multiple components.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâ€™ll earn a 50% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**                | **Heroku**                                                                                       | **Railway**                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Scaling Model**           | Instance-based                                                                                   | Usage-based                                                                                                      |
| **Vertical Scaling**        | Manual upgrade to larger instance sizes                                                          | Auto-scales to the plan's limits without manual intervention                                                     |
| **Horizontal Scaling**      | Manual or threshold-based autoscaling; requires setting CPU/memory limits                        | Add replicas manually; traffic routed automatically across replicas and regions                                  |
| **Autoscaling Flexibility** | Threshold-based, needs manual tuning                                                             | Fully automated; scales based on workload                                                                        |
| **Multi-region Support**    | Not natively supported; must set up separate apps + external load balancer                       | Built-in; auto-routes traffic to nearest region and balances load across replicas                                |
| **Persistent Storage**      | Not supported; ephemeral file system only                                                        | Persistent volumes are supported                                                                                 |
| **Private Networking**      | Available with paid Enterprise add-on                                                            | Included at no extra cost                                                                                        |
| **Pricing Model**           | Fixed monthly pricing per instance size. Manual tuning required to avoid under/over-provisioning | Usage-based: Charged by active compute time Ã— resource size (CPU & RAM). Inherently optimized by dynamic scaling |
| **Infrastructure Provider** | AWS-based; higher base costs                                                                     | Railway-owned global infrastructure; lower costs and no feature gating                                           |
| **Dashboard UX**            | Traditional app-based dashboard; each app is independent                                         | Visual, collaborative canvas view for full projects with interlinked services                                    |
| **Project Structure**       | No concept of grouped services/projects                                                          | Groups all infra components visually under a unified project view                                                |
| **Environment Variables**   | Isolated per app                                                                                 | Isolated per app but can be shared across services within a project                                              |
| **Wildcard Domains**        | Not supported; manual configuration needed per subdomain                                         | Fully supported; configure at the project level                                                                  |

## Migrate from Heroku to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. â€œChoose Deploy from GitHub repoâ€, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã— maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Render
Source: https://docs.railway.com/maturity/compare-to-render

Compare Railway and Render on infrastructure, pricing model and dashboard experience.

- You can deploy your app from a Docker image or by importing your appâ€™s source code from GitHub.
- Multi-service architecture where you can deploy different services under one project (e.g. a frontend, APIs, databases, etc.).
- Services are deployed to a long-running server.
- Services can have persistent storage via volumes.
- Public and private networking are included out-of-the-box.
- Healthchecks are available to guarantee zero-downtime deployments.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Create isolated preview environments for every pull request.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Support for wildcard domains.
- Custom domains with fully managed TLS.
- Schedule tasks with cron jobs.
- Run arbitrary commands against deployed services (SSH).
- Shared environment variables across services.

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### Render

Render follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnâ€™t scale down quickly enough, leaving you paying for unused resources.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 32 vCPU and 32 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 96 vCPU and 96 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâ€™re running.

## Pricing

### Render

Render follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!Render instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnâ€™t have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâ€™re overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

Additionally, Render runs on AWS and GCP, so the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for:

- Unlocking additional features (e.g. horizontal autoscaling and environments are only available on paid plans).
- Pay extra for resources (e.g., bandwidth, memory, CPU and storage).
- Pay for seats where each team member you invite adds a fixed monthly fee regardless of your usage.

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donâ€™t need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâ€™ll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

Finally, Railwayâ€™s infrastructure runs on hardware thatâ€™s owned and operated in data centers across the globe. This means youâ€™re not going to be overcharged for resources.

## Dashboard experience

### Render

Renderâ€™s dashboard offers a traditional dashboard where you can view all of your projectâ€™s resources.

!Render dashboard

### Railway

Railwayâ€™s dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâ€™re related to one another.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâ€™ll earn a 50% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**             | **Render**                                                                                     | **Railway**                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Scaling Model**        | Instance-based                                                                                 | Usage-based                                                                                                                                |
| **Vertical Scaling**     | Manual upgrade to larger instance sizes.                                                       | Scales to plan limits automatically                                                                                                        |
| **Horizontal Scaling**   | Manually add/remove instances or autoscaling (based on CPU/memory thresholds); requires tuning | Manually add replicas, traffic is routed automatically across regions and replicas                                                         |
| **Multi-region Support** | Not supported                                                                                  | Built-in support; traffic routed to nearest region                                                                                         |
| **Pricing Model**        | Fixed monthly pricing per instance size. Seat-based pricing                                    | Usage-based: charged by active compute time Ã— compute size. You don't pay for seats. You can invite your whole team for no additional cost |
| **Cost Optimization**    | Requires tuning to avoid over/under-provisioning                                               | Inherently optimized. Pay only for used compute                                                                                            |
| **Infrastructure**       | Runs on AWS and GCP; feature access and resources cost more                                    | Railway-owned global infrastructure, lower unit costs and features aren't gated                                                            |
| **Dashboard UX**         | Traditional dashboard to view project resources                                                | Real-time collaborative canvas with visual infra relationships. Template directory for 1-click deployments                                 |

## Migrate from Render to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. â€œChoose Deploy from GitHub repoâ€, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã— maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Fly
Source: https://docs.railway.com/maturity/compare-to-fly

Compare Railway and Fly.io on deployment model, scaling, pricing and developer workflow.

- You can deploy your app from a Docker image or by importing your appâ€™s source code from GitHub.
- Apps are deployed to a long-running server.
- Apps can have persistent storage through volumes.
- Public and private networking are included out-of-the-box.
- Multi-region deployments.
- Both platformsâ€™ infrastructure runs on hardware thatâ€™s owned and operated in data centers across the globe.
- Healthchecks to guarantee zero-downtime deployments.

That said, there are differences between both platforms when it comes to the overall developer experience that can make Railway a better fit for you.

## Deployment model & scaling

### Fly

When you deploy your app to Fly, your code runs on lightweight Virtual Machines (VMs) called Fly Machines. Each machine needs a defined amount of CPU and memory. You can either choose from preset sizes or configure them separately, depending on your appâ€™s needs.

Machines come with two types of virtual CPUs: shared and performance.

Shared CPUs are the more affordable option. They guarantee a small slice of CPU time (around 6%) but can burst to full power when thereâ€™s extra capacity. This makes them ideal for apps that are mostly idle but occasionally need to handle trafficâ€”like APIs or web servers. Just keep in mind that heavy usage can lead to throttling.

Performance CPUs, by contrast, give you dedicated access to the CPU at all times. Thereâ€™s no bursting or throttling, making them a better choice for workloads that require consistent, high performance.

**Scaling your app**

When scaling your app, you have one of two options:

- Scale a machineâ€™s CPU and RAM: you will need to manually pick a larger instance. You can do this using the Fly CLI or API.
- Increase the number of running machines. There are two options:
  - You can manually increase the number of running machines using the Fly CLI or API.
  - Fly can automatically adjust the number of running or created Fly Machines dynamically. Two forms of autoscaling are supported.
    - Autostop/autostart Machines: You create a â€œpoolâ€ of Machines in one or more regions and Flyâ€™s Proxy start/suspend Machines based on incoming requests. With this option, Machines are never created or deleted, you need to specify how many machines your app will need.
    - Metrics-based autoscaling: this is not supported out-of-the-box. However, you can deploy fly-autoscaler which polls metrics and automatically creates/deletes or starts/stops existing Machines based on the metrics you define.

!Scaling your app on Fly.io

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 32 vCPU and 32 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 96 vCPU and 96 GB RAM.

Replicas can be placed in different geographical locations. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region.

<video
src="https://res.cloudinary.com/railway/video/upload/v1753083716/docs/replicas_dmvuxp.mp4"
muted
autoplay
loop
controls>

Add replicas to your service

</video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâ€™re running.

## Pricing

### Fly

Fly charges for compute based on two primary factors: machine state and CPU type (shared vs. performance).

Machine state determines the base charge structure. Started machines incur full compute charges, while stopped machines are only charged for root file system (rootfs) storage. The rootfs size depends on your OCI image plus containerd optimizations applied to the underlying file system.

Pricing for different preset sizes is available in Fly's documentation. You can get a discount by reserving compute time blocks. This requires paying the annual amount upfront, then receiving monthly credits equal to the "per month" rate. Credits expire at month-end and do not roll over to subsequent months. The trade-off is you might end up paying for unused resources.

!Fly compute presets pricing

One important consideration is that Fly Machines incur cost based _on running time_. Even with zero traffic or resource utilization, you pay for the entire duration a machine remains in a running state. While machines can be stopped to reduce costs, any time spent running generates full compute charges regardless of actual usage.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes.

If you spin up multiple replicas for a given service, youâ€™ll only be charged for the active compute time for each replica.

!Railway autoscaling

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

## Developer Workflow & CI/CD

### Fly

Fly provides a CLI-first experience through flyctl, allowing you to create and deploy apps, manage Machines and volumes, configure networking, and perform other infrastructure tasks directly from the command line.

However, Fly lacks built-in CI/CD capabilities. This means you can't:

- Create isolated preview environments for every pull request.
- Perform instant rollbacks.

To access these features, you'll need to integrate third-party CI/CD tools like GitHub Actions.

Similarly, Fly doesn't include native environment support for development, staging, and production workflows. To achieve proper environment isolation, you must create separate organizations for each environment and link them to a parent organization for centralized billing management.

For monitoring, Fly automatically collects metrics from every application using a fully-managed Prometheus service based on VictoriaMetrics. The system scrapes metrics from all application instances and provides data on HTTP responses, TCP connections, memory usage, CPU performance, disk I/O, network traffic, and filesystem utilization.

The Fly dashboard includes a basic Metrics tab displaying this automatically collected data. Beyond the basic dashboard, Fly offers a managed Grafana instance at fly-metrics.net with detailed dashboards and query capabilities using MetricsQL as the querying language. You can also connect external tools through the Prometheus API.

!fly-metrics.net

Advanced features like alerting and custom dashboards require working with multiple tools and query languages, creating a learning curve for teams wanting sophisticated monitoring capabilities.

Additionally, Fly doesn't support webhooks, making it more difficult to build integrations with external services.

### Railway

Railway follows a dashboard-first experience, while also providing a CLI. In Railway, you create a project for each app youâ€™re building. A project is a collection of services and databases. This can include frontend, API, background workers, API, analytics database, queues and so much more. All in a unified deployment experience that supports real-time collaboration.

!Railway architecture

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâ€™ll earn a 50% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video
src="https://res.cloudinary.com/railway/video/upload/v1753083712/docs/railway.com_templates_zcydjb.mp4"
muted
autoplay
loop
controls>

Railway templates

</video>

You also get:

- First-class support for environments so you can isolate production, staging, development, testing, etc.
- GitHub integration with support for provisioning isolated preview environments for every pull request.
- Ability to do instant rollbacks for your deployments.

Each Railway project includes a built-in observability dashboard that provides a customizable view into chosen metrics, logs, and data all in one place

Screenshot of the Observability Dashboard

Finally, Railway supports creating webhooks which allow external services to listen to events from Railway

!Webhooks

## Summary

| Category                 | Railway                                                                            | Fly.io                                                                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Scaling                  | Auto-scaling included (no manual config); supports horizontal scaling via replicas | Manual vertical/horizontal scaling or horizontal autoscaling (via fly-autoscaler); two autoscaling options (autostop/start, metrics-based) |
| Compute Pricing          | Usage-based where youâ€™re only billed for active compute time                       | Based on machine uptime (started = full price); unused time still billed unless stopped                                                      |
| CI/CD Integration        | Built-in GitHub integration with preview environments and instant rollbacks        | No built-in CI/CD; requires third-party tools like GitHub Actions                                                                            |
| Environments Support     | First-class support for multiple environments (dev, staging, prod, etc.)           | Requires creating separate orgs per environment                                                                                              |
| Monitoring & Metrics     | Built-in observability dashboard (metrics, logs, data all in one place)            | Prometheus-based metrics + optional Grafana (fly-metrics.net) for deep dives                                                               |
| Webhooks & Extensibility | Webhook support for integrations                                                   | No support for outbound webhooks                                                                                                             |
| Developer Experience     | Dashboard-first, supports real-time team collaboration, CLI available              | CLI-first (flyctl) for all management tasks                                                                                                |

## Migrate from Fly.io to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

1. â€œChoose Deploy from GitHub repoâ€, connect your GitHub account, and select the repo you would like to deploy.

   !Railway Deploy New Project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway Variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

For larger workloads or specific requirements, you can book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã— maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to Vercel
Source: https://docs.railway.com/maturity/compare-to-vercel

Compare Railway and Vercel on infrastructure, pricing model and deployment experience.

- Git-based automated deployments with support for instant rollbacks.
- Automatic preview environments.
- Built-in observability.
- Autoscaling resources with usage-based pricing.

That said, there are fundamental differences between both platforms, and certain use cases where Railway is a better fit.

## Understanding the underlying infrastructure and ideal use cases

### Vercelâ€™s infrastructure

Vercel has developed a proprietary deployment model where infrastructure components are derived from the application code (see Framework-defined infrastructure).

At build time, application code is parsed and translated into the necessary infrastructure components. Server-side code is then deployed as serverless functions, powered by AWS under the hood.

To handle scaling, Vercel creates a new function instance for each incoming request with support for concurrent execution within the same instance (see Fluid compute). Over time, functions scale down to zero to save on compute resources.

!https://vercel.com/blog/introducing-fluid-compute

This deployment model abstracts away infrastructure, but introduces limitations:

- Memory limits: the maximum amount of memory per function is 4GB.
- Execution time limit: the maximum amount of time a function can run is 800 seconds (~13.3 minutes).
- SizeÂ (after gzip compression): the maximum is 250 MB.
- Cold starts: when a function instance is created for the first time, thereâ€™s an amount of added latency. Vercel includes several optimizations, which reduces cold start frequency but wonâ€™t completely eliminate them.

If you plan on running long-running workloads such as:

- Data Processing: ETL jobs, large file imports/exports, analytics aggregation.
- Media Processing: Video/audio transcoding, image resizing, thumbnail generation.
- Report Generation: Creating large PDFs, financial reports, user summaries.
- DevOps/Infrastructure: Backups, CI/CD tasks, server provisioning.
- Billing & Finance: Usage calculation, invoice generation, payment retries.
- User Operations: Account deletion, data merging, stat recalculations.

Or if you plan on running workloads that require a persistent connection such as:

- Chat messaging: Live chats, typing indicators.
- Live dashboards: Metrics, analytics, stock tickers.
- Collaboration: Document editing, presence.
- Live tracking: Delivery location updates.
- Push notifications: Instant alerts.
- Voice/video calls: Signaling, status updates.

Then deploying your backend services to Vercel functions will not be the right fit.

### Railwayâ€™s infrastructure

Railway's underlying infrastructure runs on hardware thatâ€™s owned and operated in data centers across the globe. By controlling the hardware, software, and networking stack end to end, the platform delivers best-in-class performance, reliability, and powerful features, all while keeping costs in check.

!Railway regions

Railway uses a custom builder that takes your source code or Dockerfile and automatically builds and deploys it, without needing configuration.

Your code runs on a long-running server, making it ideal for apps that need to stay running or maintain a persistent connection.

All deployments come with smart defaults out of the box, but you can tweak things as needed. This makes Railway flexible across different runtimes and programming languages.

Each service you deploy can automatically scale up vertically to handle incoming workload. You also get the option to horizontally scale a service by spinning up replicas. Replicas can be deployed in multiple regions simultaneously.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâ€™re running.

## Pricing model differences

Both platforms follow a usage-based pricing model, but are different due to the underlying infrastructure.

### Vercel

Vercel functions are billed based on:

- Active CPU: Time your code actively runs in milliseconds
- Provisioned memory: Memory held by the function instance, for the full lifetime of the instance
- Invocations: number of function requests, where youâ€™re billed per request

Each pricing plan includes a certain allocation of these metrics.

This makes it possible for you to pay for what you use. However, since Vercel runs on AWS, the unit economics of the business need to be high to offset the cost of the underlying infrastructure. Those extra costs are then passed down to you as the user, so you end up paying extra for resources such as bandwidth, memory, CPU and storage.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes.

!railway usage-based pricing

If you spin up multiple replicas for a given service, youâ€™ll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This makes it ideal for sporadic or bursty workloads, giving you the flexibility of a full server with the cost efficiency of serverless, with the benefit of only paying when your code is running.

## Deployment experience

### Vercel

**Managing multiple services**

In Vercel, a project maps to a deployed application. If you would like to deploy multiple apps, youâ€™ll do it by creating multiple projects.

!Vercel dashboard

**Integrating your application with external services**

If you would like to integrate your app with other infrastructure primitives (e.g storage solutions for your applicationâ€™s database, caching, analytical storage, etc.), you can do it through the Vercel marketplace.

!Vercel marketplace

This gives you an integrated billing experience, however managing services is still done by accessing the original service provider. Making it necessary to switch back and forth between different dashboards when youâ€™re building your app.

### Railway

**Managing projects**

In Railway, a project is a collection of services and databases. This can include frontend, API, background workers, API, analytics database, queues and so much more. All in a unified deployment experience that supports real-time collaboration.

!Railway canvas

**Databases**

Additionally, Railway has first-class support for Databases. You can one-click deploy any open-source database:

- Relational: Postgres, MySQL
- Analytical: Clickhouse, Timescale
- Key-value: Redis, Dragonfly
- Vector: Chroma, Weviate
- Document: MongoDB

Check out all of the different storage solutions you can deploy.

Template directory

Finally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâ€™ll earn a 50% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| Feature                | Railway                                                             | Vercel                                                 |
| ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ |
| Infrastructure Model   | Long-running servers on dedicated hardware                          | Serverless functions on AWS                            |
| Scaling                | Vertical + horizontal scaling with replicas                         | Scales via stateless function instances                |
| Persistent Connections | âœ… Yes (sockets, live updates, real-time apps)                      | âŒ Unsupported                                         |
| Cold Starts            | âŒ No cold starts                                                   | âš ï¸ Possible cold starts (with optimizations)           |
| Max Memory Limit       | Up to full machine capacity                                         | 4GB per function                                       |
| Execution Time Limit   | Unlimited (as long as the process runs)                             | 800 seconds (13.3 minutes)                             |
| Databases              | Built-in one-click deployments for major databases                  | Integrated via marketplace (external providers)        |
| Project Structure      | Unified project: multiple services + databases in one               | One service per project                                |
| Usage-Based Billing    | Based on compute time and size per replica                          | Based on CPU time, memory provisioned, and invocations |
| Ideal For              | Fullstack apps, real-time apps, backend servers, long-running tasks | Frontend-first apps, short-lived APIs                  |
| Support for Docker     | âœ… Yes                                                              | âŒ No (function-based only)                            |

## Migrate from Vercel to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. â€œChoose Deploy from GitHub repoâ€, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Active compute time x compute size (memory and CPU)


# Compare to DigitalOcean
Source: https://docs.railway.com/maturity/compare-to-digitalocean

Compare Railway and DigitalOcean App Platform on infrastructure, pricing model and deployment experience.

- You can deploy your app from a Docker image or by importing your appâ€™s source code from GitHub.
- Multi-service architecture where you can deploy different services under one project (e.g. a frontend, APIs, databases, etc.).
- Services are deployed to a long-running server.
- Public and private networking are included out-of-the-box.
- Healthchecks are available to guarantee zero-downtime deployments.
- Connect your GitHub repository for automatic builds and deployments on code pushes.
- Support for instant rollbacks.
- Integrated metrics and logs.
- Define Infrastructure-as-Code (IaC).
- Command-line-interface (CLI) to manage resources.
- Integrated build pipeline with the ability to define pre-deploy command.
- Support for wildcard domains.
- Custom domains with fully managed TLS.
- Run arbitrary commands against deployed services (SSH).
- Shared environment variables across services.
- Both platformsâ€™ infrastructure runs on hardware thatâ€™s owned and operated in data centers across the globe.

That said, there are some differences between the platforms that might make Railway a better fit for you.

## Scaling strategies

### DigitalOcean App Platform

DigitalOcean App Platform follows a traditional, instance-based model. Each instance has a set of allocated compute resources (memory and CPU).

In the scenario where your deployed service needs more resources, you can either scale:

- Vertically: you will need to manually upgrade to a large instance size to unlock more compute resources.
- Horizontally: your workload will be distributed across multiple running instances. You can either:
  - Manually specify the machine count.
  - Autoscale by defining a minimum and maximum instance count. The number of running instances will increase/decrease based on a target CPU and/or memory utilization you specify.

The main drawback of this setup is that it requires manual developer intervention. Either by:

- Manually changing instance sizes/running instance count.
- Manually adjusting thresholds because you can get into situations where your service scales up for spikes but doesnâ€™t scale down quickly enough, leaving you paying for unused resources.

Beyond scaling, there are other notable limitations. DigitalOcean App Platform doesnâ€™t natively support multi-region deployments. To achieve that, you must create separate instances in different regions and set up an external load balancer to route traffic appropriately.

Furthermore, services deployed to the platform do not offer persistent data storage. Any data written to the local filesystem is ephemeral and will be lost upon redeployment, meaning you'll need to integrate with external storage solutions if your application requires data durability.

### Railway

Railway automatically manages compute resources for you. Your deployed services can scale up or down based on incoming workload without manual configuration of metrics/thresholds or picking instance sizes. Each plan includes defined CPU and memory limits that apply to your services.

You can scale horizontally by deploying multiple replicas of your service. Railway automatically distributes public traffic randomly across replicas within each region. Each replica runs with the full resource limits of your plan.

For example, if you're on the Pro plan, each replica gets 32 vCPU and 32 GB RAM. So, deploying 3 replicas gives your service a combined capacity of 96 vCPU and 96 GB RAM.

Replicas can be placed in different geographical locations for multi-region deployments. The platform automatically routes public traffic to the nearest region, then randomly distributes requests among the available replicas within that region. No need to define compute usage thresholds.

<video src="https://res.cloudinary.com/railway/video/upload/v1753470552/docs/comparison-docs/railway-replicas_nt6tz8.mp4" controls autoplay loop muted></video>

You can also set services to start on a schedule using a crontab expression. This lets you run scripts at specific times and only pay for the time theyâ€™re running.

## Pricing

### DigitalOcean App Platform

DigitalOcean App Platform follows a traditional, instance-based pricing. You select the amount of compute resources you need from a list of instance sizes where each one has a fixed monthly price.

!DigitalOcean App Platform instances

While this model gives you predictable pricing, the main drawback is you end up in one of two situations:

- Under-provisioning: your deployed service doesnâ€™t have enough compute resources which will lead to failed requests.
- Over-provisioning: your deployed service will have extra unused resources that youâ€™re overpaying for every month.

Enabling horizontal autoscaling can help with optimizing costs, but the trade-off will be needing to figure out the right amount of thresholds instead.

### Railway

Railway automatically scales your infrastructure up or down based on workload demands, adapting in real time without any manual intervention. This makes it possible to offer a usage-based pricing model that depends on active compute time and the amount of resources it consumes. You only pay for what your deployed services use.

You donâ€™t need to think about instance sizes or manually configure them. All deployed services scale automatically.

!Railway usage-based pricing

If you spin up multiple replicas for a given service, youâ€™ll only be charged for the active compute time for each replica.

Railway also has a serverless feature, which helps further reduce costs when enabled. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This is ideal for workloads with sporadic or bursty traffic, so you only pay when your code is running.

## Developer Workflow & CI/CD

### DigitalOcean App Platform

DigitalOcean App Platformâ€™s dashboard offers a traditional dashboard where you can view all of your projectâ€™s resources.

!DigitalOcean App Platform dashboard

However, DigitalOcean App Platform lacks built-in CI/CD capabilities around environments:

- No concept of â€œenvironmentsâ€ (e.g., development, staging, and production). To achieve proper environment isolation, you must create separate projects for each environment.
- No native support for automatically creating isolated preview environments for every pull request. To achieve this, you'll need to integrate third-party CI/CD tools like GitHub Actions.

Finally, DigitalOcean App Platform doesn't support webhooks, making it more difficult to build integrations with external services.

### Railway

Railwayâ€™s dashboard offers a real-time collaborative canvas where you can view all of your running services and databases at a glance. You can group the different infrastructure components and visualize how theyâ€™re related to one another.

!Railway canvas

Additionally, Railway offers a template directory that makes it easy to self-host open-source projects with just a few clicks. If you publish a template and others deploy it in their projects, youâ€™ll earn a 50% kickback of their usage costs.

Check out all templates at railway.com/deploy

<video src="https://res.cloudinary.com/railway/video/upload/v1753470547/docs/comparison-docs/railway-templates-marketplace_v0svnv.mp4" controls autoplay loop muted></video>

## Summary

| **Category**              | **DigitalOcean App Platform**                                                                                                         | **Railway**                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Scaling Model**         | Manual instance-based scaling                                                                                                         | Fully automated scaling                                                    |
| **Vertical Scaling**      | Manual upgrade to larger instance                                                                                                     | N/A â€“ no instance sizes to manage                                          |
| **Horizontal Scaling**    | Manually add/remove instances or autoscaling (based on CPU/memory thresholds); requires tuning                                        | Deploy multiple replicas; traffic auto-distributed; no thresholds required |
| **Multi-region Support**  | Manual via separate instances and load balancers                                                                                      | Built-in support; traffic routed to nearest region                         |
| **Persistent volumes**    | Not supported                                                                                                                         | Supported                                                                  |
| **Pricing Model**         | Fixed monthly pricing per instance size                                                                                               | Usage-based: active compute time Ã— memory/CPU used                         |
| **Cost Optimization**     | Requires tuning to avoid over/under-provisioning                                                                                      | Inherently optimized. Pay only for used compute                            |
| **Developer Dashboard**   | Traditional project dashboard                                                                                                         | Real-time collaborative canvas with visual service layout                  |
| **Environments & CI/CD**  | No native concept of environments, requires manual project setup. Automated preview deployments not supported. Webhooks not supported | Native support for preview environments, CI/CD integrations, and webhooks  |
| **Templates & Ecosystem** | Limited                                                                                                                               | Extensive template directory; creators can earn from deployed usage        |

## Migrate from DigitalOcean App Platform to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. â€œChoose Deploy from GitHub repoâ€, connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Total resources = number of replicas Ã— maximum compute allocation per replica

Active compute time x compute size (memory and CPU)


# Compare to VPS
Source: https://docs.railway.com/maturity/compare-to-vps

Compare Railway and VPS hosting on infrastructure management, security, monitoring, pricing, and operational overhead for modern applications.

VPS hosting providers like AWS EC2, DigitalOcean Droplets, Hetzner Cloud, Linode, or Vultr give you a virtual machine where you have full control over the operating system, software stack, and configuration. This offers maximum flexibility but requires significant DevOps expertise and ongoing maintenance.

Railway provides a fully managed platform that abstracts away infrastructure complexity while giving you the flexibility of a dedicated environment. You get VPS-level control without the operational burden.

## Quick Comparison: VPS vs. Railway

| Dimension                  | VPS Hosting                                                                       | Railway                                                              |
| -------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Infrastructure**         | Full responsibility: OS setup, patches, SSL, firewalls, scaling                   | Zero-config deploy, managed OS/security, built-in scaling            |
| **Security & Compliance**  | Manual hardening, audits, SOC 2/ISO require major effort                          | SOC 2 Type II, GDPR, MFA, automatic patches, DDoS protection         |
| **Monitoring & Logging**   | Must integrate Prometheus/Grafana/ELK manually                                    | Built-in observability, logs, metrics, dashboards, alerting          |
| **Scaling & Distribution** | Manual vertical/horizontal scaling, DNS/load balancer setup, complex multi-region | Auto vertical/horizontal scaling, multi-region deploy with one click |
| **Pricing Model**          | Fixed monthly instance cost regardless of usage                                   | Usage-based, serverless sleeping, pay only for active compute        |
| **Workflow & Deployment**  | Manual CI/CD setup, manual rollbacks, secrets management                          | GitHub integration, preview envs, instant rollback, managed secrets  |

## Infrastructure & Operational Overhead

### VPS Hosting

When you choose VPS hosting, you're essentially becoming your own infrastructure team. This means taking full responsibility for:

**Server Setup & Configuration**

* Installing and configuring the operating system (Ubuntu, CentOS, Debian, etc.)
* Applying security patches and system updates
* Configuring firewalls, SSH access, and user management
* Installing and configuring web servers (Nginx, Apache)
* Setting up reverse proxies and load balancers
* Managing SSL certificates and renewals

**Application Environment Management**

* Installing/managing programming runtimes (Node.js, Python, Go, etc.)
* Setting up process managers (PM2, systemd, supervisor)
* Configuring environment variables and secrets management
* Managing database installs/configs (MySQL, Postgres, MongoDB, etc.)
* Setting up caching layers (Redis, Memcached)

**System Administration**

* Monitoring disk space, memory usage, CPU performance
* Managing log rotation and aggregation
* Automated backups and disaster recovery planning
* Applying vulnerability patches
* DNS configuration and domain setup

Youâ€™ll need to continuously maintain and update this stack, troubleshoot outages, and scale resources as needed.

### Railway

Railway eliminates this operational burden:

**Zero-Configuration Deployment**

* Deploy directly from GitHub with automatic builds

!Railway deployment from GitHub

* Auto-detects dependencies and installs them
* Built-in support for major programming languages and frameworks
* Automatic SSL provisioning and renewal
* Health checks and automatic restarts

!Healthchecks

**Managed Infrastructure**

* Railway owns/operates underlying hardware
* Automatic OS/security patches
* Built-in load balancing and traffic distribution via service replicas
* Automatic scaling based on workload demand
* Managed networking with private service communication

## Security & Compliance

### VPS Hosting

Security is entirely your responsibility, including:

**Basic Security Hardening**

* Disable root login, enforce SSH key auth
* Configure firewalls (UFW/iptables)
* Install intrusion detection (fail2ban, IDS)
* Regular audits and patching

**Application Security**

* File permissions and ownership
* Secure headers (HSTS, CSP, X-Frame-Options)
* Rate limiting and DDoS protection
* Secure secret management
* Secure database connections

**Compliance Requirements**

Achieving certifications on VPS requires significant additional work:

* Access controls and audit logging
* Data classification/handling procedures
* Incident response/business continuity plans
* Security assessments & penetration testing
* Evidence collection and documentation
* Encryption/key management systems

This typically requires dedicated expertise and can be costly.

### Railway

Railway provides enterprise-grade security out of the box:

**Built-in Security Features**

* Encrypted secret/environment management

!Variables and secrets


* SSL/TLS encryption for all services
* Private networking within projects
* Automatic patches and updates
* DDoS protection

**Compliance & Certifications**

* SOC 2 Type II
* GDPR compliance
* HIPAA compliance
* Regular third-party audits

**Security Best Practices**

* Role-based access control

!Roles & permissions

* MFA and passkey support
* Regular assessments and penetration testing
* Incident response and continuity planning

## Monitoring & Observability

### VPS Hosting

Requires integrating multiple tools:

**System & Application Monitoring**

* Install agents (Prometheus, Grafana, commercial tools)
* Custom dashboards for CPU, memory, disk, network
* Configure alerting rules and notification channels
* Implement log aggregation/analysis (ELK, Loki)
* Uptime monitoring and health checks

### Railway

Monitoring is built-in:

**Observability Dashboard**

* CPU, memory, network metrics

!Observability dashboard

* Integrated log aggregation and search

!Logs

* Auto alerting and notifications
!Notifications

## Scalability & Global Distribution

### VPS Hosting

Scaling requires manual setup:

**Vertical Scaling (Up)**

* Manually upgrade to larger instances
* Typically downtime during resizing
* Application restarts required

**Horizontal Scaling (Out)**

* Provision additional VPS instances
* Configure load balancers (HAProxy, Nginx, cloud LB)
* Manage session persistence/sticky sessions
* Database connection pooling/discovery

**Multi-Region Deployment Challenges**

* Manual VPS setup in each region
* Complex DNS/georouting configs
* Data replication/sync complexity
* Cross-region latency
* Higher operational overhead and cost

### Railway

Scaling and distribution are automatic:

**Automatic Vertical Scaling**

* Scale up to plan limits automatically
* No downtime or manual intervention

**Effortless Horizontal Scaling**

* Deploy replicas with one click
!Horizontal scaling

* Automatic load balancing & health checks
* Automatic traffic routing to nearest region

**Multi-Region Deployment**

* Deploy globally with one command
!Multi-region deployment
* Auto traffic routing, failover, replication
* CDN integration for static assets
* Simplified data management
* Reduced latency for global users

## Pricing & Cost Optimization

### VPS Hosting

* Fixed monthly pricing by instance size.
* Extra tools (monitoring, backups, scaling) often add hidden costs.

### Railway

Railway follows a usage-based pricing model that depends on how long your service runs and the amount of resources it consumes. You only pay for activce CPU and memory, not for idle time.

!railway usage-based pricing

Pricing plans start at $5/month. You can check out the pricing page for more details.

**Cost Optimization**

If you would like to further reduce costs, you can enable the serverless feature. When a service has no outbound requests for over 10 minutes, it is automatically put to sleep. While asleep, the service incurs no compute charges. It wakes up on the next incoming request, ensuring seamless reactivation without manual effort. This makes it ideal for sporadic or bursty workloads, giving you the flexibility of a full server with the cost efficiency of serverless, with the benefit of only paying when your code is running.

!serverless

## Developer Workflow & Deployment

### VPS Hosting

Deploying requires building your own CI/CD:

**CI/CD**

* Configure GitHub Actions/Jenkins/etc.
* Write deployment scripts
* Separate staging/production setup
* Automated testing/quality gates
* Rollback procedures

**Environment Management**

* Manual env var config
* Separate servers for staging/prod
* Manual DB migrations/schema updates
* Complex secret management

### Railway

CI/CD and environments are built-in:

**Automatic CI/CD**

* GitHub repo integration
* Preview environments per pull request
* One-click rollbacks
* Automatic env var management

**Environment Management**

* Built-in support for dev/staging/prod

!Environment management

* Shared env vars across services
* Encrypted secret management
* Auto DB migrations/schema updates by customizing the pre-deploy command

## Railway as a VPS Alternative: Migrate from VPS to Railway

To get started, create an account on Railway. You can sign up for free and receive $5 in credits to try out the platform.

### Deploying your app

1. Choose "Deploy from GitHub repo", connect your GitHub account, and select the repo you would like to deploy.

!Railway onboarding new project

2. If your project is using any environment variables or secrets:
   1. Click on the deployed service.
   2. Navigate to the â€œVariablesâ€ tab.
   3. Add a new variable by clicking the â€œNew Variableâ€ button. Alternatively, you can import a .env file by clicking â€œRaw Editorâ€ and adding all variables at once.

!Railway environment variables

3. To make your project accessible over the internet, you will need to configure a domain:
   1. From the projectâ€™s canvas, click on the service you would like to configure.
   2. Navigate to the â€œSettingsâ€ tab.
   3. Go to the â€œNetworkingâ€ section.
   4. You can either:
      1. Generate a Railway service domain: this will make your app available under a .up.railway.app domain.
      2. Add a custom domain: follow the DNS configuration steps.

## Need help or have questions?

If you need help along the way, the Railway Discord and Help Station are great resources to get support from the team and community.

Working with a larger workload or have specific requirements? Book a call with the Railway team to explore how we can best support your project.

## Code Examples

Active compute time x compute size (memory and CPU)



# Migration
Source: https://docs.railway.com/migration

# Migrate from Render
Source: https://docs.railway.com/migration/migrate-from-render

Learn how to migrate your apps from Render to Railway with this step-by-step guide. Fast, seamless, and hassle-free.

With features like instant deployments, CI/CD integrations, private networking, observability, and effortless scaling, Railway helps developers focus on building rather than managing infrastructure.

Railway boasts of a superior and intuitive user experience that makes deploying complex workloads easy to configure and manage.

Railway offers:

- **Broad Language and Framework Support**: Deploy apps in any language or framework.
- **Flexible Deployment Options**: Use GitHub, Dockerfiles, Docker images from supported registries (Docker Hub, GitHub, RedHat, GitLab, Microsoft), or local deployments via the Railway CLI.
- **Integrated Tools**: Simplify environment variable management, CI/CD, observability, and service scaling.
- **Networking Features:** Public and private networking.
- **Best in Class Support:** Very active community on Discord and our Central Station.

..and so much more. Want to see for yourself? Try Railway for a spin today!

## Migration Steps

In this guide, we will migrate a Go (Beego) app with a Postgres database from Render to Railway.

Hereâ€™s the link to the app. A simple chat app that have the options of Long polling and Web socket â€” https://github.com/unicodeveloper/beego-WebIM

### 1. Set Up a Railway Project

Navigate to Railway's Project Creation Page.

Select the **Deploy from GitHub Repo** option and connect your repository. If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.

!Set up a Railway Project

### 2. Deploy the App

Railway automatically detects a render.yaml file in your repository and provisions the corresponding services, including databases, web (both public and private), crons, and workers.

If environment variables are defined in your render.yaml, Railway will import them automatically to the appropriate services. If they are not defined, you can manually migrate them by following these steps:

**On Render**:

1. Go to the **Environment Variables** page of your service.
2. Copy all the variables and their values.

**On Railway**:

1. Open the **Variables** section for the relevant service.
2. Switch to the **Raw Editor** and paste the copied environment variables.
3. Deploy the changes to apply the configuration.

!Deploy on Railway

Railway will deploy both the Go app as a service and the database, as shown in the image above. You can monitor the service building and deploying in the Project Canvas.

### 3. Database Migration

Railway supports a variety of databases, including **PostgreSQL**, **MongoDB**, **MySQL**, and **Redis**, allowing you to deploy the one that best fits your application needs.

When a render.yaml file includes a databases section, Railway will automatically provision a **PostgreSQL database** for your app. If you're migrating data to Railway, you can follow these steps:

1. Export your database from Render using tools like pg_dump.
2. Import the data into Railway using psql.

For detailed instructions, check out this comprehensive tutorial on migrating PostgreSQL data between services.

Once the migration is complete, update the DATABASE_URL environment variable in your Railway app to point to the new PostgreSQL database.

### 4. Multi-region deployments

If your app needs to use multi-region deployments, you can leverage Railwayâ€™s multi-region replicas.

Enable this in the **Settings** section of your Railway service to keep your app close to users worldwide.

**Note:** Multi-region replicas is currently available to Pro users.

!Multi-region deployments

And thatâ€™s it. Thatâ€™s all you need to migrate your app from Render to Railway.


# Migrate from Fly
Source: https://docs.railway.com/migration/migrate-from-fly

Learn how to migrate your apps from Fly.io to Railway with this step-by-step guide. Fast, seamless, and hassle-free.

**TL;DR: Quick Migration Steps**

- Set up new app on Railway
- Export data from Fly.io and Import into Railway DB
- Deploy app (including auto-migration of app config & variables)

We provide everything Fly.io offersâ€”and more! Check out our comparison guide to see the differences and make an informed choice.

Why take our word for it? Experience the Railway advantage yourselfâ€”give it a spin today!

## Migration Steps

In this guide, we will migrate a Go (Gin) app with a Postgres database from Fly.io to Railway. While we are using this app as an example, the process applies to any app, making it easy to transition your projects smoothly.

Hereâ€™s the link to the app.

### 1. Set Up a Railway Project

Navigate to Railway's Project Creation Page.

Select the **Deploy from GitHub Repo** option and connect your repository. If your Railway account isnâ€™t linked to GitHub yet, youâ€™ll be prompted to do so.

!Railway new project

### 2. Deploy the App

Railway auto-imports all the build configurations, deploy commands, environment variables from your Fly.io app repoâ€”no manual setup needed.

If the environment variables are missing, you can easily add them manually by following these steps:

### Adding Environment Variables on Railway:

1. Navigate to the **Variables** section of your service.
2. Switch to the **Raw Editor** and paste the copied environment variables.
3. Deploy the changes to apply the configuration.

!Variables imported automatically from fly.toml into Railway service

Railway will deploy the Gin app as a service, as shown in the image above. You can monitor the service building and deploying in the Project Canvas.

**Serverless (App Sleep) activated**: In this **Fly.io** app, the HTTP service is configured with **auto_stop_machines='stop'** and **auto_start_machines=true**, enabling automatic stopping and restarting of machines. On Railway import, we automatically enable this setting to effortlessly optimize resource usage.

!App sleep activated to optimize resource usage and spend

### 3. Database Migration

Railway supports a variety of databases, including **PostgreSQL**, **MongoDB**, **MySQL**, and **Redis**, allowing you to deploy the one that best fits your application needs. We also support many more via our templates marketplace.

If you're migrating data to Railway from Fly, you can follow these steps:

1. Provision a new database by right clicking on the dashboard canvas and selecting Postgres.
2. Export your data from Flyio
   - Use flyctl to connect to your Flyio Postgres instance
     - fly postgres connect -a <postgres-app-name>
   - Use pg_dump to export your database
     - pg_dump -Fc --no-acl --no-owner -h localhost -p 5432 -U <your-db-username> -d <your-db-name> -f flyio_db_backup.dump
   - Use pg_restore to connect to your Railway database and restore the data from the dump.
     - pg_restore -U <username> -h <host> -p <port> -W -F t -d <db_name> <dump_file_name>

For detailed instructions, check out this comprehensive tutorial on migrating PostgreSQL data between services.

Once the migration is complete, update the DATABASE_URL environment variable in your Railway app to point to the new PostgreSQL database and redeploy.

### 4. Replicas & Multi-region deployments

In this Fly.io app, the setting **min_machines_running=2** ensures that at least **two instances** of the service remain active. On Railway import, we automatically translate this configuration to ensure that two **service instances** are running without any extra setup.

!Replicas

If your app needs to use multi-region deployments, you can leverage Railwayâ€™s multi-region replicas.

Enable this in the **Settings** section of your Railway service to keep your app close to users worldwide.

**Note:** Multi-region replicas is currently available to Pro users.

And thatâ€™s it. Thatâ€™s all you need to migrate your app from Flyio to Railway.


# Migrate from Vercel
Source: https://docs.railway.com/migration/migrate-from-vercel

Learn how to migrate your Next.js app from Vercel to Railway with this step-by-step guide. Fast, seamless, and hassle-free.

With features like instant rollbacks, integrated observability, and seamless environment management, Railway empowers developers to focus on building great applications rather than managing infrastructure.

Railway offers -

- **Next.js Optimization**: Built-in support for all Next.js features including ISR, SSR, and API routes

- **Zero Config Deployments**: Automatic framework detection and build optimization

- **Enhanced Development Flow**: Local development with production parity

- **Collaborative Features**: Team management, deployment protection, and role-based access

- **Priority Support**: Dedicated support for Railway users

## Migration Steps

Let's walk through migrating a Next.js application to Railway. For this guide, we'll use a sample e-commerce app that showcases common Next.js features and configurations.

### Deploying Your Application

To get started deploying our NextJS app, we will first make a new <a href="/overview/the-basics#project--project-canvas" target="_blank">project</a>.

- Open up the <a href="/overview/the-basics#dashboard--projects" target="_blank">dashboard</a> â†’ Click **New Project**.
- Choose the **GitHub repo** option.

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752559/docs/quick-start/new_project_uyqqpx.png"
alt="screenshot of new project menu with deploy from github selected"
layout="responsive"
width={836} height={860} quality={100} />

_Railway requires a valid GitHub account to be linked. If your Railway account isn't associated with one, you will be prompted to link it._

- Search for your GitHub project and click on it.

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752559/docs/quick-start/new_github_project_pzvabz.png"
alt="screenshot of new project menu with nextjs repo selected"
layout="responsive"
width={836} height={596} quality={100} />

- Choose either **Deploy Now** or **Add variables**.
  **Deploy Now** will immediately start to build and deploy your selected repo.
  **Add Variables** will bring you to your service and ask you to add variables, when done you will need to click the **Deploy** button at the top of your canvas to initiate the first deployment.
  _For brevity we will choose **Deploy Now**._

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752558/docs/quick-start/deploy_now_pmrqow.png"
alt="screenshot of new project menu with deploy now option selected"
layout="responsive"
width={836} height={620} quality={100} />

When you click **Deploy Now**, Railway will create a new project for you and kick off an initial deploy after the project is created.

**Once the project is created you will land on your <a href="/overview/the-basics#project--project-canvas" target="_blank">Project Canvas</a>**.

<Image src="https://res.cloudinary.com/railway/image/upload/v1723752560/docs/quick-start/project_canvas_nextjs_c6bjbq.png"
alt="screenshot of the project canvas showing environment variables configuration"
layout="responsive"
width={1363} height={817} quality={100} />

From here Railway will automatically -

- Detect your Next.js configuration

- Configure the appropriate Node.js version

- Build your application

- Run your application

### Environment Configuration

Next.js applications often rely on environment variables for API keys, database connections, and feature flags. Here's how to transfer them -

**From Vercel -**

1. Visit your Vercel project settings

2. Navigate to the Environment Variables tab

3. Export your variables (you can copy them directly)

**To Railway -**

1. Select your service in the Project Canvas

2. Open the Variables tab

3. Use the Raw Editor for bulk variable import

4. Click Deploy to apply changes

### Domain Configuration

Railway makes it simple to set up custom domains or use our provided domains -

1. Open your service's Settings

2. Navigate to the Public Networking section

3. Choose between:

   - Generating a Railway service domain

   - Adding your custom domain

4. Follow the DNS configuration steps if using a custom domain

### Deployment Verification

Before finalizing your migration:

1. Check your application's core functionality

2. Verify environment variables are properly set

3. Test dynamic routes and API endpoints

4. Confirm image optimization is working

5. Monitor build and runtime logs

Railway's integrated observability helps you catch any issues early in the migration process.

### Local Development

Railway makes local development seamless with your production environment:

1. Install the Railway CLI: npm i -g @railway/cli

2. Run railway link to connect to your project

3. Use railway run to start your app locally with production variables

This ensures development/production parity and helps catch issues before they reach production.

That's all it takes to move your Next.js application to Railway! Need help? Our team and community are always ready to assist.

Need more information on how we compare to Vercel? Check out our comparison page.


# Migrate from DigitalOcean
Source: https://docs.railway.com/migration/migrate-from-digitalocean

Learn how to migrate your WordPress site from DigitalOcean to Railway with this step-by-step guide. Fast, seamless, and hassle-free.

Railway offers:

- **Modern Infrastructure**: High-performance cloud platform

- **Quick Setup**: WordPress-ready deployment template

- **Database Support**: MariaDB database capabilities

- **Integrated SSL**: Automatic SSL certificate management

- **Scalable Infrastructure**: Easily handle traffic spikes and growth

- **Collaborative Features**: Team management, deployment protection, and role-based access

- **Priority Support**: Dedicated support for Railway users

## Migration Steps

Let's walk through migrating a WordPress site from DigitalOcean to Railway. This process involves backing up your existing installation, deploying WordPress on Railway and then restoring from your backup.

### 1. Backup your WordPress site

- Ensure you have a backup of your existing site. Use a WordPress backup plugin of your choice to export your site data.

  Make sure this backup includes, All WordPress files, All WordPress database tables, All WordPress uploads.

- Document your current configuration

  - Note any custom domain settings

  - Keep track of your username and password for wp-admin.

### 2. Deploy WordPress

- Open the WordPress Template page

  <Image src="https://res.cloudinary.com/railway/image/upload/v1741839172/docs/do-migration-guide/wordpress_template_pqnksc.png"
    alt="Screenshot of the WordPress template"
    layout="responsive"
    width={1301} height={799} quality={100} />

- Click "Deploy Now" to Deploy the WordPress template.

- Since this template doesnâ€™t require any configuration, Click "Deploy" and wait for the deployment to complete.

The template will automatically configure -

- A MariaDB database

- Initial WordPress setup

- Required environment variables

- A temporary service domain

<Image src="https://res.cloudinary.com/railway/image/upload/v1741839172/docs/do-migration-guide/wordpress_deployment_qwg5j1.png"
alt="Screenshot of wordpress after deployment"
layout="responsive"
width={838} height={454} quality={100} />

### 3. Restore your site content

After the template deployment completes -

1. Access your WordPress installation via the temporary service domain.

2. Configure your WordPress settings

3. Install your preferred backup plugin

4. Restore your site content from your backup

### 4. Configure Domain Settings

To set up your custom domain:

1. Open your service's Settings in Railway

2. Navigate to the "Networking" section

3. Add your custom domain

4. Update your DNS records according to the instructions given.

**Note:** You will need to redeploy your service for WordPress to pick up the new domain.

<Image src="https://res.cloudinary.com/railway/image/upload/v1741839172/docs/do-migration-guide/wordpress_service_settings_networking_meyhcs.png"
alt="Screenshot of Railway domain configuration page"
layout="responsive"
width={763} height={505} quality={100} />

### 5. Verify Migration

Before finalizing your migration -

1. Test all WordPress functionality

2. Verify all pages and posts are displaying correctly

3. Check media files are properly loaded

4. Test user authentication

5. Verify contact forms and other interactive elements

### 6. Performance Optimization

Consider these optimization options for your WordPress deployment:

- Configure caching by placing Cloudflare or a similar CDN in front of your site.

- Optimize database performance by setting up a caching plugin.

- Set up appropriate scaling configurations.

- Implement CDN if needed

That's all you need to migrate your WordPress site from DigitalOcean to Railway! Need assistance? The Central Station is there to help you with any questions during your migration process.


# Migrate from Heroku
Source: https://docs.railway.com/migration/migrate-from-heroku

Learn how to migrate your apps from Heroku to Railway with this step-by-step guide. Fast, seamless, and hassle-free.

All you need to do is create a project in Railway, push your code, and migrate your environment variables.

This guide will step you through the process of migrating a simple web service, using the Railway CLI.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695765903/docs/heroku-migration/intro1_uauodg.gif"
alt="Screenshot of Railway Up"
layout="intrinsic"
width={700} height={464} quality={80} />

## Working Directory

In your terminal, ensure your current working directory is the same directory where your service code is located.

This is important so that as you complete the following steps, the Railway CLI is properly linked.

## 1. Login to Railway From the CLI

Ensure your CLI is authenticated to your Railway account:

This command will prompt to open a browser to complete authentication. Once authenticated, commands executed by the Railway CLI, will be performed in the context of your Railway account.

## 2. Create a New Project

Now, let's create a new project:

This command will prompt you to define a name for your service.

## 3. Deploy the Service

Once your project is created, you can push your code into the project and assign a domain.

### Push the Code

Push the code into a service in Railway:

At this point, the service is being deployed, but let's give it a domain.

### Assign a Domain

The service we are migrating is a web service that should be available over the Internet, so let's assign a domain:

Now the service will be available over the Internet via the provided domain.

## 4. Migrate the Environment Variables

Finally, we will import the environment variables from Heroku into Railway.

<Image src="https://res.cloudinary.com/railway/image/upload/v1695765481/docs/heroku-migration/variables_hagopv.gif"
alt="Video of importing variables from Heroku"
layout="intrinsic"
width={600} height={364} quality={80} />

### Open the Project in Railway

Let's pop over to our new project in the Railway canvas.:

This will open the project in your browser.

### Add Heroku Variables to the Service

From the project canvas, import the Heroku variables into the service:

- click on the service
- click Variables tab
- open the command palette using CMD + K or Ctrl + K.
- search for Import variables from Heroku
- confirm the Heroku service and hit Enter

Your Heroku variables will be imported into the service, and it will automatically redeploy.

_Note: The first time you import variables from Heroku, you will be prompted to Allow Railway to connect to your Heroku account._

## Conclusion

Following this guide, we have successfully migrated a simple web service from Heroku to Railway, including importing variables from Heroku into Railway.

We have completed the migration by pushing our code directly from our local machine into a service in Railway. Once you are comfortable with Railway, you may want to integrate deployments into your development workflow.

For more advanced operations, like migrating your databases from Heroku to Railway, the process will be a bit more involved, but we are happy to help work out a solution!

## Need Help?

If you run into any issues, or would like help with your migrations, we would be more than happy to answer your questions on our <a href="https://discord.gg/railway" target="_blank">Discord</a> or over email at team@railway.com.

## Code Examples

railway login

railway init

railway up -d

railway domain

railway open



# Community
Source: https://docs.railway.com/community

# The Conductor Program
Source: https://docs.railway.com/community/the-conductor-program

Learn about Railwayâ€™s Conductor Program and how it empowers the developer community.

This program aims to foster collaboration and help our Conductors grow.

## What Do Conductors Do?

Our Conductors spend time in Discord and the Central Station answering questions, sharing tips, and making sure everyone can use Railway successfully.

Here are a few key ways they contribute -

- Providing community support through Discord and the Central Station.

- Maintaining a healthy and welcoming community atmosphere while moderating our channels and templates.

- Contributing to Railway's open-source projects through improvements and new features.

- Creating a direct feedback loop between users and the Railway team.

Through these activities, Conductors ensure everyone can use Railway successfully while helping to build a collaborative and supportive community environment.

## Ready to Become a Conductor?

Are you passionate about helping others and love being part of Railway's community? We're always excited to welcome new Conductors who share our enthusiasm for community engagement!

Here's what we look for in potential Conductors -

- Have demonstrated experience with Railway's platform and services.

- Show a consistent track record of helping others in our community.

- Maintain professional and friendly communication.

- Are active participants in our Discord and Central Station.

- Demonstrate strong technical problem-solving abilities.

The ideal Conductor combines technical expertise with mentorship skills to help our community thrive!

<TallyButton data-tally-open="nP2qqd" data-tally-width="700" data-tally-emoji-text="ðŸ‘‹" data-tally-emoji-animation="wave" data-tally-auto-close="2000">Apply Now</TallyButton>

## Conductor Benefits

Being a Conductor comes with several exciting perks and rewards to recognize your valuable contributions to the community.

As part of the program, conductors will receive -

- 100% off discount for the Hobby plan's subscription and resource costs.

- Cash payouts for solving complex issues for users.

- The opportunity to earn payouts for OSS contributions (CLI, Nixpacks, Docs, etc).

- First access to template bounties.

- Letters of recommendation for educational institutions and employer references.

- Moderation status on Discord and the Central Station.

- Access to a team workspace shared with other Conductors.

- A direct line to the team via the private Conductor only channel.

- Your choice of Railway Swag.

And to top it all off, each quarter we reward our most outstanding conductor with a pizza party! ðŸŽ‰

## Conductor Participation

We believe in fostering an active and supportive Conductor program that enables everyone to make meaningful contributions. To help keep our community vibrant, we conduct friendly quarterly check-ins with all Conductors.

As a Conductor, you'll contribute regularly in these key areas -

- Community Engagement

  - Being an active, welcoming presence in community channels.

  - Building connections with fellow community members.

  - Joining community conversations and sharing experiences.

  - Looking out for the community by making sure discussions stay positive and helpful.

- Support Activities

  - Helping others in Discord and the Central Station.

  - Showing consistent engagement by regularly contributing to meaningful solutions across all Railway platforms.

- Open Source Contributions

  - Contributing through either small improvements or substantial feature additions.

  - New features should address community-requested needs with demonstrated user demand.

  - Bug fixes should focus on issues affecting multiple users.

We understand that maintaining consistent participation across these areas requires dedication and time. As part of our commitment to supporting Conductors, we have quarterly check-ins to discuss your experience and ensure you have everything needed to succeed.

While we aim for regular engagement, we recognize that life circumstances and priorities can change. If participation becomes limited, we may need to transition members out of the program during our bi-annual review. However, our door always remains open â€“ former Conductors are welcome to rejoin the program when their schedule better accommodates regular participation!


# Affiliate Program
Source: https://docs.railway.com/community/affiliate-program

Show Railway to your network, earn 15% cash commission on referral revenue.

Anyone that signs up from your link will receive $20 in Railway credits, equivalent to a free month on the Pro tier.

Once the signup becomes a Railway customer, you will receive 15% commission on the first 12 months of invoices from the new customer moving forward.

## How Do I Become an Affiliate?

<Image src="https://res.cloudinary.com/railway/image/upload/v1631917786/docs/referrals_cash_ashj73.png"
alt="Screenshot of Referrals Page"
layout="intrinsic"
width={1784} height={1104} quality={80} />

Follow these steps to start earning:

- Sign up for Railway.

- Click the Refer button in the dashboard, or navigate directly to the workspace's <a href="https://railway.com/account/referrals" target="_blank">referrals page</a>.

- Copy the unique link.

- Create content and post about Railway, including the unique link.

To see and withdraw earnings:

- Navigate to the workspace settings and click on Earnings, which leads you to the <a href="https://railway.com/account/earnings" target="_blank">earnings page</a>.

- The Earnings page displays total earnings

- Follow the instructions here to withdraw to GitHub Sponsors or Buy Me a Coffee.

- After adding your account details you will request a withdrawal. Our team will receive the request and process it.

## How Do I Maximize Earnings?

Earnings come from signups that are successful and start to scale on Railway. Walk through Railway use cases to give your network an accurate idea of what they can do on Railway.

A few ideas to maximize reach and earnings as an affiliate:

- Create video content on YouTube demoing a use case with a specific template on Railway

- Write a blog post on Medium walking through pros/cons of cloud deployment and hosting on Railway

- Post on LinkedIn (or your social platform of choice) about your experience on Railway


