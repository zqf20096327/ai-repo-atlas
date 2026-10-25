# AnonymousNomad/covert-coder

⭐ 53 · TypeScript · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/AnonymousNomad/covert-coder) · 个人维护

**本地优先的治理型 AI 软件工程工作台：模型作为可替换执行者**

面向操作者的 AI 开发环境：以本地运行为默认，协调上下文选择、工作流、模型身份路由、类型化工具执行、授权、验证与溯源。架构上将逻辑角色（Planner/Coder/Reviewer）与物理模型分离，模型提出的工具请求需经 schema 校验、权限检查与执行授权中介。本地运行时经 Runtime Broker 抽象，已限定冻结配置（Windows 11 + Unsloth + Vulkan + GTX 1060 Mobile + LFM2.5 GGUF）完成资格验证，llama.cpp 作为显式参考/恢复路径。工作台含 Monaco 编辑、Git、终端、TypeScript LSP、Python DAP 等已实现能力。当前状态为 Engineering Preview，进入受控测试招募，部分能力标注为实验性或部分实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型工具请求需经 schema 校验、权限检查与执行授权的边界处理
- Unsloth 被限定为规范 V1 本地运行时后端，llama.cpp 为显式参考/恢复路径
- Hugging Face 模型搜索、显式下载、断点续传与 GGUF 导入验证
- 工作台含 Monaco 编辑、Git、终端、TypeScript LSP、Python DAP 等已实现能力

## 适用场景

- 在本地运行和管理模型进行代码开发，控制网络出口
- 按逻辑角色混配本地与在线模型并保留操作者授权边界
- 对模型产生的工具调用做验证、溯源与回放

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: A governed AI development workbench for local and connected models, bounded context, typed tool execution, verificat
> L27: The workbench is designed to coordinate the complete engineering transaction around intelligence: context selection
> L121: ### Canonical V1 backend

## 星数曲线

```mermaid
xychart-beta
    title "AnonymousNomad/covert-coder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ad43f639c841` · [字段定义](../../DATASET.md)*
