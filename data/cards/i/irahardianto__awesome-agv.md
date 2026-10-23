# irahardianto/awesome-agv

⭐ 156 · Shell · MIT · 推送 2026-10-14 · [GitHub](https://github.com/irahardianto/awesome-agv) · [官网](https://irahardianto.github.io/awesome-agv/) · 个人维护

**给 AI 编码代理的规则与技能配置套件（25 规则/68 技能）**

面向 AI 编码助手（Antigravity、Roo Code、Cline 等）的 markdown 配置套件：包含 25 条规则（覆盖安全、可靠性、架构、可维护性）、68 个按需加载的技能（含 11 个命令技能）与 21 个子代理 Persona，采用三层加载机制（always-on mandates、按上下文激活的原则、按需技能）。基于标准 markdown 上下文协议，可移植到其他 AI 编码工具。通过 npx 交互式安装器安装，支持从技术栈文件自动检测并预选组件；也支持手动复制 .agents 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 条规则 + 68 个技能 + 21 个 Agent Persona，模块化可按需取用
- 三层加载系统：常驻强制规则、按上下文激活的原则、按需技能
- npx 交互式安装器，可从 go.mod/Cargo.toml 等自动检测技术栈
- 基于标准 markdown 上下文协议，可移植到多种 AI 编码工具

## 适用场景

- 为自己的 AI 编码助手配置安全与架构约束规则
- 按语言/框架挑选规则与技能加载到项目中
- 用命令技能（如 /audit、/bugfix）执行端到端开发流程

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Awesome AGV** provides a comprehensive set of standards and practices designed to elevate the capabilities of AI 
> L43: * An AI Coding Assistant (Antigravity, Roo Code, Cline, etc.)

## 星数曲线

```mermaid
xychart-beta
    title "irahardianto/awesome-agv 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 155 --> 157
    line [156, 156]
```

2026-10-18 156 → 2026-10-23 156（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `5b0474638eca` · [字段定义](../../DATASET.md)*
