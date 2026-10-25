# Open-Quant/openquant

⭐ 52 · Jupyter Notebook · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Open-Quant/openquant) · [官网](https://open-quant.github.io/openquant/) · 组织维护

**Rust 实现金融机器学习方法（AFML）并带 Python 绑定的库**

以 Rust 实现《Advances in Financial Machine Learning》一书方法的库，核心覆盖该书大部分章节，并通过 maturin 构建 32 个子模块的 Python 绑定。当前处于预发布状态（0.1.0），未上架 crates.io/PyPI，需 Rust 工具链、Python 3.11+ 与 uv 从源码构建；官方说明后续将以 pyopenquant 名称发布到 PyPI。仓库含 Rust 测试套件、criterion 基准、notebooks 与配置驱动的实验 runner，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Rust 核心覆盖 AFML 大部分章节并在 CI 中测试
- Python 绑定暴露 32 个子模块（maturin 构建 wheel）
- 含基准测试快照、notebooks 与实验 runner

## 适用场景

- 用 Python 调用 AFML 中的金融机器学习方法
- 在量化研究流程中复现与基准测试 AFML 方法
- 基于 Rust 核心做低层性能基准比较

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5:  Rust implementations of the methods in Advances in Financial Machine Learning , with Python bindings.
> L18: Pre-release (0.1.0, unpublished). The Rust core covers most AFML chapters and is

## 星数曲线

```mermaid
xychart-beta
    title "Open-Quant/openquant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d9c43164ab57` · [字段定义](../../DATASET.md)*
