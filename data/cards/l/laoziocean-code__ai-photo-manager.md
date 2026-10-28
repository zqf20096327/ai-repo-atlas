# laoziocean-code/ai-photo-manager

⭐ 33 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/laoziocean-code/ai-photo-manager) · 个人维护 · 中文 README

**从海量照片中自动精选好照片的 AI 摄影管理工具**

面向摄影爱好者与普通用户的多平台照片精选应用：本地完成 Hash 去重、感知哈希相似检测、模糊/过曝/欠曝过滤等预处理（零 API 成本），再调用视觉模型（智谱 GLM-V4、OpenAI GPT、Gemini、Claude 或任意 OpenAI 兼容端点）做 8 维度评分与摄影师点评，输出精选目录、Lightroom 后期建议与 HTML 报告。通过 rawpy/LibRaw 支持全格式 RAW。桌面版为 PySide6，手机版为 Flask 后端加浏览器前端；需用户自备 API Key 且分析时照片内容会发送至所选模型服务商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地预处理（去重/模糊/过曝/欠曝过滤）零 API 成本
- 视觉模型 8 维度评分与拟人化摄影师点评
- rawpy/LibRaw 全格式 RAW 支持，含文件头魔数兜底
- Windows/macOS 安装包与手机 Web 版（局域网访问）

## 适用场景

- 从大量照片中自动挑出好照片并了解推荐理由
- 获得照片评分、点评与 Lightroom 后期调整建议
- 生成可分享的杂志风摄影分析报告

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L18: - **AI 视觉评分**：8 维度打分（构图 / 光影 / 色彩 / 清晰度 / 主体 / 情绪 / 故事 / 发布价值）+ 拟人化摄影师点评。
> L25: - **多模型适配**：内置智谱 GLM-V4、OpenAI GPT、Google Gemini、Anthropic Claude 等视觉模型，也支持任意 OpenAI 兼容端点。

## 星数曲线

```mermaid
xychart-beta
    title "laoziocean-code/ai-photo-manager 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-27", "2026-10-28"]
    y-axis "stars" 28 --> 33
    line [29, 30, 31, 32, 32]
```

2026-10-18 29 → 2026-10-28 32（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `87ea58e500be` · [字段定义](../../DATASET.md)*
