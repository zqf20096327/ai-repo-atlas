# Angel2mp3/Grok-Enhancer

⭐ 32 · JavaScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/Angel2mp3/Grok-Enhancer) · 个人维护

**增强 Grok 网页客户端的用户脚本：隐私隐藏、下载、界面定制**

纯原生 JS 编写的浏览器用户脚本，通过 Violentmonkey/Tampermonkey 安装，运行于 grok.com 页面并以 document-start 拦截请求。功能包括：隐藏 Premium 升级提示与弹窗、显示查询速率限制与每周用量条、隐私模式（按敏感词类目隐藏/模糊会话，配 PIN 锁、闲置自动锁与紧急热键）、Imagine 菜单面板（视频长度绕过、审核自动重试、提示词库）、自定义回复风格注入、图片/视频下载器、链接可点击化等。设置仅存 localStorage，脚本自身不发送外部请求、无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 隐私模式按敏感词类目（NSFW/医疗/药物等）隐藏或模糊会话，支持 PIN 锁与紧急热键
- Imagine 面板：拦截视频时长限制、审核自动重试与提示词混淆重写
- 拦截图片/视频 API 响应，注入下载按钮与批量下载，HD 原始链接
- 拦截 fetch 注入自定义回复风格指令到聊天请求

## 适用场景

- 隐藏 Grok 界面上的升级推销与各类弹窗
- 在共享电脑上隐藏或模糊敏感话题会话
- 批量下载 Grok 生成的图片和视频
- 给 Grok 对话固定附加自定义风格指令

## 场景标签

 · 领域:浏览器用户脚本/AI 客户端增强

## 证据(README 行号)

> L3: ** The all-in-one Grok userscript that you could ever need! **
> L11: > Requires a userscript manager like Violentmonkey or Tampermonkey (Chrome / Edge / Firefox / Safari)
> L121: Create and manage custom response style instructions that get prepended to your messages. When a style is active, 

## 星数曲线

```mermaid
xychart-beta
    title "Angel2mp3/Grok-Enhancer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9aa22436d549` · [字段定义](../../DATASET.md)*
