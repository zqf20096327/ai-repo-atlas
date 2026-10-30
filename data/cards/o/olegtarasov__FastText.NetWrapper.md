# olegtarasov/FastText.NetWrapper

⭐ 79 · C# · MIT · 推送 2026-03-16 · [GitHub](https://github.com/olegtarasov/FastText.NetWrapper) · 个人维护

**fastText 的 .NET Standard 跨平台封装库**

为 Facebook fastText 原生 C++ 库提供跨平台 .NET Standard 封装，随包内置 Windows/Linux/macOS 预编译二进制，按目标平台自动解包调用。API 对应 fastText 命令行：监督/无监督（SkipGram/Cbow）训练、模型加载、量化、自动超参搜索、测试与 PR 曲线导出、训练进度回调、原生异常处理。限制：Windows 需安装 Visual C++ Runtime 140；预训练向量须为文本格式（.vec）。面向 .NET 开发者，通过 NuGet 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置三平台预编译原生二进制，无需额外配置
- 覆盖监督/无监督训练、量化与自动超参搜索（autotune）
- 测试输出含 Precision/Recall/F1 与 PR 曲线
- 训练进度回调与 NativeLibraryException 原生错误处理

## 适用场景

- 在 .NET 项目中训练和使用 fastText 文本分类模型
- 加载 .bin 模型进行文本预测并评估指标
- 对已有模型做量化以压缩体积

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: This is a cross-platform .NET Standard wrapper for Facebook's FastText library.
> L24: The simplest use case is to train a supervised model with default parameters. We create a `FastTextWrapper` and cal

## 星数曲线

```mermaid
xychart-beta
    title "olegtarasov/FastText.NetWrapper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-30 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b2cd34a6962c` · [字段定义](../../DATASET.md)*
