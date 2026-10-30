# le0pard/json_mend

⭐ 22 · Ruby · MIT · 推送 2026-09-22 · [GitHub](https://github.com/le0pard/json_mend) · [官网](https://rubygems.org/gems/json_mend) · 个人维护

**修复 LLM 输出的破损 JSON 的 Ruby gem**

面向 Ruby 开发者的 JSON 修复库：解析、清洗并修复 LLM 常见的破损 JSON 输出，包括尾逗号、注释、单引号、未加引号的键值、截断的未闭合括号、Markdown 包裹与对话式前后缀等，输出合法 JSON 字符串或原生 Hash/Array。作为 LLM 输出与应用之间的中间层使用，通过 Gemfile 或 gem install 安装，主入口为 JsonMend.repair 方法，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 修复尾逗号、单引号/斜引号、未引号键值、注释剥离
- 处理截断 JSON：补全未闭合括号/花括号与 ... 占位符
- 可返回修复后的 JSON 字符串或原生 Ruby Hash/Array
- 启发式修复：合并悬挂数组、按重复键拆分对象

## 适用场景

- 解析 LLM 输出的结构化数据时避免 JSON::ParserError
- 剥离 LLM 回答中的 Markdown 代码块与对话前缀后提取数据
- 修复被截断的长 JSON 输出

## 场景标签

 · 领域:LLM 工具库/数据处理

## 证据(README 行号)

> L3: `JsonMend` is a robust Ruby gem designed to repair broken or malformed JSON strings. It is specifically optimized to
> L15: `JsonMend` acts as a middleware layer between the messy text output of an LLM and your Ruby application. It aggress

## 星数曲线

```mermaid
xychart-beta
    title "le0pard/json_mend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `541502f4b87d` · [字段定义](../../DATASET.md)*
