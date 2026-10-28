# janosh/tensorboard-reducer

⭐ 78 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/janosh/tensorboard-reducer) · [官网](https://pypi.org/project/tensorboard-reducer) · 个人维护

**将多个 TensorBoard 运行聚合成统计曲线的工具，供 ML 实验者降噪对比**

Python 库与 CLI（tb-reducer）：读取多个 TensorBoard run 目录的事件文件，按 numpy 操作（mean/std/min/max/median 等）计算统计量，输出为新的 TensorBoard run 或 CSV/JSON/Excel 文件。面向训练模型集成、需要降低 loss/accuracy 曲线噪声并评估性能差异显著性的 PyTorch/TensorFlow 用户。默认要求各 run 的 tag 与 step 数一致，可用 lax-tags/lax-steps 放宽。要求 Python 3.8+，通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持任意 numpy 规约操作（mean/std/min/max/median 等）
- 输出为新的 TensorBoard run 或 CSV/JSON/Excel 文件
- 提供 CLI 与 Python API 两种使用方式，附 Colab/Binder 示例笔记本
- 可处理 tag 不一致、step 不等、重复 step 等情况（多种容错标志）

## 适用场景

- 训练模型集成后对多条 loss/accuracy 曲线求均值以降噪
- 对比不同模型或训练技术时建立统计上的性能参考
- 把多个 run 的规约结果导出为 CSV/Excel 供后续分析

## 场景标签

 · 领域:机器学习工具/实验可视化

## 证据(README 行号)

> L11: Compute statistics (`mean`, `std`, `min`, `max`, `median` or any other `numpy` operation) of multiple TensorBoard r
> L41: tb-reducer runs/of-your-model* -o output-dir -r mean,std,min,max

## 星数曲线

```mermaid
xychart-beta
    title "janosh/tensorboard-reducer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-28 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cc26c1974fc0` · [字段定义](../../DATASET.md)*
