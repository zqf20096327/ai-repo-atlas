# WeiminXiong/Video2GUI

⭐ 40 · JavaScript · Apache-2.0 · 推送 2026-06-29 · [GitHub](https://github.com/WeiminXiong/Video2GUI) · [官网](https://weiminxiong.github.io/Video2GUI/) · 组织维护 · 中文 README

**从互联网视频自动合成 GUI 交互轨迹数据集（WildGUI）的论文代码库**

ICML 2026 论文 Video2GUI 的代码与数据仓库：提出三阶段全自动流水线，从 5 亿条无标注互联网视频中筛选教程视频，经 Gemini-3-Pro 抽取指令—轨迹对并进行动作空间 grounding，构建覆盖 1,500+ 应用与网站、1,200 万条交互轨迹的 WildGUI 数据集（含标注与截图，托管于 HuggingFace，标注为 JSONL、截图打包为 tar 分片）。README 给出 datasets 库加载标注与 hf 下载截图的示例代码，并展示在 Qwen2.5-VL、MiMo-VL 上预训练带来多基准提升的结果声明。仓库以 Apache 2.0 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段流水线：视频过滤→轨迹抽取→动作空间 grounding
- WildGUI：12M 条交互轨迹，覆盖 web/mobile/desktop 三平台
- 标注与截图分两个 HuggingFace 仓库开放，附加载示例代码

## 适用场景

- 为 GUI agent 模型预训练获取大规模轨迹数据
- 复现论文中的数据合成流水线
- 研究跨应用、跨平台的 GUI 交互行为分布

## 场景标签

 · 领域:GUI Agent/数据集

## 证据(README 行号)

> L11: To address this, we propose **Video2GUI**, a fully automated framework that extracts grounded GUI interaction traje
> L35: WildGUI is the largest open-source GUI pre-training dataset to date, with comprehensive coverage across **web, mobi

## 星数曲线

```mermaid
xychart-beta
    title "WeiminXiong/Video2GUI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-26 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4d2063dbb500` · [字段定义](../../DATASET.md)*
