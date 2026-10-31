# jrcalgo/generative-mouse-trajectories

⭐ 15 · Rust · MIT · 推送 2026-08-01 · [GitHub](https://github.com/jrcalgo/generative-mouse-trajectories) · [官网](https://crates.io/crates/mouse-collection-environment) · 个人维护

**采集并生成拟真鼠标轨迹的 GAN 系统**

由三部分组成的项目：Rust（tokio/winit）实现的鼠标数据采集环境，实时记录时间、空间、运动学与行为指标并导出 CSV；对轨迹数据计算派生指标的分析组件；以及在采集数据上训练 GAN 的生成与演示组件，生成器从随机隐向量合成轨迹，判别器对照真实数据评估，支持通过隐空间控制速度与路径复杂度，并有演示应用让计算机自主执行生成的光标动作。项目以 MIT 许可发布，采集环境需从源码构建运行。

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

- Rust/tokio/winit 实时采集鼠标事件并导出结构化 CSV
- 记录时间、空间、运动学（速度/加速度/jerk/曲率）与行为指标
- GAN 生成轨迹，支持隐空间控制速度与路径复杂度
- 演示应用自主执行生成的光标动作

## 适用场景

- 为 UI 自动化测试生成类人交互序列
- 基于鼠标移动模式做行为生物特征认证研究
- 为辅助技术模拟人类交互

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: 3. **GAN-based Generation & Demonstration**: Trains GAN models on the collected data to generate realistic syntheti
> L41: We utilize advanced Generative Adversarial Networks (GANs) trained on collected mouse trajectory data. The GAN mode

## 星数曲线

```mermaid
xychart-beta
    title "jrcalgo/generative-mouse-trajectories 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `90fc03c4f49a` · [字段定义](../../DATASET.md)*
