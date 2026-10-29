# livingbio/fuzzy-json

⭐ 45 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/livingbio/fuzzy-json) · 个人维护

**零依赖 Python 库：自动修复 LLM 输出的非法 JSON**

面向使用 OpenAI function call 等场景的开发者的 JSON 修复库：语言模型输出的 JSON 常含尾逗号、未转义引号、缺失闭合括号或 Markdown 包裹等问题，导致 JSONDecodeError。该库基于下推自动机在正确位置修复非法 JSON 结构，提供 fuzzy_json.loads 作为 json.loads 的即插替代，合法 JSON 原样通过，也可设 auto_repair=False 严格解析。零依赖，pip 安装，覆盖不到的案例可通过 issue 反馈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 下推自动机在正确位置修复非法 JSON 结构
- 作为 json.loads 的 drop-in 替代，零依赖
- 支持修复尾逗号、未转义引号、缺失闭合括号、Markdown 包裹 JSON
- auto_repair=False 可切回严格解析

## 适用场景

- 解析 OpenAI function call 返回的非法 JSON
- 处理 LLM 输出中带 Markdown 代码块的 JSON
- 避免靠重试或改写提示词来解决 JSON 解析失败

## 场景标签

 · 领域:LLM 输出后处理工具

## 证据(README 行号)

> L14: - Fuzzy-JSON is a compact Python package with no dependencies, designed to address the pesky `JSONDecodeError` that
> L16: - To tackle this problem, Fuzzy-JSON employs a pushdown automata capable of incorporating JSON syntax and rectifyin
> L45: `fuzzy_json.loads` works as a drop-in replacement for `json.loads`, but automatically repairs common issues found i

## 星数曲线

```mermaid
xychart-beta
    title "livingbio/fuzzy-json 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `292a50596fdc` · [字段定义](../../DATASET.md)*
