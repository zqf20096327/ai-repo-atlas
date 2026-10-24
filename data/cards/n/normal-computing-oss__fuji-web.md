# normal-computing-oss/fuji-web

⭐ 597 · TypeScript · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/normal-computing-oss/fuji-web) · 组织维护

**浏览器侧栏 AI agent，自动浏览网页并代用户执行任务**

Chrome 浏览器扩展，以侧栏形式运行的 AI agent：理解用户意图后自主导航网站、逐步执行任务并解释每步操作。安装方式为从 releases 下载 zip 解压后以开发者模式加载，也可用 Node.js 与 pnpm 从源码构建。使用时需用户提供 OpenAI 或 Anthropic API key（存储在本地浏览器），所有文本与图像提示词直接发送至所选 API。图像标注方法参考了 Microsoft UFO 论文，侧栏形态受 TaxyAI 启发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以浏览器侧栏形式运行，自主导航并逐步执行任务
- 支持 OpenAI 与 Anthropic API key，密钥仅存于本地浏览器
- 提供 releases 下载包与 pnpm 源码构建两种途径

## 适用场景

- 让 AI 代为在网页上完成重复性操作任务
- 通过一句指令驱动浏览器自动办理在线事务
- 观察 AI 逐步解释其在网页上的每个操作

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Fuji-Web is an intelligent AI partner that understands the user’s intent, navigates websites autonomously, and execu
> L31: 2. Create or access an existing OpenAI API Key or Anthropic API key and paste it in the provided box. This key will

## 星数曲线

```mermaid
xychart-beta
    title "normal-computing-oss/fuji-web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 596 --> 598
    line [597, 597]
```

2026-10-18 597 → 2026-10-24 597（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `054033a9a7c9` · [字段定义](../../DATASET.md)*
