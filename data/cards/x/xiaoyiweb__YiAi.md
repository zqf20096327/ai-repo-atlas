# xiaoyiweb/YiAi

⭐ 157 · Vue · MIT · 推送 2026-05-11 · [GitHub](https://github.com/xiaoyiweb/YiAi) · 个人维护 · 中文 README

**自托管 AI 对话平台：聚合 GPT/Claude/MJ 等模型的 ChatWeb**

基于 NineAi 2.4.2 二次开发的全套源码 AI 对话站点，含开箱即用整合包与自行编译包两条部署路径。提供用户端 chat 与管理端 admin，支持 gpt-4o、claude3.5 等模型接入与识图、文件分析、dall-e 绘画整合进 chat、Midjourney（mj-proxy-plus）绘图、模型排序与 Token 计费。运行需 Node.js/pnpm/MySQL/Redis，用 PM2 启动并监听 9520 端口。README 声明仅供学习参考、不可商用，作者提供有偿部署咨询。

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

- 支持 gpt-4o 识图与文件分析、dall-e 绘画整合进 chat
- Midjourney 绘图经 mj-proxy-plus 接入，含容错重试
- 管理端/用户端分离，支持模型关联 Token 计费
- 提供整合包（开箱即用）与编译包两种部署方式

## 适用场景

- 自建聚合多家模型的 AI 对话站点
- 运营带计费与后台管理的 AI SaaS 服务（需注意不可商用声明）
- 学习 NineAI 类对话平台的源码实现

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L11: 1. **更新模型列表，新增gpt-4o、claude3.5等热门模型**：
> L47: 4. **dall-e 绘画整合进 chat**：
> L126: - **chat端地址**：`/chat`

## 星数曲线

```mermaid
xychart-beta
    title "xiaoyiweb/YiAi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 156 --> 158
    line [157, 157]
```

2026-10-18 157 → 2026-10-27 157（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4095b5cb4beb` · [字段定义](../../DATASET.md)*
