# google-marketing-solutions/scene-machine

⭐ 42 · TypeScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/google-marketing-solutions/scene-machine) · 组织维护

**面向广告创意团队的 Google Cloud 故事板驱动 AI 视频广告生成工作台**

构建在 Google Cloud 上的开源工作台：用户上传产品图片与业务背景，由 Gemini 自动生成结构化提示词故事板，后端向 Veo 模型并行发送文生视频/图生视频请求，用户可逐场景迭代提示词，再在合成阶段添加转场、音频与品牌贴图，最终渲染并导出 MP4。面向广告主、开发者与创意团队。部署依赖 GCP 计费项目、Cloud Run（app/worker）、Firestore、IAP 登录门禁等一整套 Google Cloud API；项目与生成媒体在获准用户间共享，无按用户隔离的所有权；另有无需登录的本地开发模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 自动生成结构化提示词故事板，支持 Creative Templates 与空白故事板
- Veo 模型并行图生视频/文生视频，逐场景非破坏式迭代
- 合成阶段支持转场、背景音乐/配音与像素级品牌贴图
- 渲染历史保留多个创意版本，支持 MP4 下载

## 适用场景

- 把商品或服务图片快速转成视频广告
- 创意团队快速原型化并迭代多个广告创意版本
- 零售、外卖、旅行等行业的视频素材生产

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L6: Scene Machine is a Google Cloud-based, open-source workbench that leverages
> L18: - **Key Technology:** Harnesses
> L21:  high-fidelity, parallel image-to-video generation. The entire workflow is

## 星数曲线

```mermaid
xychart-beta
    title "google-marketing-solutions/scene-machine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d7fae031bee3` · [字段定义](../../DATASET.md)*
