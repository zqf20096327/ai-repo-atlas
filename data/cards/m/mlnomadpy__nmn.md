# mlnomadpy/nmn

⭐ 19 · Python · NOASSERTION · 推送 2026-09-14 · [GitHub](https://github.com/mlnomadpy/nmn) · [官网](https://pypi.org/project/nmn/) · 组织维护

**免激活函数的几何神经网络层库，支持六大框架**

NMN 提供 Yat 系列神经网络层（Dense、Conv、Attention、Embedding），通过相似度与距离的几何比值在层内实现非线性，替代 Linear/Conv+激活的组合。同一套层以 PyTorch、Flax NNX、Flax Linen、Keras 3、TensorFlow、MLX 六种后端交付，附机器可读的 conformance manifest 与 NumPy float64 oracle 对照测试。提供 pip 安装、CLI 诊断命令（nmn doctor）、每框架可运行示例脚本。许可为 PolyForm Noncommercial 1.0.0（非商用）。ONNX 导出与 INT8 量化尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Yat 层以几何比值实现内建非线性，无需外部激活函数
- 六框架统一交付：PyTorch/Flax NNX/Flax Linen/Keras 3/TensorFlow/MLX
- 机器可读 conformance_manifest.json 与 NumPy oracle 对照验证
- O(n) 线性注意力特征图（SLAY/MAY/RAY）与 lazy 冻结核训练模式

## 适用场景

- 在现有 PyTorch/JAX/Keras 模型中用 Yat 层替换 Linear+激活块
- 在 Apple Silicon 上以 MLX 后端运行 Yat 层
- 用长序列场景下的线性化 Yat 注意力替代精确注意力
- 跨框架迁移同一模型结构并核验数值一致性

## 场景标签

 · 领域:深度学习/神经网络库

## 证据(README 行号)

> L31: NMN is a drop-in replacement for `Linear + activation` and `Conv + activation` blocks. The non-linearity is **built

## 星数曲线

```mermaid
xychart-beta
    title "mlnomadpy/nmn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3375dde3e831` · [字段定义](../../DATASET.md)*
