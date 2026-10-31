# kodejuice/arithmetic-compressor

⭐ 19 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/kodejuice/arithmetic-compressor) · 个人维护

**Python 算术编码压缩库，附 PPM/上下文混合统计模型**

以 Python 实现的算术编码数据压缩库，提供 AECompressor 压缩/解压接口，并附带一组自适应统计模型：静态模型、频率表、简单自适应模型、PPM（含多阶加权组合与二进制版本）、Context Mixing（线性证据混合与神经网络 Logistic 混合）。面向学习压缩算法与统计模型原理的开发者，附 /examples 示例。README 明确声明仅供学习与教育用途，实现未针对性能与内存优化，不建议直接用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AECompressor 支持字符串/列表的压缩与解压
- 10 种自适应统计模型（StaticModel 至 ContextMix_Logistic）
- MultiPPM/MultiBinaryPPM 以加权平均组合多阶 PPM 预测
- ContextMix_Logistic 使用神经网络（Logistic 域）混合多模型预测

## 适用场景

- 学习算术编码与 PPM、上下文混合等压缩算法原理
- 实验和对比不同统计模型对压缩效果的影响
- 作为教学/课程中概率推断与信息论的示例代码

## 场景标签

 · 领域:数据压缩/算法库

## 证据(README 行号)

> L5: This library is an implementation of the Arithmetic Coding algorithm in Python, along with adaptive statistical data
> L175: > _**Note**: This library is intended for learning and educational purposes only. The implementation may not be op

## 星数曲线

```mermaid
xychart-beta
    title "kodejuice/arithmetic-compressor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `035ab5a844b1` · [字段定义](../../DATASET.md)*
