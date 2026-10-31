# huymert/Staff-Management-Application

⭐ 17 · Java · 推送 2026-07-05 · [GitHub](https://github.com/huymert/Staff-Management-Application) · 组织维护

**Android 员工管理应用：RBAC 权限、实时聊天与 RAG AI 助手**

越南 VNU-HCM 理科大学移动编程课程团队项目。Java 编写的 Android 应用，基于 Firebase（认证、Firestore、Storage、FCM）实现角色分级访问控制（管理员/经理/员工三级仪表盘）、考勤日历、任务板、薪资统计与实时单聊/群聊。AI 部分为接入 Gemini API 与 RAG 后端的 HR 聊天机器人，回答公司政策与薪资问题；RAG 后端由团队成员单独开发，需本地或 ngrok 隧道运行，预构建 APK 的 AI 功能依赖开发者后端在线。克隆后需手动配置 google-services.json 与 local.properties 中的 RAG 地址和密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级角色（管理员/经理/员工）RBAC 与对应仪表盘
- 基于 Gemini API + RAG 的公司政策问答 AI 助手
- Firebase 认证、Firestore、实时单聊/群聊、FCM
- 15+ 条手动测试用例与 RBAC 访问限制验证

## 适用场景

- 企业内部用统一 App 管理考勤、任务、请假与薪资
- 员工通过 AI 助手查询公司政策与内部规章
- 按角色分级控制不同功能与数据可见范围

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: A comprehensive mobile staff management application integrated with a RAG-based AI Assistant. This project was devel
> L45: The HR AI Chatbot helps answer company policies, salary calculations, and internal guidelines. It utilizes the **Ge
> L48: * **Server Note**: Since the RAG backend server is hosted locally (or tunneled via services like ngrok) during deve

## 星数曲线

```mermaid
xychart-beta
    title "huymert/Staff-Management-Application 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a36062107d3b` · [字段定义](../../DATASET.md)*
