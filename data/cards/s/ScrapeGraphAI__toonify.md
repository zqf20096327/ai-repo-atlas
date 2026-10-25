# ScrapeGraphAI/toonify

⭐ 366 · Python · 推送 2026-02-06 · [GitHub](https://github.com/ScrapeGraphAI/toonify) · [官网](https://docs.scrapegraphai.com/services/toonify) · 组织维护

**面向 LLM 的紧凑序列化格式，降低 token 用量**

TOON（Token-Oriented Object Notation）是 Python 序列化库与 CLI 工具，将结构化数据编码为比 JSON 紧凑的缩进式文本（50 个数据集测试平均缩小 63.9%、token 减少 54.1%），用于向 LLM API 传递数据以降低成本。支持字符串/数字/布尔/null 类型、三种分隔符、表格化数组、键折叠与路径展开，并可直接转换 Pydantic v1/v2 模型、生成可嵌入 LLM 提示词的响应结构模板。实现受 TypeScript 版 TOON 库启发，由 ScrapeGraphAI 团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- encode/decode 双向转换，平均比 JSON 小 63.9%、token 少 54.1%
- Pydantic v1/v2 直接转换与解码时校验
- generate_structure 生成可嵌入 LLM 提示词的响应结构模板
- 键折叠、路径展开与三种可选分隔符

## 适用场景

- 把结构化数据传给 LLM API 时压缩 token 开销
- 在有限上下文窗口中塞入更多数据
- 用结构模板约束 LLM 返回数据的格式
- 表格类数据在 LLM 流水线中的序列化

## 场景标签

 · 领域:LLM 数据格式/开发工具

## 证据(README 行号)

> L7: A compact, human-readable serialization format designed for passing structured data to Large Language Models with si
> L16: - Reducing token costs in LLM API calls

## 星数曲线

```mermaid
xychart-beta
    title "ScrapeGraphAI/toonify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 363 --> 365
    line [364, 364]
```

2026-10-18 364 → 2026-10-25 364（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d687d6c96087` · [字段定义](../../DATASET.md)*
