# czottmann/interfazzle

⭐ 23 · Swift · MIT · 推送 2025-12-06 · [GitHub](https://github.com/czottmann/interfazzle) · 个人维护

**从 Swift 符号图生成 Markdown 接口文档的 CLI 工具**

面向 Swift 包维护者的命令行工具：调用 Swift 编译器生成符号图 JSON，再转换为 Markdown 接口式文档（每模块一个文件，含目录、Xcode 风格接口代码块、README 集成与标题层级调整），输出格式参考了 LLM 阅读文档的偏好。提供 generate/build/validate 三个命令，自动过滤依赖模块，仅记录 public/open 符号。要求 macOS 与 Swift 6，需从源码构建安装；作者称其替代在其场景下失败的 sourcedocs。

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

- 符号图→Markdown 接口式文档的完整流水线（校验/构建/转换）
- 每模块单文件输出，含目录、接口代码块与 /// 文档注释
- 自动过滤依赖与 re-export，仅文档化 public/open API
- README 集成与标题层级自动调整

## 适用场景

- 为我的 Swift 包生成可读的公共 API Markdown 文档
- 为 LLM/agent 提供结构化的包接口文档上下文
- 在含预编译二进制依赖的包上替代 sourcedocs 生成文档

## 场景标签

 · 领域:开发者工具/文档生成

## 证据(README 行号)

> L3: A wee **Swift CLI tool** that builds **Markdown documentation for a package's public interface** from Swift symbol g
> L7: First and foremost, I built this for myself – it scratches my own itches! But it feels kinda useful, even more so no

## 星数曲线

```mermaid
xychart-beta
    title "czottmann/interfazzle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e84df3720b4c` · [字段定义](../../DATASET.md)*
