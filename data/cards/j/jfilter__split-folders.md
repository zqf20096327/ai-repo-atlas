# jfilter/split-folders

⭐ 424 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/jfilter/split-folders) · 个人维护

**把含文件的文件夹按比例切分为训练/验证/测试集的 Python 工具**

面向机器学习/深度学习数据准备阶段的 Python 包（含 CLI）：读取含类别子目录或扁平结构的输入文件夹，按 ratio 或 fixed 两种模式切分为 train/val/test（val/test 可选）。支持任意文件类型、随机种子可复现、可关闭 shuffle 以适配时间序列、对不平衡数据做随机过采样（仅作用于 train）。提供按前缀/stem/兄弟目录/callable 的分组机制，保证图像与标注等关联文件同切分，也支持仅切分指定扩展名与移动/复制/软链接三种方式。无外部依赖，开发用 poetry。

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

- ratio 与 fixed 两种切分模式，seed 可复现
- 不平衡数据的随机过采样（仅 train 集）
- 按 stem/sibling/callable 分组，保持图像与标注成对
- 同时提供 Python 模块与 CLI，纯 Python 无外部依赖

## 适用场景

- 训练图像分类模型前把数据集切分为训练/验证/测试集
- 把图像及其标注文件成对地分到同一子集
- 对类别不平衡的数据集做训练集过采样

## 场景标签

 · 领域:机器学习/数据工具

## 证据(README 行号)

> L3: Split folders with files (e.g. images) into **train**, **validation** and **test** (dataset) folders.
> L32: This should get you started to do some serious deep learning on your data. Read here why it's a good idea to split 

## 星数曲线

```mermaid
xychart-beta
    title "jfilter/split-folders 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 423 --> 425
    line [424, 424]
```

2026-10-18 424 → 2026-10-26 424（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `7e9668057b37` · [字段定义](../../DATASET.md)*
