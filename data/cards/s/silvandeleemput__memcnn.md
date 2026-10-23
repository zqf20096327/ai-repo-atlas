# silvandeleemput/memcnn

⭐ 257 · Python · MIT · 推送 2026-03-12 · [GitHub](https://github.com/silvandeleemput/memcnn) · 个人维护

**开发内存高效可逆神经网络的 PyTorch 框架**

面向深度学习研究者的 Python/PyTorch 框架：通过 InvertibleModuleWrapper 包装任意可逆 PyTorch 函数，在训练时以重计算换取激活内存节省；提供 AdditiveCoupling/AffineCoupling 将非线性函数转为可逆版本，并附带复现 RevNet 实验的训练评估代码。支持 CIFAR-10/100 上多种 ResNet/RevNet 模型，可选 CUDA 或 CPU 训练。README 明确声明项目不再维护，代码仅供参考与历史用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- InvertibleModuleWrapper 包装可逆模块实现训练内存节省，keep_input 属性可切换
- AdditiveCoupling / AffineCoupling 将任意非线性 PyTorch 函数转为可逆版本
- 提供复现 RevNet 实验的训练评估代码（CIFAR-10/100，ResNet/RevNet 多种规模）
- 附 JOSS 论文（DOI 10.21105/joss.01576）与内存消耗对比数据

## 适用场景

- 训练深层可逆网络时降低激活内存占用
- 复现或对比 ResNet/RevNet 在 CIFAR 上的实验结果
- 将自定义操作改造成可逆模块并验证其可逆性

## 场景标签

 · 领域:深度学习/机器学习工具库

## 证据(README 行号)

> L47: A `PyTorch <http://pytorch.org/>`__ framework for developing memory-efficient invertible neural networks.
> L63: * Enable memory savings during training by wrapping arbitrary invertible PyTorch functions with the `InvertibleModu

## 星数曲线

```mermaid
xychart-beta
    title "silvandeleemput/memcnn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 256 --> 258
    line [257, 257]
```

2026-10-18 257 → 2026-10-23 257（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `278be5482f7e` · [字段定义](../../DATASET.md)*
