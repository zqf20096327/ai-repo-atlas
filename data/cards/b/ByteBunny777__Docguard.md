# ByteBunny777/Docguard

⭐ 34 · Go · MIT · 推送 2026-07-08 · [GitHub](https://github.com/ByteBunny777/Docguard) · 个人维护

**扫描文档中隐藏提示注入内容的 Go CLI，供 RAG 索引前把关**

用 Go 编写的并发命令行工具，在文档进入 RAG 知识库或被索引前扫描其中的隐藏内容：Unicode tag 走私（解码隐藏 ASCII 载荷）、零宽字符、同形字、隐藏 HTML/CSS、已知注入触发短语及 base64 自然语言编码块。采用 goroutine 工作池并发扫描，仅依赖 Go 标准库，编译为单一静态二进制，可接入 CI 按严重级别门禁构建。README 自述为启发式绊线而非完备检测器，误报发现仅代表需要人工复核。需 Go 1.22+ 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 解码 Unicode tag 字符（U+E0000–U+E007F）中的隐藏 ASCII 载荷
- 检测同形字、零宽字符、隐藏 HTML/CSS、触发短语与 base64 编码块
- goroutine 工作池并发扫描，零外部依赖，单一静态二进制
- 退出码按严重级别设计，可直接接入 CI 门禁

## 适用场景

- 知识库文档入 RAG 索引前扫描隐藏提示注入内容
- 在 CI 中对新增文档做安全门禁，发现高危内容即失败构建
- 人工复核前快速筛出常见的低成本混淆注入手法

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: A concurrent Go CLI that scans documents for content that's **invisible or
> L31: before it's indexed, or wire into CI so a pull request that adds a

## 星数曲线

```mermaid
xychart-beta
    title "ByteBunny777/Docguard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-27 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4bf24f49d86a` · [字段定义](../../DATASET.md)*
