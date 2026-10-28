# Resk-Security/Resk-LLM

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Resk-Security/Resk-LLM) · [官网](https://resk.fr/projects/resk-llm.html) · 组织维护

**LLM 调用安全层：在输入期拦截提示注入并防护输出泄露**

Python 库，为 LLM API 调用提供安全防护层：由 11 个检测器（直连注入、越狱、记忆投毒、目标劫持、数据渗出、Agent 间注入、TF-IDF/Qdrant/Pinecone/pgvector 向量相似度等）组成管道，在输入期扫描请求；配合 InputSanitizer、OutputValidator（PII/凭据泄露检查）与 CanaryManager（金丝雀令牌检测上下文泄露）。规则集中于可编辑的 patterns.yaml，无需改代码调整。提供 FastAPI 中间件、OpenAI 客户端包装、多轮 ConversationContext 升级检测与 CLI。基础安装仅依赖 pyyaml；含 LLM Guard 归档后的兼容迁移层。给需要为 LLM 应用接入安全扫描的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个检测器在输入期运行，含注入/越狱/记忆投毒/数据渗出等专项检测
- 规则集中于用户可编辑的 patterns.yaml，无需改代码
- Canary 金丝雀令牌检测上下文泄露，OutputValidator 检查 PII/凭据
- FastAPI 中间件、OpenAI 包装器与 LLM Guard scan_prompt/scan_output 兼容层

## 适用场景

- 为 LLM API 服务加上中间件，拦截提示注入与越狱攻击
- 从已归档的 LLM Guard 迁移现有扫描器配置
- 检测响应中的 PII 与凭据泄露并做泄露取证

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: > Stops prompt injections before they reach your LLM — in one line.
> L42: That's it. Add a middleware and every request to your API is scanned:
> L91: - **Integrations**: FastAPI middleware, OpenAI client wrapper, resk-logits generation-time shadow ban, multi-turn `

## 星数曲线

```mermaid
xychart-beta
    title "Resk-Security/Resk-LLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d5683931a2c8` · [字段定义](../../DATASET.md)*
