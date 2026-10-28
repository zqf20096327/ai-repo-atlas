# pavansai20052004-hue/rocmporter-agent

⭐ 19 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/pavansai20052004-hue/rocmporter-agent) · [官网](https://rocmporter-agent.vercel.app) · 个人维护

**扫描 GitHub 仓库 CUDA 依赖并自动生成 ROCm 迁移 PR 的工具**

面向需要将 CUDA 代码迁移到 AMD ROCm 的开发团队：克隆 GitHub 仓库做静态分析，逐条给出文件/行级证据的 CUDA 依赖发现与 0–100 ROCm 就绪度评分；迁移采用混合引擎——先用确定性 hipify 转换大部分机械改动，再由 LLM（可插拔：OpenAI/Groq/OpenRouter/DeepSeek/Anthropic，本地可用 Ollama）基于 18 个 API 族知识库补齐语义改动，经语法检查与 diff 回放验证后可一键开启迁移 PR。另含 VS Code 扩展、GitHub Action、hipcc 容器编译校验。限制：迁移 PR 每次最多 10 个文件；AI 补丁为付费功能；后端需真实服务器不能跑在 serverless。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件/行/代码片段级证据的 CUDA 依赖扫描与 0–100 就绪度评分
- 确定性 hipify 优先 + AI 仅处理语义残余的混合迁移引擎（带逐文件溯源）
- 在 AMD 官方 ROCm 容器中用 hipcc 做编译校验
- VS Code 扩展、GitHub Action、README 就绪度徽章

## 适用场景

- 评估仓库从 CUDA 迁移到 AMD ROCm 的成本与风险
- 让工具自动改写 CUDA 代码并开出迁移 PR
- 在 CI 中对每个 PR 附加 ROCm 就绪度评论

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **ROCmPorter scans any GitHub repository for NVIDIA / CUDA dependencies, scores its AMD ROCm readiness with line-lev
> L40: |🤖 **Hybrid hipify + AI patches**|A deterministic CUDA→HIP mapping pass converts the mechanical majority with **zer
> L117: - **AI** — pluggable provider (OpenAI / Groq / OpenRouter / Together / DeepSeek / Anthropic, or local Ollama for d
> L142: For local AI patches, run Ollama with a coding model; or set `LLM_PROVIDER` + `LLM_API_KEY` to use a hosted model.

## 星数曲线

```mermaid
xychart-beta
    title "pavansai20052004-hue/rocmporter-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-28 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ff69a572cd7b` · [字段定义](../../DATASET.md)*
