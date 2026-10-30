# HeroBlast10/polarity-agent

⭐ 26 · Python · MIT · 推送 2026-03-21 · [GitHub](https://github.com/HeroBlast10/polarity-agent) · [官网](https://www.polarityai.xyz/) · 个人维护 · 中文 README

**讽刺性双人格 AI Agent 框架：捧哏或杠精二选一死磕到底**

开源的讽刺性 Agent 框架，将 AI 人格锁定为两个极端：Advocatus 无条件支持用户一切主张，Inquisitor 无条件反对。人格由含 ROLEPLAY OVERRIDE 与 Few-Shot 的长文本系统提示实现，配 32 条参数化红队断言验证人格稳定性。支持对决模式（法庭辩论）、Web UI（FastAPI）、Next.js 前端与 Docker。底层用 LiteLLM 接入 100+ 模型（OpenAI、Claude、Ollama 等），推荐搭配未审查或本地模型。提供人格包自定义与 JSONL 追踪日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双人格立场锁定（永远支持/永远反对）+ 红队断言验证
- LiteLLM Provider 抽象接入 100+ 大模型
- 对决模式：律师 vs 检察官多轮辩论
- 人格包自定义（config.json + system_prompt.txt）与 JSONL 追踪日志

## 适用场景

- 想让 AI 无条件捧自己或无条件抬杠来解压娱乐
- 组织两个极端人格就任意话题进行辩论对战
- 用极端人格对 LLM 做对齐压力测试

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L29: 一个**讽刺性开源 Agent 框架**，将 AI 人格分裂成两个非黑即白的极端：
> L38: 这不是生产力工具。这是**情绪宣泄**、**梗图工厂**和**LLM 对齐压力测试**——全部打包进一个 `pip install`。

## 星数曲线

```mermaid
xychart-beta
    title "HeroBlast10/polarity-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d7e8838d1d74` · [字段定义](../../DATASET.md)*
