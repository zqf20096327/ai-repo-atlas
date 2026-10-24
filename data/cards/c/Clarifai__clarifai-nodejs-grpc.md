# Clarifai/clarifai-nodejs-grpc

⭐ 50 · JavaScript · NOASSERTION · 推送 2026-07-14 · [GitHub](https://github.com/Clarifai/clarifai-nodejs-grpc) · [官网](https://docs.clarifai.com) · 组织维护

**Clarifai 平台官方 Node.js gRPC 客户端，调用其识别 API**

Clarifai 官方维护的 Node.js gRPC 客户端库，用于访问 Clarifai 平台的识别 API，覆盖图像、视频与文本的计算机视觉和 NLP 能力。提供两种使用方式：动态方式（ClarifaiStub.grpc() 构造 stub）与静态方式（V2Client，附 TypeScript 声明文件以增强 IDE 补全），两者 API 能力相同。通过 gRPC Metadata 携带 API key 认证，版本号前两位跟随后端 API 版本，不支持语义化版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 官方 gRPC 客户端，覆盖 Clarifai API 全部方法
- 动态与静态两种调用方式，静态方式提供 TypeScript 类型标注
- 版本号前两位跟随 Clarifai API 后端版本

## 适用场景

- Node.js 项目中调用 Clarifai 的图像/文本识别模型
- 以类型补全友好的方式集成 Clarifai 平台能力
- 查询 Clarifai 公开或自定义模型的预测输出

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: This is the official Clarifai gRPC Node.js client for interacting with our powerful recognition
> L39: Construct the Clarifai stub, which contains all the methods available in the Clarifai API, and the `Metadata`

## 星数曲线

```mermaid
xychart-beta
    title "Clarifai/clarifai-nodejs-grpc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `04c5cc0b63e2` · [字段定义](../../DATASET.md)*
