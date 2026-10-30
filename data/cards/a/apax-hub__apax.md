# apax-hub/apax

⭐ 39 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/apax-hub/apax) · [官网](https://apax.readthedocs.io) · 组织维护

**基于 JAX 的原子机器学习势训练与推断框架**

面向计算化学与材料科学领域的研究者和开发者，提供原子神经网络（Gaussian Moment Neural Network）的训练与推断功能。基于 JAX 构建，使用 JaxMD 作为分子动力学引擎；可通过 CLI 直接启动 NVT 分子动力学模拟，或通过 ASE calculator 使用模型。提供输入文件模板与 JSON schema 自动补全支持。通过 PyPI 安装，GPU 支持（仅 Linux）需额外安装 CUDA 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Gaussian Moment Neural Network 模型
- 基于 JAX，以 JaxMD 为分子动力学引擎
- CLI 直接启动 NVT 模拟，或经 ASE calculator 使用模型
- 生成训练与 MD 配置的 JSON schema 用于编辑器补全

## 适用场景

- 训练原子间势的机器学习模型
- 用训练好的模型运行分子动力学模拟
- 在基于 ASE 的工作流中使用学习势进行能量/力计算

## 场景标签

 · 领域:计算化学/材料科学

## 证据(README 行号)

> L8: `apax`[^1][^2] is a high-performance, extendable package for training of and inference with atomistic neural network
> L9: It implements the Gaussian Moment Neural Network model [^3][^4].

## 星数曲线

```mermaid
xychart-beta
    title "apax-hub/apax 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-30 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e2e796252f6d` · [字段定义](../../DATASET.md)*
