# jezs00/pycasso

⭐ 89 · Python · MIT · 推送 2026-06-30 · [GitHub](https://github.com/jezs00/pycasso) · 个人维护

**树莓派电子墨水屏展示 AI 生成艺术画**

运行在树莓派上的系统：通过 API 向 OpenAI 或 Stable Diffusion 请求图像，驱动 omni-epd 兼容的电子纸屏（EPD）显示；也可加载本地外部图片。提供 Bash 安装脚本（含菜单式安装/升级/服务开机自启）、.config 配置、提示词随机化语法（括号通配符、权重）与 Prompt Blocks（可调用 LLM 改写文本）。支持 PiJuice HAT 电池供电与定时唤醒、用后自动关机。需付费 API key（以明文存储），需树莓派与 EPD 硬件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 openai 与 Stable Diffusion 图像生成 API（需付费 key）
- 通过 omni-epd 驱动多种型号电子纸屏
- 括号通配符与权重、Prompt Blocks 动态生成提示词
- PiJuice 电池供电、定时唤醒与用后关机支持无头运行

## 适用场景

- 用电子墨水屏做每日 AI 艺术画框
- 电池供电的离线部署壁画装置
- 配置自己的提示词库随机生成画作展示

## 场景标签

`图像生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L2: System to send AI generated art to an E-Paper display through a Raspberry PI unit
> L39: * Select `Option 7 - Set an API key or connect website`, enter your provider and enter your key. Currently supporti

## 星数曲线

```mermaid
xychart-beta
    title "jezs00/pycasso 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 87 --> 90
    line [88, 89, 89]
```

2026-10-18 88 → 2026-10-30 89（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `96b5a90ff246` · [字段定义](../../DATASET.md)*
