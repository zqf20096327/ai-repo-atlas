# sansan-mei/page-agent-lite

⭐ 3 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/sansan-mei/page-agent-lite) · [官网](https://sansan-mei.github.io/page-agent-lite/) · 个人维护 · 中文 README

**让浏览器网页任务自动执行的轻量 Chrome/Edge 扩展**

AI 驱动的浏览器插件：在侧栏输入目标，助手按授权进入网站，读取 DOM、填写表单、点击翻页，并核对页面实际结果。支持中途补充指令与停止、IndexedDB 本机长期笔记、长任务上下文压缩。无需 Python、独立后端或构建步骤，使用用户现有登录状态与自己配置的模型 API。模型需支持 OpenAI 兼容 tools 或稳定输出 JSON，要求 Chrome/Edge 120+。项目自述处于早期，不含遥测与自有云端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取 DOM 并执行填写、点击、滚动等网页操作，附结果核对逻辑
- IndexedDB 网站/全局长期笔记，可查看、编辑、导出
- 通过 OpenAI Chat Completions 兼容接口接入自选模型，支持本机服务
- 免构建安装：商店安装或加载已解压的 extension/ 目录

## 适用场景

- 让助手按指令逐页查看条目并筛选符合条件的内容
- 按提供的信息自动填写网页表单，提交前人工检查
- 读取网页内容并整理成要点

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L4:  AI驱动的轻量浏览器插件，能持续自动化帮你处理浏览器事务
> L12: 在浏览器侧栏说出目标，从新标签页也能开始；助手按授权进入网站，读取网页、填写表单、点击和翻页，再检查实际结果。使用你现有的登录状态和自己的模型 API，无需 Python、独立后端或构建步骤。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `aeb96b2ccbca` · [字段定义](../../DATASET.md)*
