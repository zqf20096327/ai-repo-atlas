# wangfenghuan/ai-draw-io-backend

⭐ 14 · Java · 推送 2026-04-09 · [GitHub](https://github.com/wangfenghuan/ai-draw-io-backend) · [官网](https://www.intellidraw.top) · 个人维护 · 中文 README

**Draw.io 后端服务：Spring Boot+Node.js，含 AI 辅助绘图**

面向构建绘图平台的开发者，提供 Draw.io 后端服务：Spring Boot 处理业务逻辑、用户管理、文件存储与 AI 对话接口；Node.js（Hocuspocus + Yjs CRDT）微服务负责基于 WebSocket 的实时多人协作与增量同步，快照写回 MySQL。AI 部分通过 Spring AI + OpenAI API 提供自然语言生成流程图、AI 编辑与智能续写，流式输出。运行需 JDK 21+、Node.js 18+、MySQL、Redis、MinIO。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成/编辑/续写流程图（Spring AI + OpenAI API）
- Hocuspocus + Yjs CRDT 实时多人协作与增量二进制同步
- MinIO/S3 对象存储与 Redisson 分布式锁
- 双语（中英）README，双服务分别启动

## 适用场景

- 搭建支持多人实时协作的 Draw.io 绘图平台
- 让用户用自然语言生成和修改流程图
- 构建带 AI 对话接口的图表 SaaS 后端

## 场景标签

 · 领域:可视化/协作文档后端

## 证据(README 行号)

> L15: > A high-performance Draw.io backend service powered by Spring Boot 3 + Spring AI + Node.js. Supports real-time col
> L26: - **Text-to-Diagram**: Generate flowcharts directly from natural language descriptions.
> L31: #### 🤝 2. Real-time Collaboration (Node.js)

## 星数曲线

```mermaid
xychart-beta
    title "wangfenghuan/ai-draw-io-backend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4e61bc423029` · [字段定义](../../DATASET.md)*
