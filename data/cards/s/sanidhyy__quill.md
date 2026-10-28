# sanidhyy/quill

⭐ 27 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/sanidhyy/quill) · [官网](https://ai-quill.vercel.app/) · 个人维护

**面向学生的 PDF 对话问答 SaaS 应用**

基于 Next.js/React/TypeScript 的开源 Web 应用：用户上传 PDF 文件后可向 AI 提问。功能包含 Kinde 账号认证、Uploadthing 文件上传、Neon PostgreSQL 存储、Pinecone 向量检索、Stripe 订阅付费（Pro 计划）与现代 UI。依赖 @ai-sdk/openai、LangChain、pdf-parse 等实现问答。部署通过 Vercel，本地运行需配置十余项环境变量后 npm run dev 启动。

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

- 上传 PDF 并向 AI 提问的对话式问答
- Kinde 认证 + Uploadthing 上传 + Neon PostgreSQL + Pinecone 向量检索的组合栈
- Stripe 集成支持 Pro 付费计划

## 适用场景

- 上传课程 PDF 资料后直接提问获取答案
- 搭建带认证与付费订阅的自托管文档问答服务
- 作为 Next.js 全栈 SaaS 模板学习参考

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L1: # Quill - The SaaS for Students
> L135: Ask any question to AI

## 星数曲线

```mermaid
xychart-beta
    title "sanidhyy/quill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9c33b5f4e836` · [字段定义](../../DATASET.md)*
