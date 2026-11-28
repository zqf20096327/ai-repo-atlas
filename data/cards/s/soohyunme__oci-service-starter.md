# soohyunme/oci-service-starter

⭐ 9 · HCL · MIT · 推送 2026-11-27 · [GitHub](https://github.com/soohyunme/oci-service-starter) · 个人维护

**帮个人开发者/小团队在 OCI 上由 AI 代理引导部署容器化 Web 服务的 Terraform 起始模板**

面向首次向 Oracle Cloud Infrastructure 部署服务的 1 人开发者与小型团队的 Terraform 起始仓库。使用方式是 Clone 后将内置请求文交给能读写终端与本地文件的 AI 代理，代理读取 AGENTS.md 与 prompts 文件，检查缺失配置、编写 terraform.tfvars、解释 Terraform Plan 中的资源变更与计费可能，并在用户明确批准后才执行 apply/destroy。构建的环境包含 VCN、Reserved Public IPv4、单台 VM.Standard.A1.Flex（2 OCPU/12GB/100GB）、Docker Compose、Caddy 与 SSH Key 认证。不含 Kubernetes、负载均衡、CI/CD 与数据库等配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代理驱动的审批优先工作流：apply/destroy 需用户明确批准
- 自动检查 Dockerfile、镜像 Registry、端口、域名与 ARM64 兼容性后接入应用
- Reserved Public IP 在 Compute 替换后可重新连接
- 安全基线：仅 SSH Key 认证、密钥不入 Git 与代理响应

## 适用场景

- 首次在 OCI 上部署自己的容器化 Web 服务
- 通过对话让代理解释 Terraform Plan 与计费项后再批准执行
- 将现有 Docker 镜像或应用仓库连接到新构建的 OCI 环境
- 不需要时让代理引导安全删除整套环境

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: OCI Service Starter는 Oracle Cloud Infrastructure(OCI)에 서비스를 처음 배포하려는 1인 개발자와 소규모 팀을 위한 저장소입니다. 저장소를 Clone한 뒤 제공된 요청문
> L7: OCI Console의 여러 설정 화면을 직접 따라가는 대신, 검토 가능한 Terraform 코드와 에이전트 가이드를 사용합니다. Terraform 적용 전에는 생성되는 리소스, 외부에 공개되는 포트와 과금 
> L126: 첫 버전은 한 대의 OCI Compute에서 하나 이상의 소규모 컨테이너 서비스를 운영하는 시작점을 제공합니다. 다음 항목은 포함하지 않습니다.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `c8be93f33974` · [字段定义](../../DATASET.md)*
