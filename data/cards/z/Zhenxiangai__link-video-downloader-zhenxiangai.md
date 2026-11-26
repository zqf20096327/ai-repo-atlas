# Zhenxiangai/link-video-downloader-zhenxiangai

⭐ 10 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/Zhenxiangai/link-video-downloader-zhenxiangai) · 个人维护 · 中文 README

**给 Codex/Hermes 代理用的 Mac 视频下载归档与逐字稿 Skill**

安装到 Codex 或 Hermes 代理上的本地内容归档 Skill：把微信公众号、视频号、B站、小红书或抖音链接发给代理，后台完成下载、目录整理与本机音频转写，输出原视频、TXT/SRT/JSON 三种逐字稿及任务清单（含文件大小与校验值）。支持单条链接和博主历史批量抓取，批量先盘点再确认范围，任务按平台内容标识幂等复用；登录态从已登录浏览器导入，视频号依赖微信 Mac 版会话，失效时进入受控恢复窗口由用户手动操作。仅支持 Apple Silicon Mac，逐字稿不做润色或总结。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持微信公众号/视频号/B站/小红书/抖音的下载归档与博主批量抓取
- 本机生成 TXT/SRT/JSON 三种逐字稿，保留时间线且不润色改写
- 任务清单记录文件大小与校验值，按平台内容标识幂等复用任务
- 数据默认保存在本机 ~/Documents/WeChatArchive，不自动上传第三方

## 适用场景

- 把视频链接发给 Mac 上的代理，后台完成下载和逐字稿
- 批量归档喜欢的B站、抖音博主历史视频
- 本地保存公众号文章正文与配图

## 场景标签

`语音识别` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L20: 这是一个可供 Codex 或 Hermes 使用的本地内容归档 Skill。安装并完成首次设置后，你只需要把链接发给已安装该 Skill 的代理：
> L63: 下载完成后，项目会在本机提取音频并生成：
> L276: 安装器复用 Hermes 自带 Python，并安装或复用固定透明派生核心、FFmpeg、whisper.cpp、固定模型和视频号后端。它管理视频号后端、转写 worker 和内容 worker 三个用户级后台服务。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0b28b97d7e9c` · [字段定义](../../DATASET.md)*
