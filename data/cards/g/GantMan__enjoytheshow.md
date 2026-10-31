# GantMan/enjoytheshow

⭐ 41 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/GantMan/enjoytheshow) · [官网](https://enjoyingthe.show/) · 个人维护

**实时采集观众面部表情并汇总为房间情绪图表的 Web 应用**

基于 React 19 与 TensorFlow.js（@vladmandic/face-api）的 Web 应用：观众在浏览器中授权摄像头，本地检测面部表情后仅上传情绪词，经 AWS AppSync GraphQL 与 DynamoDB 汇总，演讲者页面以 Victory 饼图实时展示房间整体情绪。前端构建用 Vite 并预渲染首页，模型权重从 public/ 目录加载，部署依赖 AWS Amplify Hosting 与 API key 认证（附自动续期脚本）。提供 npm 安装与 Amplify CLI 自建后端的流程。

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

- 浏览器本地 face-api 面部表情检测，仅上传情绪词
- AppSync GraphQL + DynamoDB 汇总房间情绪为实时饼图
- 首页 Vite 构建时预渲染，含 llms.txt 与 JSON-LD 结构化数据
- API key 到期自动续期的 Lambda + EventBridge 方案

## 适用场景

- 演讲/演出时实时查看观众整体情绪分布
- 多人房间内聚合表情反馈做氛围统计
- 自建一套表情采集与展示服务

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L7: This app uses face-api to gauge your facial expression, and then sends all faces in a particular URL or (room) to a 
> L19: - @vladmandic/face-api (TensorFlow.js) for face detection + expressions, lazy-loaded only on `/room/*`. Model weigh

## 星数曲线

```mermaid
xychart-beta
    title "GantMan/enjoytheshow 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-29 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `25510c3fdbeb` · [字段定义](../../DATASET.md)*
