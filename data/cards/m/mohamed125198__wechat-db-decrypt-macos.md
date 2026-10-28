# mohamed125198/wechat-db-decrypt-macos

⭐ 19 · Python · WTFPL · 推送 2026-10-14 · [GitHub](https://github.com/mohamed125198/wechat-db-decrypt-macos) · 个人维护 · 中文 README

**macOS Apple 芯片上解密微信数据库文件的工具**

面向无需编程知识的用户：在 macOS Apple 芯片（M1/M2 或更新）机器上，从已安装的微信 4.1.2.241 中提取内部密钥，解密 SQLite 数据库文件（如 MM.sqlite），生成 MM_decrypted.sqlite 等可读文件，可用任意 SQLite 浏览器打开。使用方式为下载 macos-arm64 可执行文件后在 Terminal 中运行，传入数据库路径。仅支持微信 4.1.2.241，不支持 4.0 及以下版本，也不能在 Intel Mac 或 Windows 上运行。仓库描述提及搜索与 AI 查询集成，但 README 正文未包含相关内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | WTFPL |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从本机已安装的微信 4.1.2.241 提取密钥解密 SQLite 数据库
- 提供 macos-arm64 可执行文件，Terminal 单命令运行，无需编程知识
- 输出 MM_decrypted.sqlite，可用任意 SQLite 浏览器打开

## 适用场景

- 我在 Mac 上无法直接读取微信的加密数据库文件，需要解密后导出聊天记录
- 我拿到 MM.sqlite 后想用 DB Browser 等工具浏览和搜索内容

## 场景标签

 · 领域:桌面工具/数据解密

## 证据(README 行号)

> L7: wechat-db-decrypt-macos is a tool designed to decrypt WeChat databases on macOS with Apple silicon (arm64). It works
> L100: wechat-db-decrypt-macos uses the internal keys from your installed WeChat 4.1.2.241 to unlock the encrypted SQLite

## 星数曲线

```mermaid
xychart-beta
    title "mohamed125198/wechat-db-decrypt-macos 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `aff8180f7ffd` · [字段定义](../../DATASET.md)*
