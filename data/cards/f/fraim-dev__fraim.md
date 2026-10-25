# fraim-dev/fraim

⭐ 159 · Python · MIT · 推送 2026-02-09 · [GitHub](https://github.com/fraim-dev/fraim) · [官网](https://www.fraim.dev) · 组织维护

**面向安全团队的 AI 安全工作流框架：代码与 IaC 漏洞检测、PR 风险标记**

Fraim 是供安全工程师构建和运行 AI 驱动安全工作流的 Python 框架，可作为 CLI 或 GitHub Actions 运行。内置三类工作流：Risk Flagger（按自定义风险规则决定是否对 PR 请求安全审查）、Code Security Analysis（LLM 上下文感知的代码漏洞分析）、IAC Analysis（Terraform/CloudFormation/Kubernetes 清单审查），输出 SARIF 等格式。支持 Anthropic、OpenAI、Google Gemini 等模型 API，需自带 API key；可经 Langfuse 做观测。提供 Workflow Engine、工具系统与输入连接器用于自定义工作流。要求 Python 3.12+，经 pipx/PyPI 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Risk Flagger：按自定义风险条件决定是否对 PR 请求安全审查
- 代码安全分析：LLM 驱动、上下文感知的跨语言漏洞审查，支持 SARIF 输出
- IaC 分析：覆盖 Terraform/CloudFormation/Kubernetes 清单
- 框架组件：Workflow Engine、多 LLM 集成、工具系统、多种输出格式

## 适用场景

- 在 PR 流程中只对存在风险变更的代码请求安全审查
- 对全仓库或 diff 做漏洞与云配置问题的 AI 分析并接入 CI
- 基于框架组件构建组织自定义的安全工作流

## 场景标签

`网络安全` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: Fraim gives security engineers AI-powered workflows to help them leverage the power of AI to solve REAL business ne
> L36: Most security teams rely on signature-based scanners and scattered linters that miss context and overwhelm engineer

## 星数曲线

```mermaid
xychart-beta
    title "fraim-dev/fraim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 158 --> 160
    line [159, 159]
```

2026-10-18 159 → 2026-10-25 159（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `29e54f190970` · [字段定义](../../DATASET.md)*
