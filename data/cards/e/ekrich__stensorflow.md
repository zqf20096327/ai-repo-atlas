# ekrich/stensorflow

⭐ 43 · Scala · NOASSERTION · 推送 2026-09-09 · [GitHub](https://github.com/ekrich/stensorflow) · 个人维护

**给 Scala Native 开发者：在 Scala Native 平台绑定 TensorFlow C API**

将 TensorFlow C API 适配到 Scala Native 平台的绑定库，支持在编译为本地代码的 Scala 程序中使用 TensorFlow。通过 sbt 添加 Maven Central 依赖即可使用，提供 Gitter8 模板快速起步。要求系统上安装 TensorFlow C 库（当前版本 2.16.1）：Linux 通过下载 tar 包安装，macOS 可用 Homebrew（建议 macOS 12 以上）。支持 Scala 3.3.x LTS 与 Scala Native 0.5.x，运行于 Linux 和 macOS。文档以 Scaladoc 与单元测试示例为主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TensorFlow C API 的 Scala Native 绑定（当前支持 C 库 2.16.1）
- Maven Central 发布，sbt 依赖引入
- 提供 Gitter8 模板 stensorflow.g8 快速创建示例应用
- 支持 Scala 3.3.x LTS / Scala Native 0.5.x，Linux 与 macOS

## 适用场景

- 在 Scala Native 项目中调用 TensorFlow 构建神经网络应用
- 希望 Scala 代码编译为本地可执行文件并使用 C 语言机器学习库
- 用模板快速搭建带 TensorFlow 示例的 Scala Native 应用

## 场景标签

 · 领域:机器学习/编程库

## 证据(README 行号)

> L4: This library implements the C TensorFlow API adapted for the Scala Native platform.
> L48: The TensorFlow C library is required and the current version is `2.16.1`

## 星数曲线

```mermaid
xychart-beta
    title "ekrich/stensorflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6a2433ad0616` · [字段定义](../../DATASET.md)*
