# alpkeskin/gotoon

⭐ 241 · Go · MIT · 推送 2025-11-24 · [GitHub](https://github.com/alpkeskin/gotoon) · 个人维护

**面向 Go 的 TOON 序列化库：给 LLM 传数据省 30-60% token**

TOON（Token-Oriented Object Notation）格式的 Go 实现：将结构体、map、切片编码为紧凑的缩进式文本格式，替代 JSON 传给 LLM，按官方基准（GPT-5 tokenizer）整体减少约 49.1% token。核心机制：同构对象数组采用表格式编码（键名只声明一次）、仅在必要时加引号、map 键按字母序排序保证输出确定性；通过函数式选项配置缩进、分隔符与长度标记。以 go get 安装的 Go 包形式提供，含示例与表格驱动测试。限制：面向均匀结构化对象效果最佳，非同构数组退化为列表格式。

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

- Encode 将任意 Go 值转为 TOON 格式，基准显示整体 49.1% token 缩减
- 同构对象数组使用表格式编码，键名声明一次后流式输出行
- 支持 WithIndent/WithDelimiter/WithLengthMarker 函数式选项
- 确定性输出：map 键按字母序排序

## 适用场景

- 我在 Go 后端把数据库查询结果编码后传给 LLM，减少 token 开销
- 我需要让 LLM 以紧凑格式返回结构化数据
- 我想在 prompt 中用更短的自描述格式替代 JSON 示例

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: **GoTOON** is a Go implementation of TOON (Token-Oriented Object Notation), a compact, human-readable format design
> L12: TOON excels at **uniform complex objects** – multiple fields per row, same structure across items. It achieves **30

## 星数曲线

```mermaid
xychart-beta
    title "alpkeskin/gotoon 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 239 --> 242
    line [240, 241, 241]
```

2026-10-18 240 → 2026-10-25 241（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b743c8cc9b89` · [字段定义](../../DATASET.md)*
