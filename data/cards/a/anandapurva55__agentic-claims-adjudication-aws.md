# anandapurva55/agentic-claims-adjudication-aws

⭐ 22 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/anandapurva55/agentic-claims-adjudication-aws) · [官网](https://anandapurva55.github.io/agentic-claims-adjudication-aws/) · 个人维护

**面向车险理赔审核员的多智能体理赔裁决系统**

部署在 AWS 上的车险理赔裁决全栈系统：读取理赔表单、维修估价与损伤照片，对照保险条款给出 approve/deny/refer 建议，最终决定始终由人做出。机制上以 Strands Agents 编排多个 Bedrock 模型驱动的 agent，经 MCP 提供工具，用 Bedrock Knowledge Bases 做 RAG 条款检索，AgentCore Memory 记录纠正教训，Guardrails 过滤注入文本；由普通代码的规则引擎计算赔付金额，API 拒绝无人工记录的裁决。前端 React/TypeScript，后端 FastAPI，AWS CDK 定义全部资源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 编排（Strands）+ MCP 工具 + RAG 条款检索 + AgentCore 记忆
- 模型判定、规则引擎决策，API 强制要求人工裁决记录
- Bedrock Guardrails 提示注入过滤、PII 检测与拒答主题
- GitHub Pages 提供无服务器交互演示（AI 关闭，回放规则基线）

## 适用场景

- 车险理赔员对照保险条款审核理赔材料
- 多 agent 编排架构在保险裁决场景的参考实现
- 带人工审核环节的 AI 决策流程落地

## 场景标签

`多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L25: This project helps an insurance adjuster decide a motor insurance claim. A claim arrives as a claim form, a repair 
> L30: 4. **A team of AI agents reads the claim.** **Strands Agents** does the orchestration. It builds each agent on a mo
> L33: 7. **A person decides.** The recommendation appears in the app as it is produced. The adjuster accepts it, override


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `956aaa65268d` · [字段定义](../../DATASET.md)*
