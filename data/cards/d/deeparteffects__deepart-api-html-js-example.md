# deeparteffects/deepart-api-html-js-example

⭐ 34 · JavaScript · 推送 2026-04-01 · [GitHub](https://github.com/deeparteffects/deepart-api-html-js-example) · [官网](https://developer.deeparteffects.com) · 组织维护

**Deep Art Effects 风格迁移 API 的 JavaScript 网页示例**

官方示例工程：演示如何在网页 JavaScript 中调用 Deep Art Effects 的神经风格迁移云 API，流程为配置 apiKey/accessKey/secretKey 创建客户端实例、stylesGet 获取可用风格列表、上传 Base64 图像并指定 styleId 提交、通过 submissionId 轮询 resultGet 获取生成结果的下载 URL。风格迁移由远程 API 完成，示例本身仅含前端调用代码，本地不做模型推理。支持 Docker Compose 运行，容器挂载项目文件实现改动即时生效，应用暴露在 localhost:8080。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 演示 Deep Art Effects API 完整调用流程：列风格、上传图像、轮询取结果
- 使用 axios 与 CryptoJS（HMAC-SHA256）构建带签名的 API 请求
- 提供 Docker Compose 运行方式，文件以卷挂载实现热更新

## 适用场景

- 学习如何在 JavaScript 网页中接入 Deep Art Effects 风格迁移 API
- 作为自建图像风格迁移 Web 应用的起步模板
- 在本地通过 Docker 快速运行并修改示例代码调试 API 调用

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: Here is an example on how you can use the Deep Art Effects API for JavaScript to
> L3: display available styles, upload an image and get the result.

## 星数曲线

```mermaid
xychart-beta
    title "deeparteffects/deepart-api-html-js-example 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd3350d5f619` · [字段定义](../../DATASET.md)*
