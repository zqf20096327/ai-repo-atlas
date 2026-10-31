# Danipulok/pydantic-jsonschema

⭐ 14 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Danipulok/pydantic-jsonschema) · [官网](https://danipulok.github.io/pydantic-jsonschema/) · 个人维护

**将 JSON Schema 转换为 Pydantic 模型并做运行时校验的 Python 库**

做 Pydantic 反向转换的 Python 库：读取已有的 JSON Schema（含 $ref/$defs 解析），生成 Pydantic 模型，从而用 Pydantic 的运行时校验检查数据。面向 schema 先行的场景：API 契约、配置文件、工具定义、按固定结构校验 LLM 输出。包含四个组件：Schema/Reference 模型、转换器（支持 anyOf/oneOf/allOf 映射与判别联合）、内置 format 类型（email/uri/uuid 等，零额外依赖）、按类型/路径/谓词匹配的输入输出转换规则。要求 Python 3.12+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSON Schema → Pydantic 模型转换，$ref/$defs 解析
- anyOf/oneOf/allOf（含判别联合）映射到 Python 类型
- 内置全部 JSON Schema format 类型，零额外依赖
- Rule 机制支持按类型/JSON Pointer 路径/谓词做输入强制转换与输出序列化

## 适用场景

- 按 API 契约或配置文件的 schema 校验数据
- 将 LLM 输出校验为固定结构
- 为已有的 JSON Schema 生成带类型提示的 Pydantic 模型

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: **Pydantic turns models into JSON Schema. This library does the reverse** — it turns a
> L19: or validating LLM output against a fixed shape.

## 星数曲线

```mermaid
xychart-beta
    title "Danipulok/pydantic-jsonschema 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6b5099fb5992` · [字段定义](../../DATASET.md)*
