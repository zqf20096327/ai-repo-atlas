# lambdasec/frame

⭐ 49 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/lambdasec/frame) · 组织维护

**结合分离逻辑静态分析与可选 LLM 层的代码安全扫描工具**

面向开发者的 SAST 工具：通过追踪攻击者数据在函数、文件与层间的流动发现漏洞，用基于 Z3 的分离逻辑引擎（含 frame 推断、bi-abduction、反模型）证明每个发现而非模式匹配；支持 Python、JS/TS、Java、C#、C/C++ 五种语言与 70+ 框架包。可选 LLM 层运行于本地或托管的开放模型，用于补充召回、triage、漏洞利用与修复。提供 GitHub Action、pre-commit hook 与 MCP server 接入编码 agent。Apache 2.0 许可，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Z3 的自研分离逻辑引擎，以求解器证明发现
- 跨文件默认追踪污点数据流，覆盖 5 种语言
- 70+ 框架包，可自写 TOML 定义技术栈
- 可选 LLM 层运行于开放模型（本地或托管）做检测/triage/利用/修复
- GitHub Action、pre-commit hook 与 MCP server 三种接入方式

## 适用场景

- 在 CI 或提交前扫描代码中的跨文件安全漏洞
- 验证修复是否真正消除了漏洞、对已接受项做基线
- 让 Claude Code / Cursor 等编码 agent 通过 MCP 调用安全扫描

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Frame finds vulnerabilities by **following attacker data through your code**, across functions, files and layers, a
> L22: - **Its own separation logic engine** on Z3: entailment, frame inference, bi-abduction and countermodels.
> L73: |AI layer|Detect, triage, exploit and fix with any OpenAI-compatible model, including on-device|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7eef77a29c76` · [字段定义](../../DATASET.md)*
