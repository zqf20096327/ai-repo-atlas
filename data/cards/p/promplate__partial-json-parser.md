# promplate/partial-json-parser

⭐ 140 · Python · MIT · 推送 2026-04-22 · [GitHub](https://github.com/promplate/partial-json-parser) · [官网](https://promplate.dev/partial-json-parser) · 组织维护

**解析 LLM 流式输出中不完整 JSON 的 Python 库**

轻量级零依赖的 Python 库，用于解析 LLM 流式生成过程中尚未结束的不完整 JSON 字符串：loads 函数在接收最后一个 token 前即可解码出已生成的部分数据，ensure_json 返回补全后的 JSON 字符串。通过 Allow 枚举按位 OR 控制允许哪些类型（字符串/数字/数组/对象等）处于部分状态。纯 Python 实现，带类型标注，支持 Python 3.6+，另有 JavaScript 实现，附交互式 playground 与 Hypothesis/Pytest 测试。

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

- loads/ensure_json 解析或补全流式场景下的不完整 JSON
- Allow 枚举按位控制允许部分化的类型
- 零依赖、纯 Python 实现，支持 Python 3.6+
- 提供交互式 demo playground（json-playground）

## 适用场景

- LLM 流式输出结构化 JSON 时边生成边解析并展示给用户
- 在接收完最后一个 token 前补全 JSON 字符串
- agent 应用中处理 LLM 产生的不完整结构化数据

## 场景标签

 · 领域:LLM 开发工具库

## 证据(README 行号)

> L5: But before receiving the last token of response, the JSON is broken, which means you can't use `JSON.parse` to decod
> L7: Here comes `partial-json-parser`, a lightweight and customizable library for parsing partial JSON strings. Here is a

## 星数曲线

```mermaid
xychart-beta
    title "promplate/partial-json-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 139 --> 141
    line [140, 140]
```

2026-10-18 140 → 2026-10-26 140（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ae0d953e1eaa` · [字段定义](../../DATASET.md)*
